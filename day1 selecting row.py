#Selecting Rows
#.iloc selects rows by position (integer index). .loc selects rows by label. Both work like list slicing.
import pandas as pd
data = {
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"],
}
df =pd.DataFrame(data)
# iloc: by position
print("first row(iloc[0]):")
print(df.iloc[0])

print("\nRows 0 to 2 (iloc[o:3]):")
print(df.iloc[0:3].to_string())

print("\nLast row(iloc[-1]):")
print(df.iloc[-1].to_string())