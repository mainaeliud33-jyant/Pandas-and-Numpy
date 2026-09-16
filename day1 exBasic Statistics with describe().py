#describe() gives you count, mean, std, min, max, and quartiles for every numeric column in one call.
import pandas as pd
data = {
    "day":            ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":          [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr":       [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "water":          [7, 8, 6, 9, 8, 7, 8],
    "bench_press_kg": [80, 82, 78, 85, 80, 83, 84]
}
df =pd.DataFrame(data)

print("Statistics for all Numeric columns:")
print(df.describe().to_string())

print("\nManual check:")
print(f"Mean steps: {df['steps'].mean():.0f}")
print(f"Max steps: {df['steps'].max()}")
print(f"Min steps: {df['steps'].min()}")
print(f"Total steps: {df['steps'].sum()}")