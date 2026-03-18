import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    x=np.sort(np.array(x))
    ans=np.percentile(x,q,method='linear')
    return ans
    pass