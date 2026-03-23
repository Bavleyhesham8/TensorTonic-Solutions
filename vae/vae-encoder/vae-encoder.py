import numpy as np

def vae_encoder(x: np.ndarray, latent_dim: int) -> tuple:
    """
    Encode input to latent distribution parameters.
    """
    # Your implementation here
    wm=np.random.rand(x.shape[1],latent_dim)
    wl=np.random.rand(x.shape[1],latent_dim)
    b1=np.zeros(latent_dim)
    b2=np.zeros(latent_dim)
    return x@wm+b1, x@wl+b2
    
    pass