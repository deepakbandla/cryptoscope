from backend.core.rsa_core import TextbookRSA
import time

def main():
    print("=== CryptoScope: Phase 1 Math Engine ===\n")
    
    # Initialize RSA with a small bit size for instant generation during testing
    # In Phase 2, we will benchmark this up to 2048 bits.
    rsa = TextbookRSA(bit_size=256)
    
    start_time = time.perf_counter_ns()
    keys = rsa.generate_keys()
    end_time = time.perf_counter_ns()
    
    print("\n[+] Keys Generated Successfully!")
    print(f"Time Taken: {(end_time - start_time) / 1_000_000:.2f} ms\n")
    
    print("--- Cryptographic Parameters ---")
    print(f"Modulus (n): {keys['public_key'][1]}")
    print(f"Public Exponent (e): {keys['public_key'][0]}")
    print(f"Private Exponent (d): {keys['private_key'][0]}")
    print("-" * 32 + "\n")

    message = "ASTRA Lab Research Internship 2026"
    print(f"Original Message: '{message}'")

    # Encrypt
    encrypted_data = rsa.encrypt_string(message)
    print(f"Ciphertext Array: {encrypted_data[:3]}... (truncated for display)")

    # Decrypt
    decrypted_message = rsa.decrypt_string(encrypted_data)
    print(f"Decrypted Message: '{decrypted_message}'")
    
    assert message == decrypted_message, "DECRYPTION FAILED!"
    print("\n[SUCCESS] Encryption and Decryption mathematically verified.")

if __name__ == "__main__":
    main()