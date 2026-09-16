#Slicing NumPy arrays uses the same syntax as Python lists. 
# The difference is that slices of NumPy arrays are views, not copies. 
# Changing a slice changes the original.
import numpy as np

steps = np.array([9200, 10500, 8800, 11000, 7600, 9400, 10200])
days = np.array(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
# :is used for slicing
print("Print first 3 days:", steps[:3])
print("Last 2 days:", steps[-2:])
print("Weekdays (Mon-Fri):", steps[:5])
print("Weekends (Sat & Sun):", steps[5:])

print()
# Best week start: first day above 10k
first_10k = np.argmax(steps >= 10000) #index of first true
print(f"First 10k+ day: {days[first_10k]} with {steps[first_10k]:,} steps")

# sort and show progression
sorted_steps = np.sort(steps)
print(f"Steps sorted from low to high:, {sorted_steps}")

sorted_indices = np.argsort(steps)
sorted_days = days[sorted_indices]
sorted_steps = steps[sorted_indices]
paired_output = [f"\n{day}: {step}" for day, step in zip(sorted_days, sorted_steps)]
print("\nSteps sorted from low to high: [",", ".join(paired_output),"]")