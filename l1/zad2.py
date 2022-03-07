import numpy as np


def symdiff(m1: np.ndarray, m2: np.ndarray):
    if m1.shape != m2.shape:
        raise ValueError(
            f"matrices are supposed to be of the same shape (got {m1.shape} and {m2.shape})"
        )
    i, j = m1.shape
    result = 0
    for row in range(i):
        for col in range(j):
            result += np.abs(m1[row, col] - m2[row, col])
    return result


matrix1 = np.array([[1, 2, 3], [4, 5, 6]])
matrix2 = np.array([[0, 2, 3], [4, 5, 7]])

# as we increase the offsets between fields, the value will
# also increase. it'll only == 0 for identical matrices
# this could possibly be done by using np.diff()?
print(symdiff(matrix1, matrix2))
