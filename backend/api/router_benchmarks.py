from fastapi import APIRouter
from models.schemas import BenchmarkRequest
from services.benchmark_engine import PerformanceProfiler

router = APIRouter()
profiler = PerformanceProfiler()

@router.post("/run")
def run_performance_benchmarks(req: BenchmarkRequest):
    report = profiler.execute_suite(
        track_dimensions=req.target_dimensions,
        iterations_per_dim=req.iterations_per_dim
    )
    return {"status": "success", "data": report}