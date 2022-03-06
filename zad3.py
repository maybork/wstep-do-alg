import numpy as np


def gauss_jordan(matrix: np.ndarray):
    if len(matrix.shape) != 2:
        raise ValueError(f"expected 2d array, got {len(matrix.shape)}")
    if matrix.shape[1] != matrix.shape[0] + 1:
        raise ValueError(
            f"wrong matrix size - expected NxN+1, got {matrix.shape[0]}x{matrix.shape[1]}"
        )

    rowcount, _ = matrix.shape

    # helper variable, will ease the pain of dealing with
    # indices
    # sh_indices = (s - 1, shape[1] - 1)

    # this is how i derived my solution:
    # matrix[0] /= matrix[0, 0]
    # matrix[1] += -matrix[1, 0] * matrix[0]
    # matrix[2] += -matrix[2, 0] * matrix[0]
    # as we can see, the first step is always normalizing the
    # working row so that its diagonal element is == 1.
    # then, all OTHER rows (hence the usage of set) should be manipulate
    # as seen here. we can extrapolate that into a neat loop.

    for i in range(0, rowcount):
        if matrix[i, i] == 0:
            # skipping division by zero
            continue
        matrix[i] /= matrix[i, i]
        for j in range(0, rowcount):
            if i == j:
                continue
            matrix[j] += -matrix[j, i] * matrix[i]

    if matrix[rowcount - 1, rowcount - 1] == 1:
        print("got the solutions!")
        for x in range(0, rowcount):
            print(f"x{x} = {matrix[x, rowcount+1]}")
    else:
        print("one or more of the solutions is a parameter")

    return matrix


A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], dtype=float)
print(gauss_jordan(A))
