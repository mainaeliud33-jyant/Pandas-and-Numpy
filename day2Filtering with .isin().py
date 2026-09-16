#.isin() checks if a column's value is in a list. 
# It is cleaner than chaining multiple | conditions when you have several allowed values.
import pandas as pd
df = pd.DataFrame({
    "name":     ["James Omondi", "Sandra Weru", "Patrick Njiru", "Grace Achieng", "Brian Kamau", "Kevin Mwangi"],
    "city":     ["Nairobi", "Mombasa", "Nairobi", "Kisumu", "Nairobi", "Mombasa"],
    "steps":    [9200, 10500, 8100, 11000, 7400, 10800],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD"],
})
# Members from Nairobi or Mombasa
nrb_mba = df[df["city"].isin(["Nairobi", "Mombasa"])]
print("Niarobi and Mombasa members:")
print(nrb_mba[["name", "city", "steps", "protocol"]].to_string())

print()
mba_ksm = df[df["city"].isin(["Mombasa", "Kisumu"])]
print("Mombasa and Kisumu Members:")
print(mba_ksm[["name", "city", "steps"]].to_string())