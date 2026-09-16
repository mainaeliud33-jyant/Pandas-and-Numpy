# Create a DataFrame from a dictionary and inspect it
import pandas as pd
data = {
    "name": ["Eric", "James", "Amina", "Sara"],
    "score": [85, 72, 91, 68],
    "city": ["Nairobi", "Mombasa", "Nairobi", "Kisumu"]
}

df = pd.DataFrame(data)
print(df)
print("\nShape:", df.shape)