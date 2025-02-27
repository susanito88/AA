import random
import time
import matplotlib.pyplot as plt
import pandas as pd
from prettytable import PrettyTable

# Function to count iterations
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

# QuickSort Implementation
def quicksort(arr, counter):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if counter.increment() or x < pivot]
    middle = [x for x in arr if counter.increment() or x == pivot]
    right = [x for x in arr if counter.increment() or x > pivot]
    return quicksort(left, counter) + middle + quicksort(right, counter)

# MergeSort Implementation
def merge_sort(arr, counter):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], counter)
    right = merge_sort(arr[mid:], counter)
    return merge(left, right, counter)

def merge(left, right, counter):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        counter.increment()
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# HeapSort Implementation
def heapify(arr, n, i, counter):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and counter.increment() or (left < n and arr[left] > arr[largest]):
        largest = left

    if right < n and counter.increment() or (right < n and arr[right] > arr[largest]):
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, counter)

def heap_sort(arr, counter):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, counter)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, counter)
    return arr

# InsertionSort Implementation
def insertion_sort(arr, counter):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and counter.increment() or (j >= 0 and arr[j] > key):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Generate different types of input data
def generate_test_cases(size):
    random_array = [random.randint(-1000, 1000) for _ in range(size)]
    sorted_array = sorted(random_array)
    reversed_array = sorted_array[::-1]
    half_sorted = sorted_array[:size//2] + random.sample(sorted_array[size//2:], size//2)
    negative_numbers = [random.randint(-1000, -1) for _ in range(size)]
    return {
        "Random": random_array,
        "Sorted": sorted_array,
        "Reversed": reversed_array,
        "Half-Sorted": half_sorted,
        "Negative Numbers": negative_numbers
    }

# Running tests and collecting results
sizes = [100, 50, 1000]  # Different input sizes for analysis
results = []

table = PrettyTable()
table.field_names = ["Size", "Case", "Algorithm", "Iterations"]

for size in sizes:
    test_cases = generate_test_cases(size)
    for case_name, case_data in test_cases.items():
        for sort_name, sort_func in [("QuickSort", quicksort), ("MergeSort", merge_sort), ("HeapSort", heap_sort), ("InsertionSort", insertion_sort)]:
            counter = Counter()
            sorted_result = sort_func(case_data.copy(), counter)
            results.append({
                "Size": size,
                "Case": case_name,
                "Algorithm": sort_name,
                "Iterations": counter.count
            })
            table.add_row([size, case_name, sort_name, counter.count])

# Print the table in console
print(table)

# Convert results into DataFrame
df_results = pd.DataFrame(results)

# Plot separate graphs for each input case
for case_name in df_results["Case"].unique():
    plt.figure(figsize=(12, 6))
    subset = df_results[df_results["Case"] == case_name]
    for algo in subset["Algorithm"].unique():
        algo_subset = subset[subset["Algorithm"] == algo]
        plt.plot(algo_subset["Size"], algo_subset["Iterations"], marker='o', label=algo)
    plt.xlabel("Array Size")
    plt.ylabel("Number of Iterations")
    plt.title(f"Sorting Algorithm Performance for {case_name} Array")
    plt.legend()
    plt.grid()
    plt.show()
