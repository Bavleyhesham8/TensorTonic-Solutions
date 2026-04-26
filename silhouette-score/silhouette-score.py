import numpy as np

def silhouette_score(X, labels):
    """
    Compute the mean Silhouette Score for given points and cluster labels.
    X: np.ndarray of shape (n_samples, n_features)
    labels: np.ndarray of shape (n_samples,)
    Returns: float
    """
    # Write code here
    dis=np.sqrt(((X[:,None,:]-X[None,:,:])**2).sum(axis=2))
    n=len(X)
    a=np.zeros(n)
    for clus in np.unique(labels):
        mask=labels==clus
        sud=dis[np.ix_(mask,mask)]
        if sud.shape[0]>1:
            a[mask]=(sud.sum(axis=1)-np.diag(sud))/(sud.shape[0]-1)
    b=np.full(n,np.inf)
    for cluster in np.unique(labels):
        mask_i = labels == cluster
        for other in np.unique(labels):
            if other == cluster: 
                continue
            mask_j = labels == other
            # average distance from cluster i points to cluster j points
            avg_dist = dis[np.ix_(mask_i, mask_j)].mean(axis=1)
            b[mask_i] = np.minimum(b[mask_i], avg_dist)
        
    s = (b - a) / np.maximum(a, b)

    return s.mean()
    pass