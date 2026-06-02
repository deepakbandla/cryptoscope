from typing import Optional, List
from .math_utils import (
    generate_prime,
    modular_inverse,
    extended_gcd,
    square_and_multiply
)


class TextbookRSA:
    def __init__(self, bit_size: int = 512):
        self.bit_size = bit_size

        self.p: Optional[int] = None
        self.q: Optional[int] = None
        self.n: Optional[int] = None
        self.phi: Optional[int] = None

        self.e: int = 65537  
        self.d: Optional[int] = None

    def generate_keys(self) -> dict:
        """Generates the public and private keypairs."""
        print(f"[*] Generating {self.bit_size}-bit RSA keys. This may take a moment...")

        self.p = generate_prime(self.bit_size // 2)
        self.q = generate_prime(self.bit_size // 2)

        while self.p == self.q:
            self.q = generate_prime(self.bit_size // 2)

        self.n = self.p * self.q

        self.phi = (self.p - 1) * (self.q - 1)

        gcd, _, _ = extended_gcd(self.e, self.phi)

        if gcd != 1:
            self.e = 3
            while extended_gcd(self.e, self.phi)[0] != 1:
                self.e += 2

        self.d = modular_inverse(self.e, self.phi)

        return {
            "public_key": (self.e, self.n),
            "private_key": (self.d, self.n),
        }

    def encrypt_string(self, plaintext: str) -> List[int]:
        """Encrypts a string by converting chars to integers and applying RSA."""
        if self.n is None:
            raise ValueError("Keys have not been generated yet.")

        n = self.n  # Pyright now knows this is an int

        ciphertext: List[int] = []

        for char in plaintext:
            m = ord(char)

            # c = m^e mod n
            c = square_and_multiply(m, self.e, n)
            ciphertext.append(c)

        return ciphertext

    def decrypt_string(self, ciphertext: List[int]) -> str:
        """Decrypts a list of integers back into a string."""
        if self.d is None:
            raise ValueError("Private key is missing.")

        if self.n is None:
            raise ValueError("Modulus is missing.")

        d = self.d
        n = self.n

        plaintext = ""

        for c in ciphertext:
            m = square_and_multiply(c, d, n)
            plaintext += chr(m)

        return plaintext