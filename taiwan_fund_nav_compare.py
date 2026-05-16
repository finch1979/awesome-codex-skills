#!/usr/bin/env python3
"""
Compare Allianz Taiwan Intelligence Trends Fund with 0050.

This is exploratory research, not investment advice. Fund NAV data is fetched
from Anue Cnyes' public fund API; 0050 prices are fetched from Yahoo Finance.
"""

import argparse
import csv
import datetime as dt
import json
import os
import urllib.request

from taiwan_mean_reversion_backtest import (
    add_months,
    investment_period_rows,
    metrics,
    pct_change,
    simulate_investment_plan,
    yahoo_chart,
)


def cnyes_nav_payload_to_prices(payload):
    items = payload.get("items", {})
    timestamps = items.get("tradeDate") or []
    navs = items.get("nav") or []
    prices = {}
    for index, timestamp in enumerate(timestamps):
        if index >= len(navs) or navs[index] is None:
            continue
        date = dt.datetime.utcfromtimestamp(int(timestamp)).date()
        prices[date] = float(navs[index])
    return dict(sorted(prices.items()))


def fetch_cnyes_fund_nav(fund_id, start_date):
    start_ts = int(dt.datetime(start_date.year, start_date.month, start_date.day, tzinfo=dt.timezone.utc).timestamp())
    url = "https://fund.api.cnyes.com/fund/api/v1/funds/{0}/nav?startAt={1}".format(fund_id, start_ts)
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://fund.cnyes.com/",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def returns_from_prices(prices):
    returns_by_date = pct_change(prices)
    dates = sorted(returns_by_date)
    returns = [returns_by_date[date] for date in dates]
    return returns, dates


def aligned_growth_points(fund_prices, benchmark_prices, base=100.0):
    common_dates = sorted(set(fund_prices) & set(benchmark_prices))
    if not common_dates:
        return []
    first_date = common_dates[0]
    fund_base = fund_prices[first_date]
    benchmark_base = benchmark_prices[first_date]
    points = []
    for date in common_dates:
        points.append({
            "date": date,
            "fund_growth": base * fund_prices[date] / fund_base if fund_base else 0.0,
            "benchmark_growth": base * benchmark_prices[date] / benchmark_base if benchmark_base else 0.0,
        })
    return points


def first_outperformance_date(points):
    for index, point in enumerate(points):
        if index == 0:
            continue
        if point["fund_growth"] > point["benchmark_growth"]:
            return point["date"]
    return None


def make_equity_curve(daily_returns, start=100.0):
    equity = [start]
    for daily_return in daily_returns:
        equity.append(equity[-1] * (1 + daily_return))
    return equity


def asset_summary(name, daily_returns, dates, initial_amount, monthly_amount):
    equity = make_equity_curve(daily_returns)
    lump = simulate_investment_plan(daily_returns, dates, initial_amount=initial_amount, monthly_amount=0)
    monthly = simulate_investment_plan(daily_returns, dates, initial_amount=0, monthly_amount=monthly_amount)
    return {
        "name": name,
        "metrics": metrics(daily_returns, equity),
        "lump_sum": lump,
        "monthly": monthly,
        "periods": investment_period_rows(name, daily_returns, dates, initial_amount, monthly_amount),
    }


def svg_polyline(points, key, x_scale, y_scale):
    return " ".join("{0:.2f},{1:.2f}".format(x_scale(index), y_scale(point[key])) for index, point in enumerate(points))


def write_growth_chart(path, points, fund_name, benchmark_name, crossover_date):
    if not points:
        return
    width = 1100
    height = 620
    left = 80
    right = 40
    top = 50
    bottom = 80
    max_value = max(max(point["fund_growth"], point["benchmark_growth"]) for point in points)
    min_value = min(min(point["fund_growth"], point["benchmark_growth"]) for point in points)
    min_value = min(100.0, min_value)
    value_span = max(max_value - min_value, 1.0)

    def x_scale(index):
        if len(points) == 1:
            return left
        return left + (width - left - right) * index / float(len(points) - 1)

    def y_scale(value):
        return top + (height - top - bottom) * (max_value - value) / value_span

    fund_points = svg_polyline(points, "fund_growth", x_scale, y_scale)
    benchmark_points = svg_polyline(points, "benchmark_growth", x_scale, y_scale)
    grid_values = [100, 250, 500, 1000, 1500, 2000]
    grid_values = [value for value in grid_values if min_value <= value <= max_value]
    first = points[0]["date"].isoformat()
    last = points[-1]["date"].isoformat()
    crossover_text = crossover_date.isoformat() if crossover_date else "none"

    with open(path, "w", encoding="utf-8") as handle:
        handle.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        handle.write('<svg xmlns="http://www.w3.org/2000/svg" width="{0}" height="{1}" viewBox="0 0 {0} {1}">\n'.format(width, height))
        handle.write('<rect width="100%" height="100%" fill="#ffffff"/>\n')
        handle.write('<text x="{0}" y="30" font-family="Arial, Microsoft JhengHei, sans-serif" font-size="22" font-weight="700">10-year growth: {1} vs {2}</text>\n'.format(left, fund_name, benchmark_name))
        handle.write('<text x="{0}" y="55" font-family="Arial, Microsoft JhengHei, sans-serif" font-size="14" fill="#444">Normalized to 100. First outperformance date: {1}</text>\n'.format(left, crossover_text))
        for value in grid_values:
            y = y_scale(value)
            handle.write('<line x1="{0}" y1="{1:.2f}" x2="{2}" y2="{1:.2f}" stroke="#e2e8f0" stroke-width="1"/>\n'.format(left, y, width - right))
            handle.write('<text x="{0}" y="{1:.2f}" font-family="Arial, sans-serif" font-size="12" text-anchor="end" fill="#555">{2:.0f}</text>\n'.format(left - 10, y + 4, value))
        handle.write('<line x1="{0}" y1="{1}" x2="{2}" y2="{1}" stroke="#222" stroke-width="1"/>\n'.format(left, height - bottom, width - right))
        handle.write('<line x1="{0}" y1="{1}" x2="{0}" y2="{2}" stroke="#222" stroke-width="1"/>\n'.format(left, top, height - bottom))
        handle.write('<polyline points="{0}" fill="none" stroke="#0f766e" stroke-width="3"/>\n'.format(fund_points))
        handle.write('<polyline points="{0}" fill="none" stroke="#2563eb" stroke-width="3"/>\n'.format(benchmark_points))
        handle.write('<circle cx="{0:.2f}" cy="{1:.2f}" r="4" fill="#0f766e"/>\n'.format(x_scale(len(points) - 1), y_scale(points[-1]["fund_growth"])))
        handle.write('<circle cx="{0:.2f}" cy="{1:.2f}" r="4" fill="#2563eb"/>\n'.format(x_scale(len(points) - 1), y_scale(points[-1]["benchmark_growth"])))
        handle.write('<text x="{0}" y="{1}" font-family="Arial, sans-serif" font-size="13" fill="#444">{2}</text>\n'.format(left, height - 35, first))
        handle.write('<text x="{0}" y="{1}" font-family="Arial, sans-serif" font-size="13" fill="#444" text-anchor="end">{2}</text>\n'.format(width - right, height - 35, last))
        handle.write('<rect x="{0}" y="80" width="300" height="58" fill="#fff" stroke="#d1d5db"/>\n'.format(width - right - 320))
        handle.write('<line x1="{0}" y1="100" x2="{1}" y2="100" stroke="#0f766e" stroke-width="3"/>\n'.format(width - right - 300, width - right - 260))
        handle.write('<text x="{0}" y="105" font-family="Arial, Microsoft JhengHei, sans-serif" font-size="14">{1}</text>\n'.format(width - right - 250, fund_name))
        handle.write('<line x1="{0}" y1="125" x2="{1}" y2="125" stroke="#2563eb" stroke-width="3"/>\n'.format(width - right - 300, width - right - 260))
        handle.write('<text x="{0}" y="130" font-family="Arial, Microsoft JhengHei, sans-serif" font-size="14">{1}</text>\n'.format(width - right - 250, benchmark_name))
        handle.write("</svg>\n")


def write_comparison(output_dir, fund_summary, benchmark_summary, initial_amount, monthly_amount, source_note, growth_points=None):
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    growth_points = growth_points or []
    crossover_date = first_outperformance_date(growth_points)

    rows = []
    for summary in [fund_summary, benchmark_summary]:
        for plan_key, plan_name in [("lump_sum", "lump_sum"), ("monthly", "monthly")]:
            row = {"asset": summary["name"], "plan": plan_name}
            row.update(summary[plan_key])
            rows.append(row)

    summary_path = os.path.join(output_dir, "summary.md")
    with open(summary_path, "w", encoding="utf-8-sig") as handle:
        handle.write("# Taiwan Fund vs 0050 Investment Comparison\n\n")
        handle.write("This is exploratory research, not investment advice.\n\n")
        handle.write("## Source\n\n")
        handle.write(source_note + "\n\n")
        handle.write("## Growth Crossover\n\n")
        if crossover_date:
            handle.write("The fund first exceeded the 0050 normalized growth curve on **{0}**.\n\n".format(crossover_date.isoformat()))
        else:
            handle.write("The fund did not exceed the 0050 normalized growth curve during the compared period.\n\n")
        handle.write("## Return Metrics\n\n")
        handle.write("| Metric | {0} | {1} |\n".format(fund_summary["name"], benchmark_summary["name"]))
        handle.write("|---|---:|---:|\n")
        for key in ["total_return", "cagr", "volatility", "sharpe", "max_drawdown"]:
            fund_value = fund_summary["metrics"].get(key, 0.0)
            benchmark_value = benchmark_summary["metrics"].get(key, 0.0)
            if key == "sharpe":
                handle.write("| {0} | {1:.2f} | {2:.2f} |\n".format(key, fund_value, benchmark_value))
            else:
                handle.write("| {0} | {1:.2%} | {2:.2%} |\n".format(key, fund_value, benchmark_value))
        handle.write("\n## Investment Plan Comparison\n\n")
        handle.write("Lump sum uses NT${0:,.0f}. Monthly plan contributes NT${1:,.0f} on the first available NAV/trading day of each month.\n\n".format(initial_amount, monthly_amount))
        handle.write("| Asset | Plan | Invested | Ending value | Gain | Return on invested |\n")
        handle.write("|---|---|---:|---:|---:|---:|\n")
        for row in rows:
            handle.write("| {asset} | {plan} | {invested:,.0f} | {ending_value:,.0f} | {gain:,.0f} | {return_on_invested:.2%} |\n".format(**row))
        handle.write("\n## Period Investment Comparison\n\n")
        handle.write("| Asset | Period | Plan | Invested | Ending value | Return on invested | Annualized |\n")
        handle.write("|---|---|---|---:|---:|---:|---:|\n")
        for summary in [fund_summary, benchmark_summary]:
            for row in summary["periods"]:
                if row["period"] in ("1m", "3m", "1y", "3y", "5y"):
                    handle.write("| {asset} | {period} | {plan} | {invested:,.0f} | {ending_value:,.0f} | {return_on_invested:.2%} | {annualized_return_on_invested:.2%} |\n".format(**row))

    investment_path = os.path.join(output_dir, "investment_comparison.csv")
    with open(investment_path, "w", newline="", encoding="utf-8-sig") as handle:
        fieldnames = ["asset", "plan", "invested", "ending_value", "gain", "return_on_invested"]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    period_path = os.path.join(output_dir, "investment_period_comparison.csv")
    with open(period_path, "w", newline="", encoding="utf-8-sig") as handle:
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
        for summary in [fund_summary, benchmark_summary]:
            writer.writerows(summary["periods"])

    growth_path = os.path.join(output_dir, "growth_curve.csv")
    with open(growth_path, "w", newline="", encoding="utf-8-sig") as handle:
        fieldnames = ["date", "fund_growth", "benchmark_growth", "fund_minus_benchmark"]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for point in growth_points:
            writer.writerow({
                "date": point["date"].isoformat(),
                "fund_growth": point["fund_growth"],
                "benchmark_growth": point["benchmark_growth"],
                "fund_minus_benchmark": point["fund_growth"] - point["benchmark_growth"],
            })

    chart_path = os.path.join(output_dir, "growth_chart.svg")
    write_growth_chart(chart_path, growth_points, fund_summary["name"], benchmark_summary["name"], crossover_date)

    return summary_path, investment_path, period_path, growth_path, chart_path


def build_parser():
    parser = argparse.ArgumentParser(description="Compare Allianz Taiwan Intelligence Fund NAV with 0050.")
    parser.add_argument("--fund-id", default="A36019")
    parser.add_argument("--fund-name", default="安聯台灣智慧基金")
    parser.add_argument("--benchmark", default="0050.TW")
    parser.add_argument("--benchmark-name", default="0050 benchmark")
    parser.add_argument("--years", type=int, default=10)
    parser.add_argument("--initial-amount", type=float, default=1000000)
    parser.add_argument("--monthly-amount", type=float, default=20000)
    parser.add_argument("--output", default="taiwan_fund_results")
    return parser


def main():
    args = build_parser().parse_args()
    end_date = dt.date.today()
    start_date = add_months(end_date, -12 * args.years)

    print("Downloading fund NAV {0}...".format(args.fund_id))
    fund_payload = fetch_cnyes_fund_nav(args.fund_id, start_date)
    fund_prices = cnyes_nav_payload_to_prices(fund_payload)
    fund_returns, fund_dates = returns_from_prices(fund_prices)

    print("Downloading benchmark {0}...".format(args.benchmark))
    benchmark_rows = yahoo_chart(args.benchmark, min(fund_prices), max(fund_prices))
    benchmark_prices = {date: row["adj_close"] for date, row in benchmark_rows.items()}
    benchmark_returns, benchmark_dates = returns_from_prices(benchmark_prices)
    growth_points = aligned_growth_points(fund_prices, benchmark_prices)

    fund_summary = asset_summary(args.fund_name, fund_returns, fund_dates, args.initial_amount, args.monthly_amount)
    benchmark_summary = asset_summary(args.benchmark_name, benchmark_returns, benchmark_dates, args.initial_amount, args.monthly_amount)
    source_note = (
        "- Fund NAV: Anue Cnyes public fund API for {0}.\n"
        "- Benchmark: Yahoo Finance adjusted close for {1}.\n"
        "- Date range: {2} to {3}."
    ).format(args.fund_id, args.benchmark, min(fund_prices).isoformat(), max(fund_prices).isoformat())
    paths = write_comparison(args.output, fund_summary, benchmark_summary, args.initial_amount, args.monthly_amount, source_note, growth_points)
    print("Wrote:")
    for path in paths:
        print("  " + path)


if __name__ == "__main__":
    main()
