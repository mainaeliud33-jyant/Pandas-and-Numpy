#Selecting Columns
#A single column returns a Series. Multiple columns return a DataFrame.
import pandas as pd
data = {
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"],
}
df = pd.DataFrame(data) #for creating DataFrame

# Single column (returns a Series)
print("Steps column:")
print(df["steps"])
# multiple columns
print("\nSteps and Protocol:")
print(df[["steps", "protocol"]].to_string())