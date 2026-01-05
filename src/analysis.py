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

df = pd.read_csv(PROCESSED_DATA_PATH)

plt.figure(figsize=(8, 5))
plt.hist(df["revenue"], bins=30)
plt.title("Revenue Distribution")
plt.xlabel("Revenue")
plt.ylabel("Number of Orders")
plt.savefig("visuals/revenue_distribution.png")
plt.close()

revenue_by_product = (
    df.groupby("product")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\n*** REVENUE BY PRODUCT ***")
print(revenue_by_product)


average_order_value = df["revenue"].mean()

print("\n*** AVERAGE ORDER VALUE ***")
print(round(average_order_value, 2))


orders_count = df.shape[0]

print("\n*** TOTAL NUMBER OF ORDERS ***")
print(orders_count)


plt.figure(figsize=(8, 5))
revenue_by_product.plot(kind="bar")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visuals/revenue_by_product.png")
plt.close()