#In VS Code, loading a CSV file is one line. pd.read_csv() returns a DataFrame immediately.
import pandas as pd
df = pd.read_csv("weekly_log.csv")
print(df.head())
print(df.shape)