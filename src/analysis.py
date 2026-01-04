import pandas as pd 
import matplotlib.pyplot as plt
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "sales_dirty_5000.csv"

df = pd.read_csv(RAW_DATA_PATH)

print("\n*** BASIC INFO ***")
print(df.info())

print("\n*** FIRST ROWS ***")
print(df.head())

print("\n*** DESCRIPTIVE STATISTICS ***")
print(df.describe())

print("\n*** MISSING VALUES ***")
print(df.isna().sum())

df["order_date"] = pd.to_datetime(df["order_date"], errors ="coerce")

df["revenue"] = df["quantity"] * df["price"]

print("\n*** REVENUE RANGE ***")
print

