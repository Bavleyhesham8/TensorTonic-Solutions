import numpy as np
def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    image=np.array(image, dtype=np.float32)
    w=(image[:,:,0]*0.299+image[:,:,1]*0.587+image[:,:,2]*0.114)
    return w.tolist()
    # Write code here