from pydantic import BaseModel
from typing import List, Optional

# --- RSA Models ---
class KeyGenRequest(BaseModel):
    bit_size: int = 256

class EncryptRequest(BaseModel):
    plaintext: str
    bit_size: int = 256  # For textbook initialization
    
class DecryptRequest(BaseModel):
    ciphertext: List[int]
    bit_size: int = 256

# --- Attack Models ---
class FermatAttackRequest(BaseModel):
    target_modulus: int
    max_iterations: int = 10_000_000

# --- Benchmark Models ---
class BenchmarkRequest(BaseModel):
    target_dimensions: List[int] = [64, 128, 256]
    iterations_per_dim: int = 3