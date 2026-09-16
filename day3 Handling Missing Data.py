#Real data has gaps. 
# Pandas represents missing values as NaN (Not a Number). 
# Use isna() to find them, dropna() to remove rows with missing values, 
# and fillna() to replace them with a default.
import pandas as pd
import numpy as np
df = pd.DataFrame({
    "name":     ["James", "Sandra", "Patrick", "Grace", "Brian"],
    "steps":    [9200, None, 8100, 11000, None],
    "sleep_hr": [7.5, 8.0, None, 7.0, 9.0],
})
print("Original with NaN:")
print(df.to_string())

print("\nRows with missing values:")
print(df[df.isna().any(axis=1)].to_string())

# Fill missing steps with the column mean
df["steps"] = df["steps"].fillna(df["steps"].mean().round(0))
df["sleep_hr"] = df["sleep_hr"].fillna(df["sleep_hr"].median().round(0))

print("\nAfter filling NaN")
print(df.to_string())