# ----------------------------
# -- Numpy => Create Arrays --
# ----------------------------

import numpy as np 

# print(dir(np))

my_list = [1 , 2, 3 ,4,5]

my_array = np.array(my_list)

print(my_list)

print(my_array)

print("# " * 50)

# To Accessing elmant
print(my_list[1])

print(my_array[1])

print("#" * 50)

a = np.array(10) #Zero dimansional
b = np.array([10, 20]) #1 dimansional
c = np.array( [ [1, 2], [3, 4] ] ) #2 dimansional
d = np.array( [ [ [5, 6], [7, 9] ], [ [1, 3], [4, 8] ] ] )  # 3 dimansional

print(d[1][1][-1])
print(d[1, 1, 1])
print(d[1, 1, -1])

print("#" * 50)

# Number Of Dimensions

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

print("#" * 50)

# Custom Dimensions

my_custom_array = np.array([1, 2, 3], ndmin=3)
print(my_custom_array)
print(my_custom_array.ndim)

print(my_custom_array[0, 0, 0])