import numpy as np
from scipy.special import comb

def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """
    # Write code here
    if not ( (n, int) and n >= 0):
        raise ValueError("n must be a non-negative integer.")
    if not (0 <= p <= 1):
        raise ValueError("p must be between 0 and 1.")
    if not (isinstance(k, int) and 0 <= k <= n):
        raise ValueError("k must be an integer between 0 and n.")
    pmf = comb(n, k, exact=False) * (p ** k) * ((1 - p) ** (n - k))
    y = np.arange(0, k + 1)
    cdf = np.sum(comb(n, y, exact=False) * (p ** y) * ((1 - p) ** (n - y)))
    return float(pmf), float(cdf)
    pass