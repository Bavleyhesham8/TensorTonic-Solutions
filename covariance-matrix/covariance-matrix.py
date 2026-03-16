import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    y=np.asarray(X)
    if y.shape[0]<2 or y.ndim!=2:
        return None
    m=np.mean(y,axis=0)
    m=y-m
    ans=m.T@m
    ans/=y.shape[0]-1
    return ans
    pass