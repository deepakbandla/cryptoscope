import math
import time
from typing import Tuple, Dict, Any

class CryptanalysisEngine:
    """
    Implements mathematical attacks on textbook RSA configurations
    to demonstrate structural cryptographic vulnerabilities.
    """

    @staticmethod
    def is_perfect_square(n: int) -> Tuple[bool, int]:
        """Helper to check if an integer is a perfect square using integer arithmetic."""
        if n < 0:
            return False, -1
        if n == 0 or n == 1:
            return True, n
            
        # Initial estimate using integer square root
        root = math.isqrt(n)
        return root * root == n, root

    def run_fermat_attack(self, n: int, max_iterations: int = 10_000_000) -> Dict[str, Any]:
        """
        Executes Fermat's Factorization Attack on an RSA public modulus n.
        Fails or times out if p and q are chosen randomly far apart.
        """
        start_time = time.perf_counter_ns()
        
        # a starts at the ceiling of the square root of n
        a = math.isqrt(n)
        if a * a < n:
            a += 1
            
        b2 = a * a - n
        iterations = 0
        success = False
        p, q = None, None

        while iterations < max_iterations:
            iterations += 1
            
            is_square, b = self.is_perfect_square(b2)
            if is_square:
                # If a^2 - n = b^2, then n = a^2 - b^2 = (a-b)(a+b)
                p = a + b
                q = a - b
                success = True
                break
                
            # Mathematically equivalent to: b2 = (a+1)^2 - n = a^2 + 2a + 1 - n = b2 + 2a + 1
            b2 += 2 * a + 1
            a += 1

        end_time = time.perf_counter_ns()
        execution_time_ms = (end_time - start_time) / 1_000_000

        return {
            "success": success,
            "p": p,
            "q": q,
            "iterations_executed": iterations,
            "execution_time_ms": execution_time_ms,
            "target_modulus": n,
            "analysis": (
                f"Attack succeeded in {iterations} iterations. Primes were structurally close."
                if success else 
                f"Attack exhausted maximum iteration ceiling ({max_iterations:,}) without finding factors. Primes are structurally sound."
            )
        }