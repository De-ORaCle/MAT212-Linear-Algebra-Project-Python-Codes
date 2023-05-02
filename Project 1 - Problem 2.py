'''

This code creates a function "is_symmetric" which takes a matrix as input and returns True if the matrix is symmetric,
and False otherwise. The function first checks if the matrix is square (i.e., has the same number of rows and columns).
If it's not square, then it can't be symmetric, so the function returns False. If the matrix is square, the function
checks each element against its corresponding element in the transpose of the matrix. If any of the corresponding
elements differ, then the matrix is not symmetric, so the function returns False. If all elements are equal, then the
matrix is symmetric, and the function returns True.

We then used this function to further check if the matrices in the set X of symmetric matrices satisfy the condition
A = A^T, as required in the proof.

'''


def is_symmetric(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    if rows != cols:
        return False  # A non-square matrix cannot be symmetric
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != matrix[j][i]:
                return False  # A matrix is not symmetric if a[i][j] != a[j][i]
    return True  # If we made it through the loops, the matrix is symmetric


# Define the zero matrix
n = 4  # Dimension of the matrix
zero_matrix = [[0] * n for _ in range(n)]

# Check if the zero matrix is symmetric
if is_symmetric(zero_matrix):
    print("The zero matrix is symmetric and belongs to X")
    zero_True = True
else:
    print("The zero matrix is not symmetric")


# Example usage
matrix = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
if is_symmetric(matrix):
    print("The matrix is symmetric")
    matrix_Symmetric = True
else:
    print("The matrix is not symmetric")


# Conclusion
if zero_True == True and matrix_Symmetric == True:
    print("\nThis shows to prove that the set of X ⊆ Mn(R) of symmetric matrices X = {A ∈ Mn(R⁴) : A = A^T} is a "
          "subspace.")
else:
    print("\nThere seem to be a error. Check your matrix example usage.")
