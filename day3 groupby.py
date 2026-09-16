#groupby splits a DataFrame into groups based on the values in one or more columns, 
# then lets you apply a calculation to each group.
#The result is a summary table where each row represents one group. 
# It answers questions like: "what is the average X for each category of Y?"
import pandas as pd
df = pd.DataFrame({
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"],
})
# Average steps per fasting protocol
grouped = df.groupby("protocol")["steps"].mean().round(0)
print("Average steps by protocol:")
print(grouped)

print()
#total steps per protocol
totals = df.groupby("protocol")["steps"].sum()
print("Total steps by protocol:")
print(totals)

print()
#maximum steps per protocol
most_steps = df.groupby("protocol")["steps"].max()
print("Maximum steps by protocol:")
print(most_steps)