import time
from typing import List, Dict, Any
from core.rsa_core import TextbookRSA

class PerformanceProfiler:
    """
    Handles micro-benchmarking loops to isolate cryptographic operational
    latencies from systemic operating system scheduling noise.
    """

    def profile_dimension(self, bit_size: int, iterations: int = 5) -> Dict[str, Any]:
        """
        Measures the average performance of keygen, encryption, and decryption 
        for a targeted RSA bit configuration.
        """
        keygen_times: List[float] = []
        encrypt_times: List[float] = []
        decrypt_times: List[float] = []
        
        test_message = "ASTRA-Lab-Benchmarking-Token"

        for _ in range(iterations):
            # 1. Profile Key Generation
            rsa_instance = TextbookRSA(bit_size=bit_size)
            t0 = time.perf_counter_ns()
            rsa_instance.generate_keys()
            t1 = time.perf_counter_ns()
            keygen_times.append((t1 - t0) / 1_000_000) # Convert to ms

            # 2. Profile Encryption Execution
            t2 = time.perf_counter_ns()
            ciphertext = rsa_instance.encrypt_string(test_message)
            t3 = time.perf_counter_ns()
            encrypt_times.append((t3 - t2) / 1_000_000)

            # 3. Profile Decryption Execution
            t4 = time.perf_counter_ns()
            rsa_instance.decrypt_string(ciphertext)
            t5 = time.perf_counter_ns()
            decrypt_times.append((t5 - t4) / 1_000_000)

        # Statistical Aggregation (Mean Calculation)
        return {
            "bit_size": bit_size,
            "iterations_sampled": iterations,
            "metrics": {
                "keygen_avg_ms": sum(keygen_times) / iterations,
                "encrypt_avg_ms": sum(encrypt_times) / iterations,
                "decrypt_avg_ms": sum(decrypt_times) / iterations
            }
        }

    def execute_suite(self, track_dimensions: List[int], iterations_per_dim: int = 5) -> List[Dict[str, Any]]:
        """Executes full profile suite over sequential algorithmic key bit limits."""
        results = []
        for bit_size in track_dimensions:
            # Safe boundary assertion: pure python textbook math hangs exponentially beyond 1024-bit configs
            if bit_size > 512 and iterations_per_dim > 3:
                iterations_per_dim = 2 # Clamp iterations to prevent system freeze during execution
            
            metrics = self.profile_dimension(bit_size, iterations=iterations_per_dim)
            results.append(metrics)
        return results