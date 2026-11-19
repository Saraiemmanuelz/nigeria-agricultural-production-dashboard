"""
Recompute the headline numbers shown on the four dashboard pages directly from
the CSV files, so they can be compared with the Power BI measures.

Run from the repository root:   python scripts/verify_numbers.py
Requires: pandas
"""
import pandas as pd

fact = pd.read_csv("data/powerbi/Fact_Production.csv")
item = pd.read_csv("data/powerbi/Dim_Item.csv")
df = fact.merge(item, on="Item_ID")
crops = df[df["Is_Aggregate"] == "No"]          # FAO aggregate rows excluded

total = crops["Production"].sum()
by_year = crops.groupby("Year")["Production"].sum()
by_item = crops.groupby("Item")["Production"].sum().sort_values(ascending=False)
by_cat = crops.groupby("Crop_Category")["Production"].sum()
staple_cats = ["Cereals", "Roots & Tubers"]
staple = crops[crops["Crop_Category"].isin(staple_cats)]["Production"].sum()
n_years = crops["Year"].nunique()

def avg_annual(period):
    sub = crops[crops["Period"] == period]
    return sub["Production"].sum() / sub["Year"].nunique()

def area(cat, year):
    return crops[(crops["Crop_Category"] == cat) & (crops["Year"] == year)]["Area_Harvested"].sum()

checks = {
    "Total Production (t)": total,
    "Crop Count": crops["Item_ID"].nunique(),
    "Avg Yield kg per ha (simple mean)": crops["Yield"].mean(),
    "Peak Year": int(by_year.idxmax()),
    "Production CAGR 2000 to 2024": (by_year[2024] / by_year[2000]) ** (1 / 24) - 1,
    "Staple Share %": staple / total,
    "Staple Production (t)": staple,
    "Roots & Tubers Share %": by_cat["Roots & Tubers"] / total,
    "Cereals Share %": by_cat["Cereals"] / total,
    "Cassava Production (t)": by_item["Cassava, fresh"],
    "Cassava Share %": by_item["Cassava, fresh"] / total,
    "Yams Share %": by_item["Yams"] / total,
    "Top 10 crops share %": by_item.head(10).sum() / total,
    "Avg Annual Output (t)": total / n_years,
    "High Production Records": int((crops["Production_Level"] == "High Production").sum()),
    "Production 1961 (t)": by_year[1961],
    "Production 2024 (t)": by_year[2024],
    "Avg annual 1961-1999 (t)": avg_annual("1961-1999"),
    "Avg annual 2000-2009 (t)": avg_annual("2000-2009"),
    "Avg annual 2010-2019 (t)": avg_annual("2010-2019"),
    "Avg annual 2020-2024 (t)": avg_annual("2020-2024"),
    "Cereal Avg Yield (kg/ha)": crops[crops["Crop_Category"] == "Cereals"]["Yield"].mean(),
    "Roots & Tubers Avg Yield (kg/ha)": crops[crops["Crop_Category"] == "Roots & Tubers"]["Yield"].mean(),
    "Roots & Tubers area 2000 (ha)": area("Roots & Tubers", 2000),
    "Roots & Tubers area 2024 (ha)": area("Roots & Tubers", 2024),
    "Cereal area 2000 (ha)": area("Cereals", 2000),
    "Cereal area 2024 (ha)": area("Cereals", 2024),
    "Total incl. FAO aggregates (t), NOT used": df["Production"].sum(),
}

def cat_prod(cat, year):
    return crops[(crops["Crop_Category"] == cat) & (crops["Year"] == year)]["Production"].sum()

def item_yield(name, year):
    return crops[(crops["Item"] == name) & (crops["Year"] == year)]["Yield"].sum()

checks.update({
    "Cereal production growth 2000 to 2024 (%)": (cat_prod("Cereals", 2024) / cat_prod("Cereals", 2000) - 1) * 100,
    "Roots & Tubers production multiple 2024 / 2000 (x)": cat_prod("Roots & Tubers", 2024) / cat_prod("Roots & Tubers", 2000),
    "Roots & Tubers area multiple 2024 / 2000 (x)": area("Roots & Tubers", 2024) / area("Roots & Tubers", 2000),
    "Cassava yield 2000 (kg/ha)": item_yield("Cassava, fresh", 2000),
    "Cassava yield 2024 (kg/ha)": item_yield("Cassava, fresh", 2024),
    "Maize yield 1961 (kg/ha)": item_yield("Maize (corn)", 1961),
    "Maize yield 2024 (kg/ha)": item_yield("Maize (corn)", 2024),
    "Cassava production 1961 (t)": crops[(crops["Item"] == "Cassava, fresh") & (crops["Year"] == 1961)]["Production"].sum(),
    "Cassava production 2024 (t)": crops[(crops["Item"] == "Cassava, fresh") & (crops["Year"] == 2024)]["Production"].sum(),
})

for name, value in checks.items():
    print(f"{name:45s} {value:>22,.4f}" if isinstance(value, float) else f"{name:45s} {value:>22,}")
