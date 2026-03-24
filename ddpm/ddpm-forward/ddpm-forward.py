import numpy as np

def get_alpha_bar(betas: np.ndarray) -> np.ndarray:
    """
    Compute cumulative product of (1 - beta).
    """
    # YOUR CODE HERE
    alphabar=1-betas
    alphabar=np.cumprod(alphabar)
    return alphabar
    
    pass

def forward_diffusion(
    x_0: np.ndarray,
    t: int,
    betas: np.ndarray
) -> tuple:
    """
    Sample x_t from q(x_t | x_0).
    """
    # YOUR CODE HERE
    eps=np.random.randn(*x_0.shape)
    alphabar=get_alpha_bar(betas)
    alphat=alphabar[t-1]
    xt=x_0*np.sqrt(alphat)+np.sqrt(1-alphat)*eps
    return xt,eps
    pass
