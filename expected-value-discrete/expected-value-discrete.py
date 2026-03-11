import numpy as np

def expected_value_discrete(x, p):
    x = np.array(x)
    p = np.array(p)
    
    if x.shape != p.shape:
        raise ValueError("x and p must have the same shape.")
    
    if not np.allclose(np.sum(p), 1.0, atol=1e-6):
        raise ValueError(f"Probabilities must sum to 1.0 (current sum: {np.sum(p)})")
        
    return np.dot(x, p)
