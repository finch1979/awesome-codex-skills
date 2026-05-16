@echo off
set "SCRIPT_DIR=%~dp0"
python "%SCRIPT_DIR%taiwan_mean_reversion_backtest.py" --years 10 --top-n 30 --lookback-days 756 --hold-days 63 --output "%SCRIPT_DIR%backtest_results"
