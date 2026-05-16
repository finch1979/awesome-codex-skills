import datetime as dt
import unittest

from portfolio_allocation_compare import aligned_weighted_returns, aligned_weighted_returns_from_prices, generate_allocation_grid, parse_allocation


class PortfolioAllocationCompareTests(unittest.TestCase):
    def test_parse_allocation_reads_name_and_weights(self):
        name, weights = parse_allocation("Aggressive=sp500:40,0050:30,allianz:30")

        self.assertEqual(name, "Aggressive")
        self.assertEqual(weights, {"sp500": 0.4, "0050": 0.3, "allianz": 0.3})

    def test_aligned_weighted_returns_uses_common_dates(self):
        returns_by_asset = {
            "a": {dt.date(2024, 1, 2): 0.10, dt.date(2024, 1, 3): 0.20},
            "b": {dt.date(2024, 1, 2): -0.10, dt.date(2024, 1, 3): 0.00},
        }
        returns, dates = aligned_weighted_returns(returns_by_asset, {"a": 0.75, "b": 0.25})

        self.assertEqual(dates, [dt.date(2024, 1, 2), dt.date(2024, 1, 3)])
        self.assertAlmostEqual(returns[0], 0.05)
        self.assertAlmostEqual(returns[1], 0.15)

    def test_aligned_weighted_returns_ignores_zero_weight_assets(self):
        returns_by_asset = {
            "a": {dt.date(2024, 1, 2): 0.10, dt.date(2024, 1, 3): 0.20},
            "b": {dt.date(2024, 1, 3): 0.00},
        }
        returns, dates = aligned_weighted_returns(returns_by_asset, {"a": 1.0, "b": 0.0})

        self.assertEqual(dates, [dt.date(2024, 1, 2), dt.date(2024, 1, 3)])
        self.assertEqual(returns, [0.10, 0.20])

    def test_generate_allocation_grid_uses_step_and_sums_to_one(self):
        rows = generate_allocation_grid(step=50)

        self.assertEqual(len(rows), 6)
        for name, weights in rows:
            self.assertTrue(name.startswith("Grid_"))
            self.assertAlmostEqual(sum(weights.values()), 1.0)

    def test_aligned_weighted_returns_from_prices_uses_price_change_between_common_dates(self):
        prices_by_asset = {
            "a": {
                dt.date(2024, 1, 1): 100.0,
                dt.date(2024, 1, 2): 110.0,
                dt.date(2024, 1, 3): 121.0,
            },
            "b": {
                dt.date(2024, 1, 1): 100.0,
                dt.date(2024, 1, 3): 110.0,
            },
        }

        returns, dates = aligned_weighted_returns_from_prices(prices_by_asset, {"a": 0.5, "b": 0.5})

        self.assertEqual(dates, [dt.date(2024, 1, 3)])
        self.assertAlmostEqual(returns[0], 0.155)


if __name__ == "__main__":
    unittest.main()
