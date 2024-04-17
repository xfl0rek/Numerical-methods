import numpy as np


def calculate_determinant(matrix):
    determinant = np.linalg.det(matrix)
    return determinant


def is_diagonally_dominant(matrix):
    n = matrix.shape[0]
    for i in range(n):
        row_sum = np.sum(np.abs(matrix[i])) - np.abs(matrix[i][i])
        if np.abs(matrix[i][i]) <= row_sum:
            return False
    return True


def gauss_seidel(A, b, x0=None, max_iter=None, epsilon=None):
    global k
    if calculate_determinant(A) == 0:
        print("The system is either indeterminate or inconsistent.")
        return None
    if not is_diagonally_dominant(A):
        print("The matrix is not diagonally dominant.")
        return None
    n = len(b)
    if x0 is None:
        x0 = np.zeros(n)
    if max_iter is None and epsilon is None:
        raise ValueError("You must provide either max_iter or epsilon.")
    if max_iter is None:
        max_iter = 1000
    if epsilon is None:
        epsilon = 1e-10

    x = x0.copy()
    for k in range(max_iter):
        x_prev = x.copy()
        for i in range(n):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i + 1:], x_prev[i + 1:])) / A[i, i]
        if np.linalg.norm(x - x_prev) < epsilon:
            break
    print(f"Solution found after {k + 1} iterations.")
    return x
