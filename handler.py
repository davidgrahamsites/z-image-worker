import runpod

def handler(job):
    inp = job.get("input", {})
    prompt = inp.get("prompt", "")
    return {"ok": True, "prompt": prompt}

runpod.serverless.start({"handler": handler})
