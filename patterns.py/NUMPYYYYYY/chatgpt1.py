
import numpy as np

# 1. Find duplicates
def find_duplicates(arr):
    values, counts = np.unique(arr, return_counts=True)
    return values[counts > 1]


# 2. Prefix sum
def prefix_sum(arr):
    return np.cumsum(arr)


# 3. Find elements greater than target
def greater_than(arr, target):
    return arr[arr > target]


# 4. Find the index of a target
def search(arr, target):
    positions = np.where(arr == target)[0]

    if len(positions) == 0:
        return -1

    return positions[0]


# 5. Sort an array
def sort_array(arr):
    return np.sort(arr)


# 6. Matrix row and column sums
def matrix_analysis(matrix):
    return {
        "row_sums": np.sum(matrix, axis=1),
        "column_sums": np.sum(matrix, axis=0),
        "transpose": matrix.T
    }


# 7. Sliding window maximum
def sliding_window_max(arr, k):
    windows = np.lib.stride_tricks.sliding_window_view(arr, k)
    return np.max(windows, axis=1)


# Test everything
numbers = np.array([2, 5, 3, 5, 8, 2, 10])

print("Duplicates:", find_duplicates(numbers))
print("Prefix sums:", prefix_sum(numbers))
print("Greater than 5:", greater_than(numbers, 5))
print("Search 8:", search(numbers, 8))
print("Sorted:", sort_array(numbers))

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Matrix analysis:", matrix_analysis(matrix))

print("Sliding window maximum:",
      sliding_window_max(numbers, 3))
