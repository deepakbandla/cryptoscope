from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.router_rsa import router as rsa_router
from api.router_attacks import router as attacks_router
from api.router_benchmarks import router as benchmarks_router

app = FastAPI(
    title="CryptoScope API",
    description="Backend engine for cryptographic mathematics, attacks, and empirical profiling.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

app.include_router(rsa_router, prefix="/api/v1/rsa", tags=["RSA Core"])
app.include_router(attacks_router, prefix="/api/v1/attacks", tags=["Cryptanalysis"])
app.include_router(benchmarks_router, prefix="/api/v1/benchmarks", tags=["Empirical Profiling"])

@app.get("/")
def health_check():
    return {"status": "online", "system": "CryptoScope Empirical Engine"}

if __name__ == "__main__":
    import uvicorn
    # This allows you to run the file directly via `python main.py`
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)