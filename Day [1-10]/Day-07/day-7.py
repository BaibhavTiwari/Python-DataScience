# 1. NumPy arrays vs Python lists

import numpy as np 

price_list = [ 100, 101.5, 102.3, 101, 109]
price_arr = np.array(price_list)

print(price_list)
print(price_arr)
print(type(price_list), type(price_arr))

return_arr = (price_arr[1:] - price_arr[:-1]) / price_arr[:-1]
print(return_arr)

'''
# A NumPy array is a fast, fixed-type, multidimensional array used heavily in data science.
# Arrays allow vectorized operations: one operation applies to all elements without explicit Python loops.
# NumPy provides fast implementations of mean, std, min, max on arrays, useful before moving into Pandas/ML. 
'''

# 2. Basic NumPy operations

print("Mean price: ", price_arr.mean())
print("Std Price: ", price_arr.std())
print("Min price: ", price_arr.min())
print("Max price: ", price_arr.max())


