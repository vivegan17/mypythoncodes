import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

# Arithmetic
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# Scalar operations
print(a * 2)
print(a + 5)

# Comparisons
print(a > 20)
print(a == 30)

# Boolean filtering
print(a[a > 20])

# Aggregation
print(np.sum(a))
print(np.mean(a))
print(np.max(a))
print(np.min(a))
print(np.std(a))

# Sorting and searching
print(np.sort(a))
print(np.where(a > 20))
print(np.argmax(a))
print(np.argmin(a))
print(np.unique([1, 2, 2, 3, 3, 3]))