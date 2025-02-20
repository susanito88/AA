import time
import matplotlib.pyplot as plt
import math
from decimal import Decimal, getcontext

# Set precision for Decimal calculations (increase if necessary)
getcontext().prec = 500  # 500-digit precision should be enough

# Space Optimized Fibonacci (Iterative with Constant Space)
def fibonacci_space_optimized(n):
    if n <= 1:
        return n
    prev1, prev2 = 1, 0
    for _ in range(2, n + 1):
        prev1, prev2 = prev1 + prev2, prev1
    return prev1

# Recursive Fibonacci function (only for small values)
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Dynamic Programming Fibonacci (Bottom-Up Approach)
def fibonacci_dp(n):
    if n <= 1:
        return n
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]

# Matrix Exponentiation Fibonacci Method
def matrix_power_fibonacci(n):
    def matrix_mult(A, B):
        return [[A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
                [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]]

    def matrix_power(matrix, exp):
        result = [[1, 0], [0, 1]]  # Identity matrix
        base = matrix
        while exp:
            if exp % 2:
                result = matrix_mult(result, base)
            base = matrix_mult(base, base)
            exp //= 2
        return result

    if n == 0:
        return 0
    base_matrix = [[0, 1], [1, 1]]
    result_matrix = matrix_power(base_matrix, n - 1)
    return result_matrix[1][1]  # Fibonacci(n)

# Binet's Formula Fibonacci using Decimal for high precision
def fibonacci_binet(n):
    sqrt5 = Decimal(5).sqrt()
    phi = (Decimal(1) + sqrt5) / Decimal(2)
    psi = (Decimal(1) - sqrt5) / Decimal(2)
    return int((phi**n - psi**n) / sqrt5)  # Convert back to integer safely

# Fast Doubling Fibonacci Method
def fibonacci_fast_doubling(n):
    def fib_doubling(k):
        if k == 0:
            return (0, 1)
        else:
            a, b = fib_doubling(k // 2)
            c = a * ((b << 1) - a)
            d = a * a + b * b
            if k % 2 == 0:
                return (c, d)
            else:
                return (d, c + d)

    return fib_doubling(n)[0]

# Define datasets for different methods
dataset_recursive = list(range(36))  # Only up to 35 for recursion
dataset_large = [
    1000,  5041,  9083, 13125, 17166,
    21208, 25250, 29291, 33333, 37375,
    41416, 45458, 49500, 53541, 57583,
    61625, 65666, 69708, 73750, 77791,
    81833, 85875, 89916, 93958, 100000
]

# Lists to store execution times
times_recursive = []
times_dp = []
times_matrix = []
times_binet = []
times_space_optimized = []
times_fast_doubling = []

# Measure time for the Recursive approach (only up to 35 terms)
for n in dataset_recursive:
    start_time = time.time()
    fibonacci_recursive(n)
    end_time = time.time()
    times_recursive.append(end_time - start_time)

# Measure time for the DP approach
for n in dataset_large:
    start_time = time.time()
    fibonacci_dp(n)
    end_time = time.time()
    times_dp.append(end_time - start_time)

# Measure time for Matrix Exponentiation approach
for n in dataset_large:
    start_time = time.time()
    matrix_power_fibonacci(n)
    end_time = time.time()
    times_matrix.append(end_time - start_time)

# Measure time for Binet's Formula approach (with Decimal)
for n in dataset_large:
    start_time = time.time()
    fibonacci_binet(n)
    end_time = time.time()
    times_binet.append(end_time - start_time)

# Measure time for Space Optimized approach
for n in dataset_large:
    start_time = time.time()
    fibonacci_space_optimized(n)
    end_time = time.time()
    times_space_optimized.append(end_time - start_time)

# Measure time for Fast Doubling approach
for n in dataset_large:
    start_time = time.time()
    fibonacci_fast_doubling(n)
    end_time = time.time()
    times_fast_doubling.append(end_time - start_time)

# Plotting the results
plt.figure(figsize=(14, 18))

# Recursive Time Plot
plt.subplot(6, 1, 1)
plt.plot(dataset_recursive, times_recursive, marker='o', linestyle='-', color='b')
plt.title('Time taken to compute Fibonacci (Recursive)')
plt.xlabel('Fibonacci Term (n)')
plt.ylabel('Time taken (seconds)')
plt.grid(True)

# Dynamic Programming Time Plot
plt.subplot(6, 1, 2)
plt.plot(dataset_large, times_dp, marker='o', linestyle='-', color='r')
plt.title('Time taken to compute Fibonacci (Dynamic Programming)')
plt.xlabel('Fibonacci Term (n)')
plt.ylabel('Time taken (seconds)')
plt.grid(True)

# Matrix Exponentiation Time Plot
plt.subplot(6, 1, 3)
plt.plot(dataset_large, times_matrix, marker='o', linestyle='-', color='g')
plt.title('Time taken to compute Fibonacci (Matrix Exponentiation)')
plt.xlabel('Fibonacci Term (n)')
plt.ylabel('Time taken (seconds)')
plt.grid(True)

# Binet's Formula Time Plot (Fixed for Large `n`)
plt.subplot(6, 1, 4)
plt.plot(dataset_large, times_binet, marker='o', linestyle='-', color='purple')
plt.title('Time taken to compute Fibonacci (Binet’s Formula)')
plt.xlabel('Fibonacci Term (n)')
plt.ylabel('Time taken (seconds)')
plt.grid(True)

# Space Optimized Time Plot
plt.subplot(6, 1, 5)
plt.plot(dataset_large, times_space_optimized, marker='o', linestyle='-', color='orange')
plt.title('Time taken to compute Fibonacci (Space Optimized)')
plt.xlabel('Fibonacci Term (n)')
plt.ylabel('Time taken (seconds)')
plt.grid(True)

# Fast Doubling Time Plot
plt.subplot(6, 1, 6)
plt.plot(dataset_large, times_fast_doubling, marker='o', linestyle='-', color='cyan')
plt.title('Time taken to compute Fibonacci (Fast Doubling)')
plt.xlabel('Fibonacci Term (n)')
plt.ylabel('Time taken (seconds)')
plt.grid(True)

plt.tight_layout()  # Adjust layout for better visibility
plt.show()
