#before analysing dataframe, inspect. these four comands tells you what you are working with
import pandas as pd
data = {
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"],
    "cold_shower": [True, True, False, True, True, True, True]
}
df = pd.DataFrame(data)

#check dimensions and columns
print("shape (rows, cols):", df.shape) # prints a tuple containing the dimentions of the table ie 100,5 meaning 100 rows and 5 columns
print("\nColumns:", list(df.columns)) #outputs a clean python list containing the name of all the column headers in the table
#checking data types
print("\nData types:") #simply prints a section header label
print(df.dtypes) #list each column name alongside the specific data type it contains(int64 for integers, float64 for decimals etc)
#viewing sample data
print("\nFirst 3 rows:") #prints another section header label
print(df.head(3).to_string()) #df.head(3) extract only the first 3 rows of the dataset.
#.to_string() ensures that these three rows are rendered completely as plain text without any hidden characters or formating glitches in your termina output.