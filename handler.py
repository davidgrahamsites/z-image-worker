import base64
from io import BytesIO

import runpod
from PIL import Image, ImageDraw

def handler(event):
    inp = event.get("input", {}) or {}
    prompt = inp.get("prompt", "")

    img = Image.new("RGB", (768, 512), (20, 20, 20))
    draw = ImageDraw.Draw(img)
    draw.text((24, 24), f"PROMPT:\n{prompt}", fill=(240, 240, 240))

    buf = BytesIO()
    img.save(buf, format="PNG")
    image_b64 = base64.b64encode(buf.getvalue()).decode("utf-8")

    return {"ok": True, "image_b64": image_b64}

runpod.serverless.start({"handler": handler})
