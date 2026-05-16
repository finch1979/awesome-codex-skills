# Taiwan 30-Stock Mean Reversion Backtest

This is exploratory research, not investment advice.

## Data Limits

- Default universe is a current sample list, so it has survivorship bias.
- Yahoo adjusted prices are used as a practical proxy for total-return data.
- Replace the universe with point-in-time TWSE/TEJ data before relying on results.

## Metrics

| Metric | 30-stock strategy | 0050 benchmark |
|---|---:|---:|
| total_return | 477.50% | 596.56% |
| cagr | 20.28% | 22.68% |
| volatility | 20.02% | 19.37% |
| sharpe | 1.02 | 1.15 |
| max_drawdown | -34.62% | -33.83% |

## Investment Plan Comparison

Lump sum uses NT$1,000,000. Monthly plan contributes NT$20,000 on the first trading day of each month.

| Asset | Plan | Invested | Ending value | Gain | Return on invested |
|---|---|---:|---:|---:|---:|
| 30-stock strategy | lump_sum | 1,000,000 | 5,775,001 | 4,775,001 | 477.50% |
| 0050 benchmark | lump_sum | 1,000,000 | 6,965,569 | 5,965,569 | 596.56% |
| 30-stock strategy | monthly | 2,380,000 | 6,204,356 | 3,824,356 | 160.69% |
| 0050 benchmark | monthly | 2,380,000 | 8,520,980 | 6,140,980 | 258.02% |

## Period Investment Comparison

| Asset | Period | Plan | Invested | Ending value | Return on invested | Annualized |
|---|---|---|---:|---:|---:|---:|
| 30-stock strategy | 1y | lump_sum | 1,000,000 | 1,526,972 | 52.70% | 52.74% |
| 30-stock strategy | 1y | monthly | 260,000 | 310,276 | 19.34% | 19.35% |
| 30-stock strategy | 3y | lump_sum | 1,000,000 | 1,667,282 | 66.73% | 18.61% |
| 30-stock strategy | 3y | monthly | 740,000 | 987,966 | 33.51% | 10.13% |
| 30-stock strategy | 5y | lump_sum | 1,000,000 | 2,036,484 | 103.65% | 15.29% |
| 30-stock strategy | 5y | monthly | 1,220,000 | 1,847,598 | 51.44% | 8.66% |
| 0050 benchmark | 1y | lump_sum | 1,000,000 | 2,060,507 | 106.05% | 106.15% |
| 0050 benchmark | 1y | monthly | 260,000 | 378,103 | 45.42% | 45.46% |
| 0050 benchmark | 3y | lump_sum | 1,000,000 | 2,853,820 | 185.38% | 41.92% |
| 0050 benchmark | 3y | monthly | 740,000 | 1,454,498 | 96.55% | 25.31% |
| 0050 benchmark | 5y | lump_sum | 1,000,000 | 2,671,983 | 167.20% | 21.72% |
| 0050 benchmark | 5y | monthly | 1,220,000 | 2,813,300 | 130.60% | 18.19% |

## Latest Holdings

- 2912.TW 統一超
- 6409.TW 旭隼
- 9910.TW 豐泰
- 2357.TW 華碩
- 1476.TW 儒鴻
- 2207.TW 和泰車
- 4966.TWO 譜瑞-KY
- 2360.TW 致茂
- 9914.TW 美利達
- 3529.TWO 力旺
- 2377.TW 微星
- 3406.TW 玉晶光
- 6669.TW 緯穎
- 8046.TW 南電
- 3443.TW 創意
- 2382.TW 廣達
- 2308.TW 台達電
- 2353.TW 宏碁
- 1102.TW 亞泥
- 3034.TW 聯詠
- 5269.TW 祥碩
- 4904.TW 遠傳
- 3706.TW 神達
- 2354.TW 鴻準
- 2330.TW 台積電
- 2317.TW 鴻海
- 2376.TW 技嘉
- 3665.TW 貿聯-KY
- 1504.TW 東元
- 2412.TW 中華電
