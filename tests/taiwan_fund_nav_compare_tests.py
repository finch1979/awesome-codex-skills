import datetime as dt
import unittest

from taiwan_fund_nav_compare import cnyes_nav_payload_to_prices
from taiwan_fund_nav_compare import aligned_growth_points, first_outperformance_date


class TaiwanFundNavCompareTests(unittest.TestCase):
    def test_cnyes_nav_payload_to_prices_converts_epoch_dates_and_sorts(self):
        payload = {
            "items": {
                "tradeDate": [1704153600, 1704067200],
                "nav": [11.0, 10.0],
            }
        }
        prices = cnyes_nav_payload_to_prices(payload)

        self.assertEqual(list(prices.keys()), [dt.date(2024, 1, 1), dt.date(2024, 1, 2)])
        self.assertEqual(prices[dt.date(2024, 1, 1)], 10.0)
        self.assertEqual(prices[dt.date(2024, 1, 2)], 11.0)

    def test_aligned_growth_points_normalizes_common_dates(self):
        fund_prices = {
            dt.date(2024, 1, 1): 10.0,
            dt.date(2024, 1, 2): 12.0,
        }
        benchmark_prices = {
            dt.date(2024, 1, 1): 20.0,
            dt.date(2024, 1, 2): 22.0,
        }

        points = aligned_growth_points(fund_prices, benchmark_prices)

        self.assertEqual(points[0]["date"], dt.date(2024, 1, 1))
        self.assertAlmostEqual(points[0]["fund_growth"], 100.0)
        self.assertAlmostEqual(points[0]["benchmark_growth"], 100.0)
        self.assertAlmostEqual(points[1]["fund_growth"], 120.0)
        self.assertAlmostEqual(points[1]["benchmark_growth"], 110.0)

    def test_first_outperformance_date_ignores_starting_tie(self):
        points = [
            {"date": dt.date(2024, 1, 1), "fund_growth": 100.0, "benchmark_growth": 100.0},
            {"date": dt.date(2024, 1, 2), "fund_growth": 99.0, "benchmark_growth": 101.0},
            {"date": dt.date(2024, 1, 3), "fund_growth": 103.0, "benchmark_growth": 102.0},
        ]

        self.assertEqual(first_outperformance_date(points), dt.date(2024, 1, 3))


if __name__ == "__main__":
    unittest.main()
