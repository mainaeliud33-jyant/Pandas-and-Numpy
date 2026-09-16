#A NumPy array is a fixed-type, fixed-size sequence of numbers stored in a single block of memory. 
# Unlike a Python list, every element must be the same type (all integers, or all floats). 
# This constraint is what makes NumPy arrays 10 to 100 times faster than lists for numerical operations.
#Creating Arrays
import numpy as np

# From a Python list
steps = np.array([9200, 10500, 8800, 11000, 7600, 9400, 10200])
print("steps array:", steps)
print("type:", type(steps))
print("dtype:", steps.dtype)
print("shape:", steps.shape)

# Zeros and ones
print("\nnp.zeros(5):", np.zeros(5))
print("np.ones(5):", np.ones(5))

# Range of numbers
print("\nnp.arange(1, 8):", np.arange(1, 8))

# Evenly spaced
print("\nnp.linspace(0,1,5):", np.linspace(0,1,5))