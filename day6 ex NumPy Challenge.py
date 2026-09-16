# Create an array of 10 random integers between 1 and 100
# Print the mean, max, min, and standard deviation
import numpy as np
arr = np.array([23, 67, 45, 89, 12, 56, 78, 34, 90, 41])
print(f" Mean:    {arr.mean():.2f}")
print(f" Max:     {arr.max()}")
print(f" Min:     {arr.min()}")
print(f" std dev: {arr.std():.2f}")
