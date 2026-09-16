import pandas as pd
df = pd.DataFrame({
    "name":     ["James", "Sandra", "Patrick", "Grace", "Brian", "Kevin", "James", "Sandra"],
    "city":     ["Nairobi", "Mombasa", "Nairobi", "Kisumu", "Nairobi", "Mombasa", "Nairobi", "Mombasa"],
    "steps":    [9200, 10500, 8100, 11000, 7400, 10800, 9800, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 7.0, 8.5],
})
# Multiple aggregations on steps by city
city_stats = df.groupby("city")["steps"].agg(["mean", "max", "min", "count"]).round(0)
print("Steps statistics by City:")
print(city_stats)