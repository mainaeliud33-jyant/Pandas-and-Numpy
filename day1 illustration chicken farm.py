import pandas as pd
data = {
    "day":        ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "eggs":       [312, 298, 320, 305, 290, 315, 308],
    "feed_kg":    [18.5, 18.0, 19.2, 18.8, 17.5, 18.6, 19.0],
    "deaths":     [0, 1, 0, 0, 2, 0, 0],
    "pen":        ["A", "A", "A", "B", "B", "B", "A"],
}
df = pd.DataFrame(data)

print("Weekly egg production:")
print(df.to_string())

print("\nShape:", df.shape)
print("\nSummary statistics")
print(df[["eggs","feed_kg","deaths","pen"]].describe().round(1).to_string())

print(f"Total eggs this week: {df['eggs'].sum()}")
print(f"Average daily eggs: {df['eggs'].mean():.1f}")
print(f"\nWorst day(eggs): {df.loc[df['eggs'].idxmin(), 'day']}")
#create a new revenue column
df["revenue_kes"] = df["eggs"] * 18

print(f"\nWeekly total revenue: kes {df['revenue_kes'].sum()}")