'''

The code defines three functions and uses them to test whether a given set of matrices form a subspace of the space of n x n matrices with real entries (Mn(R)). The set being tested is defined as the set of all upper-triangular n x n matrices, denoted by B.

The function is_upper_triangular checks if a given matrix A is an upper-triangular matrix. An upper-triangular matrix is a square matrix in which all entries below the main diagonal are zero. The function returns True if the matrix is upper-triangular and False otherwise.

The function is_in_B checks if a given matrix A belongs to the set B of upper-triangular matrices. It does this by calling the is_upper_triangular function and returning its result.

The function is_subspace_B checks if a given set of matrices A, C, and their linear combination alpha*A + C belong to B. It does this by calling the is_in_B function for each of these matrices and returning True if all three matrices belong to B and False otherwise.

The code then tests whether the set B is non-empty and closed under vector addition and scalar multiplication, which are two of the conditions required for a set to be a subspace of a given vector space. It generates two upper-triangular matrices A and C of size n x n and a scalar alpha, and checks if their linear combination alpha*A + C also belongs to B using the is_subspace_B function.

Finally, based on the results of the tests, the code outputs whether the set B is a subspace of Mn(R) or not.

'''


import numpy as np

def is_upper_triangular(A):
    m, n = A.shape
    for i in range(1, m):
        for j in range(i):
            if A[i,j] != 0:
                return False
    return True

def is_in_B(A):
    return is_upper_triangular(A)

def is_subspace_B(A, C, alpha):
    return is_in_B(A) and is_in_B(C) and is_in_B(A + alpha*C)

# Testing the subspace B
n = 4
B = np.zeros((n,n))

# Testing non-emptiness
if is_in_B(B):
    print("B is not empty")
    presentZ = True
else:
    print("B is empty")

# Testing closure under vector addition and scalar multiplication
A = np.triu(np.random.rand(n,n))
C = np.triu(np.random.rand(n,n))

alpha = 2
if is_subspace_B(A, C, alpha):
    print("B is closed under vector addition and scalar multiplication")
    closedV = True
else:
    print("B is not closed under vector addition and scalar multiplication")


if presentZ == True and closedV == True:
    print("C is a subspace of Mn(R)")
else:
    print("C is not a subspace of Mn(R)")
