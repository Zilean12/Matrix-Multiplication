import numpy as np

def strassen(a, b):
    """
    Multiply two matrices using Strassen's algorithm.
    """
    n = len(a)

    # Base case: 1x1 matrices
    if n == 1:
        return a * b

    # Split matrices into quarters
    a11, a12, a21, a22 = a[:n//2, :n//2], a[:n//2, n//2:], a[n//2:, :n//2], a[n//2:, n//2:]
    b11, b12, b21, b22 = b[:n//2, :n//2], b[:n//2, n//2:], b[n//2:, :n//2], b[n//2:, n//2:]

    # Compute sub-products
    p1 = strassen(a11 + a22, b11 + b22)
    p2 = strassen(a21 + a22, b11)
    p3 = strassen(a11, b12 - b22)
    p4 = strassen(a22, b21 - b11)
    p5 = strassen(a11 + a12, b22)
    p6 = strassen(a21 - a11, b11 + b12)
    p7 = strassen(a12 - a22, b21 + b22)

    # Compute final product
    c11 = p1 + p4 - p5 + p7
    c12 = p3 + p5
    c21 = p2 + p4
    c22 = p1 - p2 + p3 + p6

    # Combine sub-products into result
    c = np.zeros((n, n))
    c[:n//2, :n//2], c[:n//2, n//2:], c[n//2:, :n//2], c[n//2:, n//2:] = c11, c12, c21, c22
    return c

# Get user input for matrices A and B
n = int(input("Enter the size of the matrices (must be a power of 2): "))
print("Enter the elements of matrix A (one row at a time):")
a = np.array([list(map(int, input().split())) for _ in range(n)])
print("Enter the elements of matrix B (one row at a time):")
b = np.array([list(map(int, input().split())) for _ in range(n)])

# Multiply matrices using Strassen's algorithm and print result
c = strassen(a, b)
print("Result of matrix multiplication using Strassen's algorithm:")
print(c)
