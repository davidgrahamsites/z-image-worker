from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class GenReq(BaseModel):
    prompt: str

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/generate")
def generate(req: GenReq):
    return {"ok": True, "received": req.prompt, "message": "worker stub (not generating yet)"}
