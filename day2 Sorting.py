#sort_values() sorts by one or more columns. ascending=False sorts high to low.
import pandas as pd
df = pd.DataFrame({
    "name":     ["James Omondi", "Sandra Weru", "Patrick Njiru", "Grace Achieng", "Brian Kamau", "Kevin Mwangi"],
    "steps":    [9200, 10500, 8100, 11000, 7400, 10800],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5],
})

# Sort by steps, highest first
ranked = df.sort_values("steps", ascending=False).reset_index(drop=True)
ranked.index = ranked.index + 1 #1-Based ranking

print("Steps leaderboard:")
for i, row in ranked.iterrows():
    print(f"#({i}  {row['name']:<20}  {row['steps']:,} steps")

print()
ranked = df.sort_values("sleep_hr", ascending=True).reset_index(drop=False)
ranked.index = ranked.index + 1

print("Sleep hours leaderboard:")
for i, row in ranked.iterrows():
    print(f"#){i}    {row['name']:<20}  {row['sleep_hr']:,} hours")

print()
#adding a "wake_up_score column then sorting by it
df["wake_up_score"] = (df["sleep_hr"]) *(df["steps"]) / 100
ranked = df.sort_values("wake_up_score", ascending=True).reset_index(drop=False)
ranked.index = ranked.index +1

print("Wake up score leaderboard:")
for i, row in ranked.iterrows():
    print(f"-{i} {row['name']:<20} {row['wake_up_score']:,}")


