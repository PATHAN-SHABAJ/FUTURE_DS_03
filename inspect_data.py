import pandas as pd
from pathlib import Path

# Load dataset
file_path = Path("data/bank-full.csv")
df = pd.read_csv(file_path, sep=";")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("\nColumn Names:",df.columns.tolist())
print("\nFirst 5 Records:",df.head())
print("\nMissing Values:",df.isnull().sum())
print("\nDuplicate Rows:", df.duplicated().sum())
print("\nSubscription Outcome:",df["y"].value_counts())
print("\nSubscription Percentage:", (df["y"].value_counts(normalize=True) * 100).round(2))
