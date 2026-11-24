import numpy as np
import math
def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    # Your code here
    # ls = arr.flatten()
    # val = 0
    # if norm_type == 'l1':
    #     for i in ls:
    #         val += abs(i)
    # elif norm_type == 'l2':
    #     for i in ls:
    #         val+= i**2
    #     val = math.sqrt(val)
    # elif norm_type == 'linf':
    #     val = max(abs(ls))
    # elif norm_type == 'frobenius':
    #     if len(arr.shape) != 2:
    #         raise ValueError("ValueError")
    #     else:
    #         for i in ls:
    #             val+= i**2
    #         val = math.sqrt(val)
    #         return val
    # else:
    #     raise ValueError("ValueError")
    # return val

    if norm_type=='l1':
        arr = arr.flatten()
        val = np.linalg.norm(arr, ord=1)
        return val
        # return np.linalg.norm(arr, ord=1)
    elif norm_type=='l2':
        arr = arr.flatten()
        return np.linalg.norm(arr, ord=2)
    elif norm_type=='linf':
        arr = arr.flatten()
        return np.linalg.norm(arr, ord=np.inf)
    elif norm_type=='frobenius':
        try:
            val = np.linalg.norm(arr, ord='fro')
            return val
        except:
            raise ValueError("ValueError")
    else:
        raise ValueError("ValueError")

    pass
