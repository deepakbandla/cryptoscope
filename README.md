# CryptoScope: Applied Cryptography & Empirical Profiling Platform

CryptoScope is a full-stack, research-oriented cryptography laboratory designed for the empirical analysis of RSA cryptographic primitives, structural vulnerabilities, and execution-time telemetry.

The platform bridges the gap between theoretical number theory and practical systems engineering by providing interactive cryptographic experimentation, mathematical visualization, and high-resolution performance benchmarking.

---

## 🔬 Research Objectives

### 1. Algorithmic Transparency

Demystify black-box cryptographic libraries by implementing foundational algorithms from first principles:

* Miller–Rabin Primality Testing
* Extended Euclidean Algorithm (EEA)
* Modular Exponentiation (Square-and-Multiply)

All algorithms are implemented in pure Python to expose the underlying mathematical mechanics of RSA cryptography.

### 2. Adversarial Cryptanalysis

Investigate weaknesses in RSA key generation through practical cryptanalytic simulations.

Current attack modules include:

* Fermat's Factorization Method
* Weak Prime Selection Analysis
* Vulnerable Modulus Demonstrations

These experiments illustrate how improper prime selection can compromise RSA security.

### 3. Empirical Telemetry

Measure both theoretical and practical performance characteristics of cryptographic operations through:

* Nanosecond-resolution timing
* Statistical aggregation
* Scaling analysis across multiple key sizes
* Computational complexity visualization

---

## 🚀 Technology Stack

### Backend — Cryptographic & Profiling Engine

| Technology   | Purpose                                |
| ------------ | -------------------------------------- |
| Python 3.10+ | Core mathematical computation          |
| FastAPI      | High-performance API framework         |
| Pydantic     | Data validation and schema enforcement |
| Uvicorn      | ASGI application server                |

### Frontend — Research Dashboard

| Technology   | Purpose                              |
| ------------ | ------------------------------------ |
| React 18     | User interface                       |
| TypeScript   | Type-safe development                |
| Vite         | Build tooling and development server |
| Tailwind CSS | Styling and responsive layouts       |
| Recharts     | Performance telemetry visualization  |
| MathJax      | LaTeX mathematical rendering         |

---

## 📂 Project Structure

```text
cryptoscope/
│
├── backend/
│   ├── core/              # Cryptographic primitives
│   │   ├── miller_rabin.py
│   │   ├── euclidean.py
│   │   └── exponentiation.py
│   │
│   ├── services/          # Benchmarking & cryptanalysis
│   ├── api/               # REST API endpoints
│   ├── models/            # Pydantic schemas
│   └── main.py            # FastAPI entry point
│
└── frontend/
    └── src/
        ├── components/    # Reusable UI components
        ├── pages/         # Explorer, Attacks, Telemetry
        └── services/      # API integration layer
```

---

## ✨ Features

### RSA Explorer

* Generate RSA key pairs
* Visualize key generation mathematics
* Explore modular arithmetic operations
* Inspect intermediate cryptographic values

### Cryptanalysis Laboratory

* Simulate Fermat factorization attacks
* Analyze weak RSA moduli
* Demonstrate practical vulnerabilities
* Study attack complexity and success conditions

### Performance Telemetry

* Benchmark key generation performance
* Measure encryption and decryption latency
* Compare execution times across bit lengths
* Visualize scaling behavior using interactive charts

### Mathematical Visualization

* Native LaTeX rendering via MathJax
* Step-by-step algorithm breakdowns
* Interactive mathematical explanations

---

## ⚙️ Installation & Setup

CryptoScope follows a decoupled architecture. Run the backend and frontend in separate terminal sessions.

### 1. Start the Backend

#### Requirements

* Python 3.10+
* pip

```bash
cd backend

python -m venv .venv

# Linux / macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

Backend API:

```text
http://localhost:8000
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

---

### 2. Start the Frontend

#### Requirements

* Node.js 18+
* npm

```bash
cd frontend

npm install

npm run dev
```

Frontend Dashboard:

```text
http://localhost:5173
```

---

## 📊 Dashboard Preview

### RSA Explorer

![RSA Explorer](docs/rsa-explorer.png)

### Cryptanalysis Simulation

![Fermat Attack](docs/fermat-attack.png)

### Empirical Telemetry Dashboard

![Telemetry Dashboard](docs/telemetry.png)

> Replace the images above with actual screenshots stored in the `docs/` directory.

---

## 📈 Example Research Questions

CryptoScope can be used to investigate:

* How does RSA key generation scale with increasing bit lengths?
* How effective is Fermat's factorization against poorly chosen primes?
* What is the practical runtime cost of modular exponentiation?
* How closely do empirical measurements align with theoretical complexity analysis?

---

## 🔮 Future Work

### Side-Channel Analysis

* Timing attack simulations
* Synthetic power-consumption traces
* Leakage visualization tools

### Randomness Evaluation

* Entropy estimation
* PRNG quality assessment
* Statistical randomness testing

### Machine Learning Distinguishers

* Support Vector Machines (SVMs)
* Decision Trees
* Classification of biased versus uniform bitstreams

### Extended Cryptographic Support

* Diffie–Hellman Key Exchange
* ElGamal Encryption
* Elliptic Curve Cryptography (ECC)

---

## 🎓 Educational Value

CryptoScope is designed for:

* Cryptography students
* Security researchers
* Computer science educators
* Systems performance analysts
* Enthusiasts exploring applied cryptography

The platform emphasizes transparency, reproducibility, and empirical investigation of cryptographic systems.

---

## 📜 License

This project is released under the MIT License.

---

## 👨‍💻 Author

**Deepak**

Applied Cryptography • Systems Engineering • Performance Analysis

CryptoScope was developed as a research and educational platform for exploring the mathematical foundations, practical implementation, and performance characteristics of modern cryptographic systems.
