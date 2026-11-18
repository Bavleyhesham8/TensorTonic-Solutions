import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a=np.array(a)
    b=np.array(b)
    ne=np.dot(a,b)
    de1=np.linalg.norm(a)
    de2=np.linalg.norm(b)
    if de1==0 or de2==0:
        return 0.0
    return float(ne/(de1*de2))
    