import pandas as pd
import numpy as np
from pathlib import Path

np.random.seed(42)

N_ROWS = 5000

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"
RAW_DATA_PATH.mkdir(parents=True, exist_ok=True)

dates = pd.date_range(
start="2022-01-01",
end="2023-12-31",
freq="D"
)

df = pd.DataFrame({
"order_id": np.arange(1, N_ROWS + 1),
"order_date": np.random.choice(dates, N_ROWS),
"customer_id": np.random.randint(1, 1200, N_ROWS),
"product": np.random.choice(
["Laptop", "Phone", "Tablet", "Monitor", "Headphones"],
size=N_ROWS,
p=[0.15, 0.35, 0.2, 0.15, 0.15]
),
"quantity": np.random.choice(
[-3, -1, 0, 1, 2, 3, 4, 5],
size=N_ROWS,
p=[0.02, 0.03, 0.05, 0.35, 0.25, 0.15, 0.1, 0.05]
),
"price": np.random.choice(
[49, 99, 199, 299, 499, 999, None],
size=N_ROWS,
p=[0.2, 0.25, 0.2, 0.15, 0.1, 0.05, 0.05]
)
})

output_file = RAW_DATA_PATH / "sales_dirty_5000.csv"
df.to_csv(output_file, index=False)

print(f"Dirty sales data generated: {output_file}")
print(f"Rows: {len(df)}")