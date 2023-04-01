def strassen_mult(matrix1, matrix2):
    # Check if matrices are single-element matrices
    if len(matrix1) == 1 and len(matrix2) == 1:
        return [[matrix1[0][0] * matrix2[0][0]]]
    
    # Split matrices into quadrants
    a, b, c, d = split(matrix1)
    e, f, g, h = split(matrix2)
    
    # Recursively calculate the seven products
    p1 = strassen_mult(a, subtract_matrices(f, h))
    p2 = strassen_mult(add_matrices(a, b), h)
    p3 = strassen_mult(add_matrices(c, d), e)
    p4 = strassen_mult(d, subtract_matrices(g, e))
    p5 = strassen_mult(add_matrices(a, d), add_matrices(e, h))
    p6 = strassen_mult(subtract_matrices(b, d), add_matrices(g, h))
    p7 = strassen_mult(subtract_matrices(a, c), add_matrices(e, f))
    
    # Calculate the quadrants of the result matrix
    top_left = add_matrices(subtract_matrices(add_matrices(p5, p4), p2), p6)
    top_right = add_matrices(p1, p2)
    bottom_left = add_matrices(p3, p4)
    bottom_right = subtract_matrices(subtract_matrices(add_matrices(p5, p1), p3), p7)
    
    # Combine the quadrants into the result matrix
    result = combine(top_left, top_right, bottom_left, bottom_right)
    
    return result

def split(matrix):
    # Split matrix into quadrants
    n = len(matrix)
    m = n // 2
    a = [row[:m] for row in matrix[:m]]
    b = [row[m:] for row in matrix[:m]]
    c = [row[:m] for row in matrix[m:]]
    d = [row[m:] for row in matrix[m:]]
    return a, b, c, d

def combine(top_left, top_right, bottom_left, bottom_right):
    # Combine quadrants into matrix
    result = []
    n = len(top_left)
    for i in range(n):
        result.append(top_left[i] + top_right[i])
    for i in range(n):
        result.append(bottom_left[i] + bottom_right[i])
    return result

def add_matrices(matrix1, matrix2):
    # Add two matrices
    n = len(matrix1)
    result = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result

def subtract_matrices(matrix1, matrix2):
    # Subtract two matrices
    n = len(matrix1)
    result = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = matrix1[i][j] - matrix2[i][j]
    return result

# Get user input for matrix sizes and elements
n = int(input("Enter the size of the matrices: "))
print("Enter the elements of the first matrix:")
matrix1 = [[int(input()) for j in range(n)] for i in range(n)]
print("Enter the elements of the second matrix:")
matrix2 = [[int(input()) for j in range(n)] for i in range(n)]

# Multiply matrices using Strassen's method
result
