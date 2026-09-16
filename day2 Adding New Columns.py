#Add a new column by assigning to a column name that does not exist yet. 
# The right side can be a calculation using existing columns.
import pandas as pd
df = pd.DataFrame({
    "day":          ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":        [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr":     [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "water_glasses":[7, 8, 6, 9, 8, 7, 8],
    "protocol":     ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"],
})

# Boolean column: did we hit the step goal?
df["hit_goal"]= df["steps"] >= 10000

# Numeric column: steps deficit or surplus vs 10k goal
df["steps_vs_goal"] = df["steps"] - 10000

# Category column: water rating
df["hydration"] = df["water_glasses"].apply(lambda x: "Good" if x >= 8 else "Low")

print(df[["day", "steps", "protocol", "sleep_hr", "hit_goal", "steps_vs_goal", "hydration"]].to_string())