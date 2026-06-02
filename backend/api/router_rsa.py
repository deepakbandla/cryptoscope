from fastapi import APIRouter, HTTPException
from models.schemas import KeyGenRequest, EncryptRequest, DecryptRequest
from core.rsa_core import TextbookRSA

router = APIRouter()


@router.post("/generate")
def generate_keys(req: KeyGenRequest):
    if req.bit_size > 1024:
        raise HTTPException(status_code=400, detail="For textbook pure-Python math, keep bit size <= 1024 to prevent timeouts.")
    
    rsa = TextbookRSA(bit_size=req.bit_size)
    keys = rsa.generate_keys()
    
    return {
        "status": "success",
        "bit_size": req.bit_size,
        "n": keys["public_key"][1],
        "e": keys["public_key"][0],
        "d": keys["private_key"][0]
    }

@router.post("/encrypt")
def encrypt_message(req: EncryptRequest):
    # In a real scenario, we'd pass e and n. Here we simulate for the explorer.
    rsa = TextbookRSA(bit_size=req.bit_size)
    rsa.generate_keys() # Generate fresh keys for the demo
    
    ciphertext = rsa.encrypt_string(req.plaintext)
    return {
        "status": "success",
        "ciphertext": ciphertext,
        "public_key": {"e": rsa.e, "n": rsa.n},
        "private_key": {"d": rsa.d} 
    }