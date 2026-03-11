import torch
import torch.nn as nn
import math

def create_embedding_layer(vocab_size: int, d_model: int) -> nn.Embedding:
    """
    Create an embedding layer with scaled initialization.
    """
    embedding = nn.Embedding(vocab_size, d_model, padding_idx=0)
    nn.init.normal_(embedding.weight, mean=0, std=1/math.sqrt(d_model))
    
    return embedding

def embed_tokens(embedding: nn.Embedding, tokens: torch.Tensor, d_model: int) -> torch.Tensor:
    """
    Convert token indices to scaled embeddings as per the Transformer paper.
    """

    return embedding(tokens) * math.sqrt(d_model)