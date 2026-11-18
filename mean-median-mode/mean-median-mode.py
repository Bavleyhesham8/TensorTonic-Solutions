from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    x=np.array(x)
    mean=float(np.mean(x))
    median=float(np.median(x))
    val,cou=np.unique(x,return_counts=True)
    mod=float(val[np.argmax(cou)])
    di={"mean":mean,"median":median,"mode":mod}
    return di