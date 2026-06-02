# CryptoScope: Applied Cryptography & Empirical Profiling Platform

**CryptoScope** is a full-stack, research-oriented interactive laboratory designed for the empirical analysis of cryptographic algorithms, structural vulnerabilities, and execution-time telemetry. 

Built to bridge the gap between abstract number theory and applied systems engineering, this platform provides high-resolution benchmarking and mathematical visualization of RSA cryptographic primitives.

## 🔬 Research Objectives

1. **Algorithmic Transparency:** To demystify black-box cryptographic libraries by implementing textbook mathematical primitives (Miller-Rabin Primality, Extended Euclidean Algorithm, Square-and-Multiply) from scratch in pure Python.
2. **Adversarial Cryptanalysis:** To mathematically simulate structural vulnerabilities in prime selection, utilizing Fermat's Factorization method to break weak moduli arrays.
3. **Empirical Telemetry:** To measure the asymptotic time complexity and hardware execution latency of cryptographic operations across variable bit dimensions, utilizing high-resolution nanosecond profiling and statistical aggregation.

## 🚀 Tech Stack

**Backend (The Profiling & Math Engine)**
* **Python 3.10+**: Core math execution and simulation logic.
* **FastAPI**: Asynchronous, high-performance API routing.
* **Pydantic**: Strict data validation and typing constraint enforcement.

**Frontend (The Academic Dashboard)**
* **React 18 & Vite**: Client-side rendering engine.
* **TypeScript**: Strict type safety across UI components.
* **Tailwind CSS**: Minimalist, research-focused aesthetic formatting.
* **Recharts**: D3-based rendering for empirical execution telemetry graphs.
* **MathJax**: Native rendering of LaTeX mathematical equations in the browser.

## 📂 Project Architecture

```text
cryptoscope/
├── backend/                             # Python Empirical Engine
│   ├── core/                            # Pure math: Miller-Rabin, EEA, exponentiation
│   ├── services/                        # Profiling loops & Fermat Factorization
│   ├── api/                             # RESTful routing (RSA, Attacks, Benchmarks)
│   ├── models/                          # Pydantic validation schemas
│   └── main.py                          # FastAPI ASGI entry point
└── frontend/                            # React Client
    └── src/
        ├── components/                  # DRY UI components (KeyValueGrid, MathBlock)
        ├── pages/                       # Module views (Explorer, Attacks, Telemetry)
        └── services/                    # Axios API integration