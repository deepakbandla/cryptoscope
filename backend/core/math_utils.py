import random
from typing import Tuple

def square_and_multiply(base: int,exponent: int, modulus: int) ->int:
    """
    Computes (base^exponent) % modulus using bitwise operations.
    This simulates hardware-level execution and is critical for side-channel research.
    """
    if modulus == 1:
        return 0
    
    result =1
    base = base %modulus
    
    # Process exponent bit by bit (from LSB to MSB)
    while exponent > 0:
        # if the least significant bit is 1,multiply
        if (exponent & 1)== 1:
            result = (result * base) % modulus
        
        # shift right (divide by 2) and square the base
        exponent = exponent >> 1
        base = (base * base) % modulus
        
    return result

def miller_rabin(n: int, k: int = 40) -> bool:
    """
    Probabilistic primality test. Returns True if n is likely prime.
    k = 40 gives a false positive probability of 4^-40.
    """
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # Find r and d such that n - 1 = 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = square_and_multiply(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
            
        for _ in range(r - 1):
            x = square_and_multiply(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits: int) -> int:
    """Generates a random prime number of the specified bit length."""
    while True:
        # Generate random odd number
        p = random.getrandbits(bits)

        # Ensure it has exactly 'bits' length by setting the MSB and LSB to 1
        p |= (1 << bits - 1) | 1
        if miller_rabin(p):
            return p

def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    Extended Euclidean Algorithm.
    Returns (gcd, x, y) such that a*x + b*y = gcd
    """
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def modular_inverse(e: int, phi: int) -> int:
    """Finds the modular inverse of e modulo phi."""
    gcd, x, y = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError(f"Modular inverse does not exist. {e} and {phi} are not coprime.")
    else:
        return x % phi