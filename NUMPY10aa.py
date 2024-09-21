import numpy as np


array1 = np.array([8, 10, 12])
array2 = np.array([14, 16, 18])
print("array1=",array1,"\narray2=",array2)

# 1. Sum of two arrays
sum_of_arrays = array1 + array2
print("1. Sum of two arrays:\n", sum_of_arrays)
print('*'*50)

# 2. Sum of all array elements
sum_of_elements_array1 = np.sum(array1)
sum_of_elements_array2 = np.sum(array2)
print("\n2. Sum of all elements in array1:", sum_of_elements_array1)
print("   Sum of all elements in array2:", sum_of_elements_array2)
print("\n2. Sum of all elements :", sum_of_elements_array1+sum_of_elements_array2)

print('*'*50)

# 3. Square root of two arrays
sqrt_of_array1 = np.sqrt(array1)
sqrt_of_array2 = np.sqrt(array2)
print("\n3. Square root of array1:\n", sqrt_of_array1)
print("\n   Square root of array2:\n", sqrt_of_array2)
print('*'*50)

# 4. Sum of each column and each row of two arrays
sum_of_columns_array1 = np.sum(array1)
sum_of_rows_array1 = np.sum(array1)
sum_of_columns_array2 = np.sum(array2)
sum_of_rows_array2 = np.sum(array2)
print("\n4. Sum of columns of array1:", sum_of_columns_array1)
print("   Sum of rows of array1:", sum_of_rows_array1)
print("   Sum of columns of array2:", sum_of_columns_array2)
print("   Sum of rows of array2:", sum_of_rows_array2)
print('*'*50)

# 5. Transpose of two arrays
transpose_array1 = array1.reshape(-1, 1)
transpose_array2 = array2.reshape(-1, 1)
print("\n5. Transpose of array1:\n", transpose_array1)
print("\n   Transpose of array2:\n", transpose_array2)
print('*'*50)
