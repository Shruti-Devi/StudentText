import pandas as pd
from pathlib import Path

csv_path = Path(__file__).resolve().parent / "data" / "full_dataset" / "goemotions_1.csv"

df = pd.read_csv(csv_path)

print(df.head())
print(df.columns)
print(df.shape)