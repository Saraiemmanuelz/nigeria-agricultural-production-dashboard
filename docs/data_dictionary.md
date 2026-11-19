# Data dictionary

All tables describe Nigeria, 1961 to 2024. Source: FAOSTAT, *Crops and livestock products*.

## `data/powerbi/Fact_Production.csv` (6,504 rows, one row per item per year)

| Column | Type | Description |
|---|---|---|
| `Year` | whole number | Calendar year, 1961 to 2024 |
| `Item_ID` | whole number | Key to `Dim_Item` |
| `Area_Harvested` | decimal | Harvested area in hectares (ha). Blank for items with no area, such as livestock products |
| `Production` | decimal | Production in tonnes (t) |
| `Yield` | decimal | Yield in kg per hectare (kg/ha), as reported by FAO. Blank when there is no area |
| `Production_Level` | text | `High Production` if the row's production is at or above the median production of all rows, otherwise `Low Production` |
| `Period` | text | `1961-1999`, `2000-2009`, `2010-2019` or `2020-2024` |

## `data/powerbi/Dim_Item.csv` (108 rows, one row per FAOSTAT item)

| Column | Type | Description |
|---|---|---|
| `Item_ID` | whole number | Primary key |
| `Item` | text | FAOSTAT item name, for example `Cassava, fresh` |
| `Crop_Category` | text | Group assigned to each item for this project: Cereals, Roots & Tubers, Pulses, Oilseeds & Nuts, Fruits, Vegetables, Cash & Industrial Crops, Meat & Livestock Products, Dairy & Eggs, Processed Products, or Aggregate (FAO total) |
| `Is_Aggregate` | text | `Yes` for the 16 FAO total rows (such as "Cereals, primary") that already contain other items, otherwise `No`. All measures filter on `No` |

## `Dim_Year` (created in Power Query, 64 rows)

| Column | Type | Description |
|---|---|---|
| `Year` | whole number | 1961 to 2024 |
| `Decade` | whole number | Year rounded down to the decade (1960, 1970, and so on) |

## `data/processed/Nigeria_Agricultural_Production_Final.csv` (output of the Python notebook)

Same data as the fact table before it was split into tables. Extra columns:

| Column | Description |
|---|---|
| `Area` | Always `Nigeria` |
| `Item` | Item name (replaced by `Item_ID` in the Power BI fact table) |
| `Production_per_Hectare` | `Production / Area_Harvested` (tonnes per hectare), blank where there is no area |
| `High_Production` | 1 if `Production_Level` is `High Production`, otherwise 0 (used for the logistic regression in the notebook) |

## Units and conventions

- Production is in tonnes, area in hectares and yield in kg/ha.
- Blank means "not reported or not applicable". Blanks are never converted to zero.
