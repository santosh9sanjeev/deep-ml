import numpy as np

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    # arr = np.transpose(a)

    shape = np.shape(a)
    arr = np.zeros((shape[1], shape[0]))
    for i in range(shape[0]):
        for j in range(shape[1]):
            arr[j][i] = a[i][j]

    return arr
