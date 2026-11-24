import numpy as np

def cosine_similarity(v1, v2):
    """
    Calculate the cosine_similarity of two vectors.
    Args:
        vec1 (numpy.ndarray): 1D array representing the first vector.
        vec2 (numpy.ndarray): 1D array representing the second vector.
    Returns:
        The cosine_similarity of the two vectors.
    """
    # Implement your code here
    if np.shape(v1)!=np.shape(v2):
        raise ValueError

    v1 = v1.flatten()
    v2 = v2.flatten() 

    if np.linalg.norm(v1, ord=2)!=0 and np.linalg.norm(v1, ord=2)!=0:
        return np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
    pass