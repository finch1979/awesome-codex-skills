#!/usr/bin/env python3
"""
Taiwan 30-stock mean reversion backtest.

This is a research tool, not investment advice. The default universe is a
survivorship-biased sample of currently known Taiwan stocks, so results are
exploratory until replaced with a point-in-time universe and total-return data.
"""

import argparse
import csv
import datetime as dt
import json
import math
import os
import statistics
import time
import urllib.parse
import urllib.request
from collections import namedtuple


Score = namedtuple("Score", "score residual_z beta alpha momentum volatility")


def mean(values):
    values = list(values)
    return sum(values) / len(values) if values else 0.0


def stdev(values):
    values = list(values)
    if len(values) < 2:
        return 0.0
    return statistics.stdev(values)


def product(values):
    result = 1.0
    for value in values:
        result *= value
    return result


def linear_regression(x_values, y_values):
    x = list(x_values)
    y = list(y_values)
    if len(x) != len(y) or len(x) < 2:
        return 0.0, 0.0
    x_mean = mean(x)
    y_mean = mean(y)
    var_x = sum((v - x_mean) ** 2 for v in x)
    if var_x == 0:
        return y_mean, 0.0
    cov_xy = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(len(x)))
    beta = cov_xy / var_x
    alpha = y_mean - beta * x_mean
    return alpha, beta


def pct_change(prices):
    returns = {}
    previous_date = None
    previous_price = None
    for date, price in sorted(prices.items()):
        if previous_price is not None and previous_price > 0:
            returns[date] = price / previous_price - 1.0
        previous_date = date
        previous_price = price
    return returns


def align_returns(stock_returns, benchmark_returns, dates):
    xs = []
    ys = []
    for date in dates:
        if date in stock_returns and date in benchmark_returns:
            xs.append(benchmark_returns[date])
            ys.append(stock_returns[date])
    return ys, xs


def rolling_sums(values, window):
    if len(values) < window:
        return []
    sums = []
    current = sum(values[:window])
    sums.append(current)
    for index in range(window, len(values)):
        current += values[index] - values[index - window]
        sums.append(current)
    return sums


def residual_reversion_score(stock_returns, benchmark_returns, residual_window=20):
    length = min(len(stock_returns), len(benchmark_returns))
    stock = list(stock_returns)[-length:]
    benchmark = list(benchmark_returns)[-length:]
    if length < max(40, residual_window + 5):
        return Score(float("-inf"), 0.0, 0.0, 0.0, 0.0, 0.0)

    alpha, beta = linear_regression(benchmark, stock)
    residuals = [stock[i] - (alpha + beta * benchmark[i]) for i in range(length)]
    residual_roll = rolling_sums(residuals, residual_window)
    if len(residual_roll) < 2:
        return Score(float("-inf"), 0.0, beta, alpha, 0.0, 0.0)

    residual_mean = mean(residual_roll)
    residual_sd = stdev(residual_roll)
    residual_z = 0.0 if residual_sd == 0 else (residual_roll[-1] - residual_mean) / residual_sd
    momentum_window = min(252, length)
    momentum = product([1 + r for r in stock[-momentum_window:]]) - 1.0
    volatility = stdev(stock[-momentum_window:]) * math.sqrt(252)

    # Lower residual_z means the stock recently lagged its own benchmark
    # relationship. Positive momentum avoids selecting pure falling knives.
    score = (-residual_z) + 0.35 * momentum - 0.15 * volatility
    return Score(score, residual_z, beta, alpha, momentum, volatility)


def calculate_drawdown(equity_curve):
    peak = None
    drawdowns = []
    for value in equity_curve:
        if peak is None or value > peak:
            peak = value
        drawdowns.append(0.0 if peak == 0 else value / peak - 1.0)
    return drawdowns


def max_drawdown(equity_curve):
    drawdowns = calculate_drawdown(equity_curve)
    return min(drawdowns) if drawdowns else 0.0


def portfolio_turnover(old_holdings, new_holdings):
    old = set(old_holdings or [])
    new = set(new_holdings or [])
    if not old and not new:
        return 0.0
    if not old:
        return 1.0
    removed = old - new
    added = new - old
    return max(len(removed), len(added)) / float(max(len(old), len(new)))


def parse_date(value):
    return dt.datetime.strptime(value, "%Y-%m-%d").date()


def unix_time(date):
    return int(dt.datetime(date.year, date.month, date.day, tzinfo=dt.timezone.utc).timestamp())


def yahoo_chart(symbol, start_date, end_date, sleep_seconds=0.15):
    period1 = unix_time(start_date)
    period2 = unix_time(end_date + dt.timedelta(days=1))
    params = urllib.parse.urlencode({
        "period1": period1,
        "period2": period2,
        "interval": "1d",
        "events": "history|div|split",
        "includeAdjustedClose": "true",
    })
    url = "https://query1.finance.yahoo.com/v8/finance/chart/{0}?{1}".format(symbol, params)
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.loads(response.read().decode("utf-8"))
    time.sleep(sleep_seconds)

    result = payload.get("chart", {}).get("result", [None])[0]
    if not result:
        return {}
    timestamps = result.get("timestamp") or []
    indicators = result.get("indicators", {})
    quote = (indicators.get("quote") or [{}])[0]
    adjclose = (indicators.get("adjclose") or [{}])[0].get("adjclose") or quote.get("close") or []
    volume = quote.get("volume") or []

    rows = {}
    for index, timestamp in enumerate(timestamps):
        if index >= len(adjclose) or adjclose[index] is None:
            continue
        date = dt.datetime.utcfromtimestamp(timestamp).date()
        rows[date] = {
            "adj_close": float(adjclose[index]),
            "volume": int(volume[index] or 0) if index < len(volume) else 0,
        }
    return rows


def load_universe(path):
    symbols = []
    names = {}
    with open(path, newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            symbol = row["symbol"].strip()
            if not symbol:
                continue
            symbols.append(symbol)
            names[symbol] = row.get("name", "").strip()
    return symbols, names


def rebalance_dates(all_dates, lookback_days, step_days):
    dates = sorted(all_dates)
    result = []
    index = lookback_days
    while index < len(dates) - step_days:
        result.append(dates[index])
        index += step_days
    return result


def metrics(daily_returns, equity_curve):
    if not daily_returns or not equity_curve:
        return {}
    total_return = equity_curve[-1] / equity_curve[0] - 1.0
    years = len(daily_returns) / 252.0
    cagr = (equity_curve[-1] / equity_curve[0]) ** (1 / years) - 1.0 if years > 0 else 0.0
    vol = stdev(daily_returns) * math.sqrt(252)
    sharpe = (mean(daily_returns) * 252) / vol if vol > 0 else 0.0
    return {
        "total_return": total_return,
        "cagr": cagr,
        "volatility": vol,
        "sharpe": sharpe,
        "max_drawdown": max_drawdown(equity_curve),
    }


def normalize_plan_date(value):
    if hasattr(value, "year") and hasattr(value, "month"):
        return value
    return parse_date(str(value))


def simulate_investment_plan(daily_returns, dates, initial_amount=0.0, monthly_amount=0.0):
    value = 0.0
    invested = 0.0
    contributed_months = set()

    if initial_amount:
        value += float(initial_amount)
        invested += float(initial_amount)

    for index, daily_return in enumerate(daily_returns):
        date = normalize_plan_date(dates[index]) if index < len(dates) else None
        if monthly_amount and date:
            month_key = (date.year, date.month)
            if month_key not in contributed_months:
                value += float(monthly_amount)
                invested += float(monthly_amount)
                contributed_months.add(month_key)
        value *= 1 + daily_return

    gain = value - invested
    return {
        "invested": invested,
        "ending_value": value,
        "gain": gain,
        "return_on_invested": gain / invested if invested else 0.0,
    }


def period_slice(daily_returns, dates, cutoff_date):
    cutoff = normalize_plan_date(cutoff_date)
    sliced_returns = []
    sliced_dates = []
    for index, daily_return in enumerate(daily_returns):
        if index >= len(dates):
            break
        date = normalize_plan_date(dates[index])
        if date >= cutoff:
            sliced_returns.append(daily_return)
            sliced_dates.append(dates[index])
    return sliced_returns, sliced_dates


def add_months(date, month_delta):
    month_index = date.month - 1 + month_delta
    year = date.year + month_index // 12
    month = month_index % 12 + 1
    days_in_month = [31, 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = min(date.day, days_in_month[month - 1])
    return dt.date(year, month, day)


def annualize_return(return_on_invested, days):
    years = days / 365.25
    if years <= 0 or return_on_invested <= -1:
        return 0.0
    return (1 + return_on_invested) ** (1 / years) - 1


def investment_period_rows(asset, daily_returns, dates, initial_amount, monthly_amount):
    if not daily_returns or not dates:
        return []
    end_date = normalize_plan_date(dates[-1])
    periods = [
        ("1m", add_months(end_date, -1)),
        ("3m", add_months(end_date, -3)),
        ("1y", add_months(end_date, -12)),
        ("3y", add_months(end_date, -36)),
        ("5y", add_months(end_date, -60)),
        ("full", normalize_plan_date(dates[0])),
    ]
    rows = []
    for label, cutoff in periods:
        period_returns, period_dates = period_slice(daily_returns, dates, cutoff)
        if not period_returns:
            continue
        start_date = normalize_plan_date(period_dates[0])
        days = max((end_date - start_date).days, 1)
        plans = [
            ("lump_sum", initial_amount, 0),
            ("monthly", 0, monthly_amount),
        ]
        for plan, initial, monthly in plans:
            simulated = simulate_investment_plan(period_returns, period_dates, initial_amount=initial, monthly_amount=monthly)
            row = {
                "asset": asset,
                "period": label,
                "start_date": start_date.isoformat(),
                "end_date": end_date.isoformat(),
                "plan": plan,
                "annualized_return_on_invested": annualize_return(simulated["return_on_invested"], days),
            }
            row.update(simulated)
            rows.append(row)
    return rows


def run_backtest(args):
    end_date = parse_date(args.end) if args.end else dt.date.today()
    start_date = parse_date(args.start) if args.start else end_date - dt.timedelta(days=365 * args.years + 370 * 3)
    symbols, names = load_universe(args.universe)
    if args.max_candidates:
        symbols = symbols[:args.max_candidates]

    print("Downloading benchmark {0}...".format(args.benchmark))
    benchmark_rows = yahoo_chart(args.benchmark, start_date, end_date)
    benchmark_prices = {date: row["adj_close"] for date, row in benchmark_rows.items()}
    benchmark_returns = pct_change(benchmark_prices)
    benchmark_dates = sorted(benchmark_returns)

    stock_prices = {}
    stock_returns = {}
    for index, symbol in enumerate(symbols, 1):
        print("[{0}/{1}] Downloading {2}".format(index, len(symbols), symbol))
        try:
            rows = yahoo_chart(symbol, start_date, end_date)
        except Exception as exc:
            print("  skip {0}: {1}".format(symbol, exc))
            continue
        prices = {date: row["adj_close"] for date, row in rows.items()}
        returns = pct_change(prices)
        if len(returns) >= args.lookback_days + args.hold_days:
            stock_prices[symbol] = prices
            stock_returns[symbol] = returns

    dates = benchmark_dates
    rebalances = rebalance_dates(dates, args.lookback_days, args.hold_days)
    holdings = []
    holding_rows = []
    portfolio_daily_returns = []
    benchmark_daily_returns = []
    portfolio_dates = []
    equity = [100.0]
    benchmark_equity = [100.0]
    selected_by_date = {}

    for rebalance_date in rebalances:
        date_index = dates.index(rebalance_date)
        lookback = dates[date_index - args.lookback_days:date_index]
        scored = []
        for symbol, returns in stock_returns.items():
            stock_y, bench_x = align_returns(returns, benchmark_returns, lookback)
            if len(stock_y) < args.lookback_days * 0.75:
                continue
            score = residual_reversion_score(stock_y, bench_x, residual_window=args.residual_window)
            if math.isfinite(score.score):
                scored.append((score.score, symbol, score))
        scored.sort(reverse=True, key=lambda item: item[0])
        new_holdings = [symbol for _, symbol, _ in scored[:args.top_n]]
        selected_by_date[rebalance_date] = new_holdings
        turnover = portfolio_turnover(holdings, new_holdings)
        holdings = new_holdings
        holding_rows.extend([
            {
                "rebalance_date": rebalance_date.isoformat(),
                "rank": rank,
                "symbol": symbol,
                "name": names.get(symbol, ""),
                "score": score.score,
                "residual_z": score.residual_z,
                "momentum": score.momentum,
                "volatility": score.volatility,
            }
            for rank, (_, symbol, score) in enumerate(scored[:args.top_n], 1)
        ])

        hold_dates = dates[date_index: min(date_index + args.hold_days, len(dates))]
        for day_index, date in enumerate(hold_dates):
            day_returns = [stock_returns[symbol][date] for symbol in holdings if date in stock_returns.get(symbol, {})]
            if not day_returns:
                continue
            portfolio_return = mean(day_returns)
            if day_index == 0 and args.transaction_cost > 0:
                portfolio_return -= turnover * args.transaction_cost
            benchmark_return = benchmark_returns.get(date, 0.0)
            portfolio_daily_returns.append(portfolio_return)
            benchmark_daily_returns.append(benchmark_return)
            portfolio_dates.append(date)
            equity.append(equity[-1] * (1 + portfolio_return))
            benchmark_equity.append(benchmark_equity[-1] * (1 + benchmark_return))

    return {
        "args": args,
        "names": names,
        "equity": equity,
        "benchmark_equity": benchmark_equity,
        "portfolio_daily_returns": portfolio_daily_returns,
        "benchmark_daily_returns": benchmark_daily_returns,
        "portfolio_dates": portfolio_dates,
        "holding_rows": holding_rows,
        "selected_by_date": selected_by_date,
        "available_symbols": sorted(stock_returns),
    }


def write_outputs(result, output_dir):
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    portfolio_metrics = metrics(result["portfolio_daily_returns"], result["equity"])
    benchmark_metrics = metrics(result["benchmark_daily_returns"], result["benchmark_equity"])
    args = result["args"]
    investment_rows = [
        {
            "asset": "30-stock strategy",
            "plan": "lump_sum",
            **simulate_investment_plan(
                result["portfolio_daily_returns"],
                result["portfolio_dates"],
                initial_amount=args.initial_amount,
                monthly_amount=0,
            ),
        },
        {
            "asset": "0050 benchmark",
            "plan": "lump_sum",
            **simulate_investment_plan(
                result["benchmark_daily_returns"],
                result["portfolio_dates"],
                initial_amount=args.initial_amount,
                monthly_amount=0,
            ),
        },
        {
            "asset": "30-stock strategy",
            "plan": "monthly",
            **simulate_investment_plan(
                result["portfolio_daily_returns"],
                result["portfolio_dates"],
                initial_amount=0,
                monthly_amount=args.monthly_amount,
            ),
        },
        {
            "asset": "0050 benchmark",
            "plan": "monthly",
            **simulate_investment_plan(
                result["benchmark_daily_returns"],
                result["portfolio_dates"],
                initial_amount=0,
                monthly_amount=args.monthly_amount,
            ),
        },
    ]
    investment_periods = (
        investment_period_rows(
            "30-stock strategy",
            result["portfolio_daily_returns"],
            result["portfolio_dates"],
            args.initial_amount,
            args.monthly_amount,
        )
        + investment_period_rows(
            "0050 benchmark",
            result["benchmark_daily_returns"],
            result["portfolio_dates"],
            args.initial_amount,
            args.monthly_amount,
        )
    )

    summary_path = os.path.join(output_dir, "summary.md")
    with open(summary_path, "w", encoding="utf-8-sig") as handle:
        handle.write("# Taiwan 30-Stock Mean Reversion Backtest\n\n")
        handle.write("This is exploratory research, not investment advice.\n\n")
        handle.write("## Data Limits\n\n")
        handle.write("- Default universe is a current sample list, so it has survivorship bias.\n")
        handle.write("- Yahoo adjusted prices are used as a practical proxy for total-return data.\n")
        handle.write("- Replace the universe with point-in-time TWSE/TEJ data before relying on results.\n\n")
        handle.write("## Metrics\n\n")
        handle.write("| Metric | 30-stock strategy | 0050 benchmark |\n")
        handle.write("|---|---:|---:|\n")
        for key in ["total_return", "cagr", "volatility", "sharpe", "max_drawdown"]:
            p = portfolio_metrics.get(key, 0.0)
            b = benchmark_metrics.get(key, 0.0)
            if key == "sharpe":
                handle.write("| {0} | {1:.2f} | {2:.2f} |\n".format(key, p, b))
            else:
                handle.write("| {0} | {1:.2%} | {2:.2%} |\n".format(key, p, b))
        handle.write("\n## Investment Plan Comparison\n\n")
        handle.write("Lump sum uses NT${0:,.0f}. Monthly plan contributes NT${1:,.0f} on the first trading day of each month.\n\n".format(
            args.initial_amount,
            args.monthly_amount,
        ))
        handle.write("| Asset | Plan | Invested | Ending value | Gain | Return on invested |\n")
        handle.write("|---|---|---:|---:|---:|---:|\n")
        for row in investment_rows:
            handle.write("| {asset} | {plan} | {invested:,.0f} | {ending_value:,.0f} | {gain:,.0f} | {return_on_invested:.2%} |\n".format(**row))
        handle.write("\n## Period Investment Comparison\n\n")
        handle.write("| Asset | Period | Plan | Invested | Ending value | Return on invested | Annualized |\n")
        handle.write("|---|---|---|---:|---:|---:|---:|\n")
        for row in investment_periods:
            if row["period"] in ("1y", "3y", "5y"):
                handle.write(
                    "| {asset} | {period} | {plan} | {invested:,.0f} | {ending_value:,.0f} | {return_on_invested:.2%} | {annualized_return_on_invested:.2%} |\n".format(**row)
                )
        handle.write("\n## Latest Holdings\n\n")
        latest_date = max(result["selected_by_date"]) if result["selected_by_date"] else None
        if latest_date:
            for symbol in result["selected_by_date"][latest_date]:
                handle.write("- {0} {1}\n".format(symbol, result["names"].get(symbol, "")))

    equity_path = os.path.join(output_dir, "equity_curve.csv")
    with open(equity_path, "w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.writer(handle)
        writer.writerow(["index", "date", "strategy_equity", "benchmark_equity"])
        row_count = min(len(result["equity"]), len(result["benchmark_equity"]))
        for index in range(row_count):
            date = "" if index == 0 or index - 1 >= len(result["portfolio_dates"]) else result["portfolio_dates"][index - 1].isoformat()
            writer.writerow([index, date, result["equity"][index], result["benchmark_equity"][index]])

    investment_path = os.path.join(output_dir, "investment_comparison.csv")
    with open(investment_path, "w", newline="", encoding="utf-8-sig") as handle:
        fieldnames = ["asset", "plan", "invested", "ending_value", "gain", "return_on_invested"]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(investment_rows)

    investment_period_path = os.path.join(output_dir, "investment_period_comparison.csv")
    with open(investment_period_path, "w", newline="", encoding="utf-8-sig") as handle:
        fieldnames = [
            "asset",
            "period",
            "start_date",
            "end_date",
            "plan",
            "invested",
            "ending_value",
            "gain",
            "return_on_invested",
            "annualized_return_on_invested",
        ]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(investment_periods)

    holdings_path = os.path.join(output_dir, "rebalance_holdings.csv")
    with open(holdings_path, "w", newline="", encoding="utf-8-sig") as handle:
        fieldnames = ["rebalance_date", "rank", "symbol", "name", "score", "residual_z", "momentum", "volatility"]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(result["holding_rows"])

    return summary_path, equity_path, holdings_path, investment_path, investment_period_path


def build_parser():
    parser = argparse.ArgumentParser(description="Backtest a Taiwan 30-stock mean reversion strategy against 0050.")
    parser.add_argument("--universe", default="taiwan_sample_universe.csv")
    parser.add_argument("--benchmark", default="0050.TW")
    parser.add_argument("--years", type=int, default=10)
    parser.add_argument("--start")
    parser.add_argument("--end")
    parser.add_argument("--top-n", type=int, default=30)
    parser.add_argument("--max-candidates", type=int, default=0)
    parser.add_argument("--lookback-days", type=int, default=756)
    parser.add_argument("--hold-days", type=int, default=63)
    parser.add_argument("--residual-window", type=int, default=20)
    parser.add_argument("--transaction-cost", type=float, default=0.003)
    parser.add_argument("--initial-amount", type=float, default=1000000)
    parser.add_argument("--monthly-amount", type=float, default=20000)
    parser.add_argument("--output", default="backtest_results")
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    result = run_backtest(args)
    paths = write_outputs(result, args.output)
    print("Wrote:")
    for path in paths:
        print("  " + path)


if __name__ == "__main__":
    main()
