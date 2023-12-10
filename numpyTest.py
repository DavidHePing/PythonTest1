import numpy as np

# Create an empty 2-dimensional array (matrix) filled with zeros
empty_matrix = np.zeros((3, 3))  # Creates a 3x3 matrix filled with zeros

# Display the empty matrix
print(empty_matrix)

matrix3 = np.zeros((3,3,3))
print(matrix3)

int_array = np.arange(1, 10).reshape(3, 3)
print(int_array)
int_array = np.zeros((3, 3), dtype=int)
print(int_array)