
import numpy as np

# 1. Creating arrays
a = np.array([10, 20, 30, 40, 50])

# 2. Creating special arrays
zeros = np.zeros(5)
ones = np.ones(5)
sequence = np.arange(1, 11)
random_array = np.random.randint(1, 100, size=5)

print("Array:", a)
print("Zeros:", zeros)
print("Ones:", ones)
print("Sequence:", sequence)
print("Random:", random_array)

# 3. Array properties
print("Shape:", a.shape)
print("Dimensions:", a.ndim)
print("Size:", a.size)
print("Data type:", a.dtype)

# 4. Indexing
print("First:", a[0])
print("Last:", a[-1])

# 5. Slicing
print("First three:", a[:3])
print("Every second:", a[::2])
print("Reversed:", a[::-1])

# 6. Modifying
a[0] = 100
print("Modified:", a)

# 7. Reshaping
matrix = np.arange(1, 13).reshape(3, 4)

print("Matrix:")
print(matrix)

print("Transpose:")
print(matrix.T)

# 8. Flattening
print("Flatten:", matrix.flatten())
