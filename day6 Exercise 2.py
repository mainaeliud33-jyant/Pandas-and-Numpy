# Filter to show only students from Nairobi with score above 80
import pandas as pd
data = {"name": ["Eric","James","Amina","Sara"], "score": [85,72,91,68], "city": ["Nairobi","Mombasa","Nairobi","Kisumu"]}
df = pd.DataFrame(data)
results = df[(df['city'] == 'Nairobi') & (df['score'] > 80)]
print(results)