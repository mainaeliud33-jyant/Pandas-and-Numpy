#NumPy and pandas work together. 
# A pandas Series is built on a NumPy array. 
# You can pull a column out of a DataFrame as a NumPy array using .values or .to_numpy(). 
# Many pandas methods internally use NumPy for speed.
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "bench_press_kg":[60, 80, 50,70, 90, 40, 100]
})
# Pull a column as a NumPy array
bench_press_kg = np.array([60, 80, 50,70, 90, 40, 100])
steps = np.array([9200, 10500, 8800, 11000, 7600, 9400, 10200])
steps_arr = df["steps"].to_numpy()
bench_arr = df["bench_press_kg"].to_numpy()
correlation_matrix = np.corrcoef(steps, bench_press_kg)
print("NumPy array from Pandas column:", steps_arr)
print("Type:", type(steps_arr))

# Use NumPy on it
print(f"\nMean:,      {np.mean(steps_arr):,.0f}")
print(f"standard dev: {np.std(steps_arr):,.0f}")
print(f"Mean:,        {np.mean(bench_arr):,.0f}")



# Add a normalized column back to the DataFrame
# Normalize to 0-1 range (min-max scaling)
df["normal_steps"] = (df["steps"] - df["steps"].min()) / (df["steps"].max() - df["steps"].min())
df["normal_steps"] = df["normal_steps"].round(3)
print("\nWith normalized steps:")
print(df[["day", "steps", "normal_steps"]].to_string())
print(f"\nCorrelation matrix:", correlation_matrix)