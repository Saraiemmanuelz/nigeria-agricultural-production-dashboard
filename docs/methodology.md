# Methodology

## 1. Data acquisition
The notebook downloads the FAOSTAT bulk file *Production_Crops_Livestock (Normalized)* with Python and extracts it.

## 2. Cleaning and transformation (Python, pandas)
- Filtered to Nigeria.
- Kept three elements with fixed units: Production (t), Area harvested (ha) and Yield (kg/ha).
- Pivoted the long FAOSTAT format so that each row is one item in one year, with Production, Area_Harvested and Yield as columns.
- Added `Production_per_Hectare`, `Production_Level` (median split) and `Period`.
- Checked duplicates, missing values and descriptive statistics.

## 3. Modelling (Power Query, MySQL, Power BI)
- **Crop categories:** each of the 108 items was assigned to a category in `Dim_Item.csv`, and the 16 FAO aggregate rows were flagged with `Is_Aggregate = Yes`.
- **MySQL:** `Dim_Item` was created in MySQL (`sql/Dim_Item_MySQL.sql`) and imported into Power BI to practise a database connection.
- **Star schema:** `Dim_Item` and `Dim_Year` each connect one-to-many to `Fact_Production`, with single-direction filtering.

## 4. Analysis logic
- **Aggregates are excluded** from every measure to avoid double-counting. Summing all rows gives 13.32 billion tonnes, but the real total is 6.91 billion.
- **Different period lengths** (39, 10, 10 and 5 years) mean period comparisons use average annual production, not totals.
- **Growth** is measured as a compound annual growth rate (CAGR) between 2000 and 2024, which smooths out year-to-year swings.
- **Yield and area claims** (for example "cereal growth is yield-led") compare how harvested area and output moved between 2000 and 2024. They describe what moved together and do not prove causes.

## 5. Validation
- `scripts/verify_numbers.py` recomputes every headline number from the CSV files.
- `docs/reconciliation.md` lists the dashboard values next to the recomputed values.
- A donut chart was found to be omitting three categories, which gave a wrong Roots & Tubers share (53.5%). It was corrected to 51.7%, and the recomputed values confirm it.

## 6. Limitations
- FAO figures are estimates and can be revised between releases.
- Area and yield are not reported for livestock and processed items, so yield analysis covers crops only.
- `Production_Level` is a median split over all rows, including aggregate rows. It is a simple label, not a performance standard.
- The average yield card (about 4.1K kg/ha) is a simple average across crops and years, so it is dominated by high-yield root and vegetable crops. Treat it as an overview figure.
- The notebook also contains a logistic regression that predicts `High_Production`. Because that label is derived from `Production`, and a feature (`Production_per_Hectare`) is also derived from it, the model is a learning exercise and not a validated forecasting model.
