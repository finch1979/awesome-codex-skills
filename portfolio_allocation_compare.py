#!/usr/bin/env python3
"""
Compare allocation mixes across S&P 500, 0050, and Allianz Taiwan Intelligence.

This is exploratory research, not investment advice.
"""

import argparse
import csv
import datetime as dt
import os

from taiwan_fund_nav_compare import cnyes_nav_payload_to_prices, fetch_cnyes_fund_nav, make_equity_curve
from taiwan_mean_reversion_backtest import (
    add_months,
    metrics,
    pct_change,
    simulate_investment_plan,
    yahoo_chart,
)


def parse_allocation(value):
    name, raw_weights = value.split("=", 1)
    weights = {}
    for part in raw_weights.split(","):
        asset, raw_weight = part.split(":", 1)
        weights[asset.strip()] = float(raw_weight.strip()) / 100.0
    total = sum(weights.values())
    if abs(total - 1.0) > 0.0001:
        raise ValueError("Allocation {0} sums to {1:.2%}, not 100%".format(name, total))
    return name.strip(), weights


def generate_allocation_grid(step=5):
    if step <= 0 or 100 % step != 0:
        raise ValueError("step must divide 100")
    rows = []
    for sp500 in range(0, 101, step):
        for tw50 in range(0, 101 - sp500, step):
            allianz = 100 - sp500 - tw50
            name = "Grid_SP{0:03d}_TW{1:03d}_AZ{2:03d}".format(sp500, tw50, allianz)
            rows.append((name, {
                "sp500": sp500 / 100.0,
                "0050": tw50 / 100.0,
                "allianz": allianz / 100.0,
            }))
    return rows


def aligned_weighted_returns(returns_by_asset, weights):
    common_dates = None
    active_weights = {asset: weight for asset, weight in weights.items() if abs(weight) > 0.000001}
    for asset in active_weights:
        dates = set(returns_by_asset[asset])
        common_dates = dates if common_dates is None else common_dates & dates
    dates = sorted(common_dates or [])
    returns = []
    for date in dates:
        returns.append(sum(returns_by_asset[asset][date] * weight for asset, weight in active_weights.items()))
    return returns, dates


def aligned_weighted_returns_from_prices(prices_by_asset, weights):
    active_weights = {asset: weight for asset, weight in weights.items() if abs(weight) > 0.000001}
    common_dates = None
    for asset in active_weights:
        dates = set(prices_by_asset[asset])
        common_dates = dates if common_dates is None else common_dates & dates
    dates = sorted(common_dates or [])
    if len(dates) < 2:
        return [], []
    returns = []
    return_dates = []
    for index in range(1, len(dates)):
        previous_date = dates[index - 1]
        date = dates[index]
        weighted_return = 0.0
        for asset, weight in active_weights.items():
            previous_price = prices_by_asset[asset][previous_date]
            price = prices_by_asset[asset][date]
            weighted_return += (price / previous_price - 1.0) * weight
        returns.append(weighted_return)
        return_dates.append(date)
    return returns, return_dates


def returns_dict_from_prices(prices):
    return pct_change(prices)


def format_weights(weights):
    return ", ".join("{0} {1:.0%}".format(asset, weight) for asset, weight in weights.items())


def calendar_cagr(equity_curve, dates):
    if not equity_curve or len(equity_curve) < 2 or not dates:
        return 0.0
    years = max((dates[-1] - dates[0]).days / 365.25, 0.000001)
    return (equity_curve[-1] / equity_curve[0]) ** (1 / years) - 1


def portfolio_row(name, weights, prices_by_asset, initial_amount):
    daily_returns, dates = aligned_weighted_returns_from_prices(prices_by_asset, weights)
    equity = make_equity_curve(daily_returns)
    stats = metrics(daily_returns, equity)
    stats["cagr"] = calendar_cagr(equity, dates)
    plan = simulate_investment_plan(daily_returns, dates, initial_amount=initial_amount, monthly_amount=0)
    row = {
        "portfolio": name,
        "weights": format_weights(weights),
        "invested": plan["invested"],
        "ending_value": plan["ending_value"],
        "gain": plan["gain"],
        "return_on_invested": plan["return_on_invested"],
        "cagr": stats.get("cagr", 0.0),
        "volatility": stats.get("volatility", 0.0),
        "sharpe": stats.get("sharpe", 0.0),
        "max_drawdown": stats.get("max_drawdown", 0.0),
    }
    return row


def write_outputs(output_dir, rows, source_note):
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    summary_path = os.path.join(output_dir, "allocation_summary.md")
    with open(summary_path, "w", encoding="utf-8-sig") as handle:
        handle.write("# Allocation Comparison\n\n")
        handle.write("This is exploratory research, not investment advice.\n\n")
        handle.write("## Source\n\n")
        handle.write(source_note + "\n\n")
        handle.write("## Results\n\n")
        handle.write("| Portfolio | Weights | Ending value | Return | CAGR | Volatility | Max drawdown | Sharpe |\n")
        handle.write("|---|---|---:|---:|---:|---:|---:|---:|\n")
        for row in rows:
            handle.write(
                "| {portfolio} | {weights} | {ending_value:,.0f} | {return_on_invested:.2%} | {cagr:.2%} | {volatility:.2%} | {max_drawdown:.2%} | {sharpe:.2f} |\n".format(**row)
            )

    csv_path = os.path.join(output_dir, "allocation_summary.csv")
    with open(csv_path, "w", newline="", encoding="utf-8-sig") as handle:
        fieldnames = [
            "portfolio",
            "weights",
            "invested",
            "ending_value",
            "gain",
            "return_on_invested",
            "cagr",
            "volatility",
            "sharpe",
            "max_drawdown",
        ]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return summary_path, csv_path


def build_parser():
    parser = argparse.ArgumentParser(description="Compare allocation mixes across 00646, 0050, and Allianz A36019.")
    parser.add_argument("--years", type=int, default=10)
    parser.add_argument("--initial-amount", type=float, default=1000000)
    parser.add_argument("--output", default="allocation_results")
    parser.add_argument("--grid-step", type=int, default=0, help="Generate all allocations at this percentage step, e.g. 5.")
    parser.add_argument(
        "--allocation",
        action="append",
        default=[
            "BalancedGrowth=sp500:50,0050:30,allianz:20",
            "Aggressive=sp500:40,0050:30,allianz:30",
            "HighConviction=sp500:35,0050:25,allianz:40",
            "VeryAggressive=sp500:30,0050:20,allianz:50",
            "TaiwanTilt=sp500:30,0050:40,allianz:30",
        ],
    )
    return parser


def main():
    args = build_parser().parse_args()
    end_date = dt.date.today()
    start_date = add_months(end_date, -12 * args.years)

    print("Downloading Allianz A36019 NAV...")
    fund_prices = cnyes_nav_payload_to_prices(fetch_cnyes_fund_nav("A36019", start_date))
    start = min(fund_prices)
    end = max(fund_prices)

    print("Downloading 00646.TW...")
    sp500_rows = yahoo_chart("00646.TW", start, end)
    sp500_prices = {date: row["adj_close"] for date, row in sp500_rows.items()}

    print("Downloading 0050.TW...")
    tw50_rows = yahoo_chart("0050.TW", start, end)
    tw50_prices = {date: row["adj_close"] for date, row in tw50_rows.items()}

    prices_by_asset = {
        "sp500": sp500_prices,
        "0050": tw50_prices,
        "allianz": fund_prices,
    }
    allocations = generate_allocation_grid(args.grid_step) if args.grid_step else [parse_allocation(raw) for raw in args.allocation]

    rows = []
    for name, weights in allocations:
        rows.append(portfolio_row(name, weights, prices_by_asset, args.initial_amount))

    rows.sort(key=lambda row: row["cagr"], reverse=True)
    source_note = (
        "- S&P 500 proxy: 00646.TW Yahoo Finance adjusted close.\n"
        "- Taiwan 50 proxy: 0050.TW Yahoo Finance adjusted close.\n"
        "- Allianz Taiwan Intelligence Fund: Cnyes A36019 NAV.\n"
        "- Date range: {0} to {1}."
    ).format(start.isoformat(), end.isoformat())
    paths = write_outputs(args.output, rows, source_note)
    print("Wrote:")
    for path in paths:
        print("  " + path)


if __name__ == "__main__":
    main()
