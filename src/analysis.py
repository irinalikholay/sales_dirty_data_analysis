import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "sales_dirty_5000.csv"
PROCESSED_DATA_PATH = PROJECT_ROOT / "data" / "processed" / "sales_cleaned.csv"

df = pd.read_csv(RAW_DATA_PATH)

# *** basic type fixes ***
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

# *** data cleaning rules ***
clean_df = df.copy()

clean_df = clean_df[clean_df["price"].notna()]
clean_df = clean_df[clean_df["quantity"] > 0]

# *** revenue recalculation ***
clean_df["revenue"] = clean_df["quantity"] * clean_df["price"]

# *** save cleaned data ***
clean_df.to_csv(PROCESSED_DATA_PATH, index=False)

# *** sanity checks ***
print("\n*** CLEAN DATA INFO ***")
print(clean_df.info())

print("\n*** CLEAN DATA SAMPLE ***")
print(clean_df.head())

print("\n*** REVENUE SUMMARY ***")
print(clean_df["revenue"].describe())

clean_df.to_csv(PROCESSED_DATA_PATH, index=False)