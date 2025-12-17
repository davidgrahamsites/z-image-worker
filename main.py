from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class GenerateRequest(BaseModel):
    prompt: str

@app.post("/generate")
def generate(req: GenerateRequest):
    return {
        "ok": True,
        "prompt": req.prompt,
        "message": "RunPod worker alive"
    }

