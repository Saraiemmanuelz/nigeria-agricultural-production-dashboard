# Reconciliation: dashboard vs data

Every headline figure on the four dashboard pages was recomputed directly from `data/powerbi/*.csv` using `scripts/verify_numbers.py`. All of them match.

Run it yourself from the repository root:

```
python scripts/verify_numbers.py
```

| Figure | Page | Dashboard shows | Recomputed from the data |
|---|---|---|---|
| Total Production | 1 | 6.91bn | 6,910,219,688 t |
| Crop Count | 1 | 92 | 92 |
| Avg Yield kg per ha | 1 | 4.10K | 4,104.05 |
| Peak Year | 1 | 2023 | 2023 |
| CAGR 2000 to 2024 | 1 | 2.6% | 2.62% |
| Staple Share % | 1 | 68.3% | 68.27% |
| Roots & Tubers share | 1, 4 | 51.7% | 51.67% |
| Cereals share | 1 | 16.6% | 16.60% |
| Cassava Production | 2 | 1.83bn | 1,830,037,222 t |
| Cassava share | 3, 4 | 26.5% | 26.48% |
| Staple Production | 2 | 4.72bn | 4,717,763,462 t |
| Avg Annual Output | 2 | 107.97M | 107,972,183 t |
| High Production Records | 2 | 2,428 | 2,428 |
| Avg annual output 1961-1999 | 2, 3 | 62.51M | 62,509,397 t |
| Avg annual output 2000-2009 | 2, 3 | 145.02M | 145,018,595 t |
| Avg annual output 2010-2019 | 2, 3 | 188.00M | 188,001,226 t |
| Avg annual output 2020-2024 | 2, 3 | 228.43M | 228,431,002 t |
| Yams share | 3 | 21.00% | 21.00% |
| Top 10 crops share | 3, 4 | 77.83% | 77.83% |
| Cereal Avg Yield | 3 | 1,508 | 1,507.93 kg/ha |
| Root & Tuber Avg Yield | 3 | 7,403 | 7,402.97 kg/ha |

## Figures quoted in the insight text

| Statement | Recomputed |
|---|---|
| Production rose from 37.6M (1961) to 232.2M tonnes (2024) | 37,627,687 and 232,240,604 t |
| Cassava rose from 7.4M to 62.6M tonnes, about 8.5 times | 7,384,000 and 62,624,946 t |
| Cereal output rose about a third (2000 to 2024) | +33.5% |
| Cereal area stayed near 18M ha | 18.40M (2000) and 18.48M ha (2024) |
| Roots & Tubers area tripled (7.3M to 22.0M ha) | 7.25M and 22.00M ha, 3.03 times |
| Roots & Tubers output grew about 2.25 times | 2.25 times |
| Cassava yield fell from about 9,700 to 5,840 kg/ha | 9,700 and 5,840.5 kg/ha |
| Maize yield rose from about 805 to 2,030 kg/ha | 805.1 and 2,029.8 kg/ha |
| Total including FAO aggregates (not used) | 13,322,065,192 t |
