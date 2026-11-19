# DAX measures explained

All 25 measures and the `Is Staple` calculated column are in [`measures.dax`](measures.dax). This page explains how the most important ones work.

## Excluding FAO aggregates (used in nearly every measure)
```
Total Production = CALCULATE(SUM(Fact_Production[Production]), Dim_Item[Is_Aggregate] = "No")
```
FAOSTAT includes total rows such as "Cereals, primary" that already contain their component crops. Summing everything gives 13.32bn tonnes. The `Is_Aggregate = "No"` filter inside `CALCULATE` leaves 6.91bn. Because the filter sits inside the measure, it still applies when a user changes a slicer.

## Production CAGR 2000 to 2024
```
VAR p0 = CALCULATE([Total Production], Fact_Production[Year] = 2000)
VAR p1 = CALCULATE([Total Production], Fact_Production[Year] = 2024)
RETURN IF(p0 > 0 && p1 > 0, POWER(DIVIDE(p1, p0), 1 / 24) - 1)
```
Compound annual growth rate = (end value / start value) ^ (1 / number of years) - 1. There are 24 years between 2000 and 2024. The `IF` stops the measure returning an error if a slicer removes either year.

## Cumulative Production
```
CALCULATE([Total Production], FILTER(ALL(Dim_Year), Dim_Year[Year] <= MAX(Dim_Year[Year])))
```
`ALL(Dim_Year)` removes the current year filter, and `FILTER` then keeps every year up to the one on the axis, producing a running total from 1961.

## Production Share %
```
DIVIDE([Total Production], CALCULATE([Total Production], ALL(Dim_Item)))
```
The numerator is the production in the current row (an item or a category). The denominator removes all item filters to give total production, so each share is a share of the whole.

## Average annual production (period comparisons)
```
DIVIDE([Total Production], DISTINCTCOUNT(Fact_Production[Year]))
```
Periods have 39, 10, 10 and 5 years, so totals are not comparable. Dividing by the number of years in each period fixes this.

## Peak Year
```
VAR t = ADDCOLUMNS(VALUES(Fact_Production[Year]), "Prod", [Total Production])
RETURN MAXX(TOPN(1, t, [Prod], DESC), Fact_Production[Year])
```
Builds a table of years with their production, keeps the top row, and returns its year.

## Full list

| Group | Measures |
|---|---|
| Core totals | Total Production, Total Area Harvested, Avg Yield kg per ha, Max Yield kg per ha, Crop Count, Avg Production per Item, Crop Production per Hectare |
| Time intelligence | Production LY, YoY Growth %, Cumulative Production, Recent Production 2020 to 2024, Avg Annual Production, Peak Year, Production CAGR 2000 to 2024 |
| Shares and ranking | Production Share %, Production Rank, Cassava Production, Staple Production, Staple Share %, Roots Tubers Share %, High Production Records |
| Crop Performance page | Top Crop, Top Crop Share %, Cereal Avg Yield, Roots Tubers Avg Yield |
