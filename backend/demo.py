from core.rsa_core import TextbookRSA
from services.attack_engine import CryptanalysisEngine
from services.benchmark_engine import PerformanceProfiler

def verify_cryptanalysis():
    print("=== CryptoScope: Verifying Fermat's Factorization Attack ===")
    
    # We deliberately forge a vulnerable modulus by choosing two extremely close primes
    # p = 61051, q = 61099
    p_weak = 61051
    q_weak = 61099
    n_weak = p_weak * q_weak
    
    analyzer = CryptanalysisEngine()
    attack_report = analyzer.run_fermat_attack(n_weak)
    
    print(f"Target Modulus: {n_weak}")
    print(f"Attack Result Status: Success = {attack_report['success']}")
    print(f"Recovered Primes: p={attack_report['p']}, q={attack_report['q']}")
    print(f"Iterations Needed: {attack_report['iterations_executed']}")
    print(f"Time Taken: {attack_report['execution_time_ms']:.4f} ms")
    print(f"Report: {attack_report['analysis']}\n")

def verify_profiler():
    print("=== CryptoScope: Running Empirical Profiler Suite ===")
    profiler = PerformanceProfiler()
    
    # We sample smaller sizes for interactive testing to avoid long loop waits
    target_sizes = [64, 128, 256]
    suite_report = profiler.execute_suite(target_sizes, iterations_per_dim=3)
    
    print(f"{'Bit Size':<10}{'KeyGen Avg (ms)':<20}{'Encrypt Avg (ms)':<20}{'Decrypt Avg (ms)':<20}")
    print("-" * 70)
    for run in suite_report:
        print(f"{run['bit_size']:<10}"
              f"{run['metrics']['keygen_avg_ms']:<20.4f}"
              f"{run['metrics']['encrypt_avg_ms']:<20.4f}"
              f"{run['metrics']['decrypt_avg_ms']:<20.4f}")
    print("\n[SUCCESS] Phase 2 engine validation complete.")

if __name__ == "__main__":
    verify_cryptanalysis()
    verify_profiler()