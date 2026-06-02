from fastapi import APIRouter
from models.schemas import FermatAttackRequest
from services.attack_engine import CryptanalysisEngine

router = APIRouter()
analyzer = CryptanalysisEngine()

@router.post("/fermat")
def execute_fermat_attack(req: FermatAttackRequest):
    report = analyzer.run_fermat_attack(
        n=req.target_modulus, 
        max_iterations=req.max_iterations
    )
    return report