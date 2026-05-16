import math
import unittest

from taiwan_mean_reversion_backtest import (
    calculate_drawdown,
    linear_regression,
    max_drawdown,
    portfolio_turnover,
    period_slice,
    residual_reversion_score,
    simulate_investment_plan,
)


class TaiwanFundBacktestTests(unittest.TestCase):
    def test_linear_regression_fits_simple_series(self):
        alpha, beta = linear_regression([1, 2, 3], [3, 5, 7])
        self.assertAlmostEqual(alpha, 1.0)
        self.assertAlmostEqual(beta, 2.0)

    def test_max_drawdown_uses_peak_to_trough_loss(self):
        curve = [100, 120, 90, 110, 80]
        self.assertAlmostEqual(max_drawdown(curve), -0.3333333333)

    def test_drawdown_curve_starts_at_zero(self):
        curve = [100, 110, 99]
        drawdowns = calculate_drawdown(curve)
        self.assertEqual(drawdowns[0], 0)
        self.assertAlmostEqual(drawdowns[-1], -0.1)

    def test_turnover_between_equal_weight_portfolios(self):
        old = ["A", "B", "C"]
        new = ["B", "C", "D"]
        self.assertAlmostEqual(portfolio_turnover(old, new), 1 / 3)

    def test_residual_reversion_score_rewards_low_recent_residual(self):
        stock_returns = [0.01] * 40 + [-0.03] * 5
        benchmark_returns = [0.01] * 45
        score = residual_reversion_score(stock_returns, benchmark_returns, residual_window=5)
        self.assertTrue(math.isfinite(score.score))
        self.assertLess(score.residual_z, 0)
        self.assertGreater(score.score, 0)

    def test_lump_sum_plan_invests_once_at_start(self):
        dates = ["2024-01-02", "2024-01-03", "2024-01-04"]
        result = simulate_investment_plan([0.10, -0.05, 0.00], dates, initial_amount=100000, monthly_amount=0)
        self.assertAlmostEqual(result["invested"], 100000)
        self.assertAlmostEqual(result["ending_value"], 104500)
        self.assertAlmostEqual(result["return_on_invested"], 0.045)

    def test_monthly_plan_contributes_on_first_trading_day_of_each_month(self):
        dates = ["2024-01-02", "2024-01-03", "2024-02-01", "2024-02-02"]
        result = simulate_investment_plan([0.10, 0.00, 0.10, 0.00], dates, initial_amount=0, monthly_amount=10000)
        self.assertAlmostEqual(result["invested"], 20000)
        self.assertAlmostEqual(result["ending_value"], 23100)
        self.assertAlmostEqual(result["return_on_invested"], 0.155)

    def test_period_slice_keeps_returns_after_cutoff_date(self):
        dates = ["2024-01-02", "2024-02-01", "2024-03-01"]
        sliced_returns, sliced_dates = period_slice([0.1, 0.2, 0.3], dates, "2024-02-01")
        self.assertEqual(sliced_dates, ["2024-02-01", "2024-03-01"])
        self.assertEqual(sliced_returns, [0.2, 0.3])


if __name__ == "__main__":
    unittest.main()
