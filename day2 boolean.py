#Boolean filtering selects rows where a condition is True
#ou write a condition that compares a column to a value.
#Pandas evaluates it for every row and returns only the matching ones.
#The result is a new DataFrame, not a modification of the original.
import pandas as pd
df = pd.DataFrame({
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"],
})
# Days where step goal was hit
goal_days = df[df["steps"] >= 10000]
print("Days with 10k+ steps:")
print(goal_days[["day", "steps", "protocol"]].to_string())

print()
# Days with less than 7.5 hours sleep
low_sleep = df[df["sleep_hr"] <7.5]
print("Days with under 7.5hrs sleep:")
print(low_sleep[["day", "sleep_hr"]].to_string())

print()
#Days with OMAD
OMAD = df[df["protocol"] == "OMAD"]
print("Days on OMAD:")
print(OMAD[["day", "protocol"]].to_string())