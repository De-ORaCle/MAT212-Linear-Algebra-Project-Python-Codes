'''

The code defines and tests whether the set of skew-symmetric matrices C = {B ∈ Mn(R) : B = -B^T} is a subspace of Mn(R), where Mn(R) is the set of n x n matrices with real entries.

The code first checks for non-emptiness by verifying whether the zero matrix belongs to C. If the zero matrix is skew-symmetric, the code appends it to C and sets a boolean variable existentZ to True. If the zero matrix is not skew-symmetric, the code sets existentZ to False and prints a message indicating that C is empty.

The code then checks whether C is closed under vector addition and scalar multiplication. To do so, the code loops over all the entries of the n x n matrices B1 and B2 and creates two skew-symmetric matrices by setting certain entries to 1 and -1. It then checks if B1 and B2 are skew-symmetric matrices by verifying whether they satisfy the condition B = -B^T. If B1 and B2 are skew-symmetric, the code checks if B1 + B2 and alphaB1 are also skew-symmetric for any scalar alpha in R, by iterating over a range of alpha values. If both conditions are satisfied, the matrices B1, B2, B1+B2, and alphaB1 are appended to C.

Finally, the code checks if C is a subspace of Mn(R) by verifying whether it satisfies two conditions: non-emptiness and closure under vector addition and scalar multiplication. If both conditions are satisfied, the code sets a boolean variable closedAM to True. If either condition is not satisfied, closedAM is set to False. If both existentZ and closedAM are True, the code prints a message indicating that C is a subspace of Mn(R). If either existentZ or closedAM is False, the code prints a message indicating that C is not a subspace of Mn(R).

'''


import numpy as np

# Define Mn(R) as a 2-dimensional array of shape (n, n)
n = 3
MnR = np.zeros((n, n))

# Define C as the set of skew-symmetric matrices
C = []

# Condition 1: Non-emptiness
# Check if the zero matrix is skew-symmetric and belongs to C
zero_matrix = np.zeros((n, n))
if np.array_equal(zero_matrix, -zero_matrix.T):
    C.append(zero_matrix)
    print("C is non-empty")
    existentZ = True
else:
    print("C is empty")

# Condition 2: Closure under vector addition and scalar multiplication
# Check if the vector addition and scalar multiplication of two skew-symmetric matrices is also skew-symmetric
for i in range(n):
    for j in range(n):
        # Create two skew-symmetric matrices B1 and B2 in C
        B1 = np.zeros((n, n))
        B2 = np.zeros((n, n))
        B1[i][j] = 1
        B1[j][i] = -1
        B2[i][j] = -2
        B2[j][i] = 2

        # Check if B1 and B2 are skew-symmetric
        if np.array_equal(B1, -B1.T) and np.array_equal(B2, -B2.T):
            # Check if B1 + B2 and alpha*B1 are also skew-symmetric for any scalar alpha in R
            for alpha in np.arange(-10, 10, 0.5):  # Check for a range of alpha values
                if np.array_equal((B1 + B2), -(B1 + B2).T) and np.array_equal((alpha * B1), -(alpha * B1).T):
                    C.append(B1)
                    C.append(B2)
                    C.append(B1 + B2)
                    C.append(alpha * B1)
                    print("C is closed under vector addition and scalar multiplication")
                    closedAM = True
        else:
            print("C is closed under vector addition and scalar multiplication")

if existentZ == True and closedAM == True:
    print("C is a subspace of Mn(R)")
else:
    print("C is not a subspace of Mn(R)")
