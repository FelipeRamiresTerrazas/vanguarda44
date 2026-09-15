import numpy as np
from PIL import Image, ImageDraw, ImageFilter

W, H = 1000, 1414
rng = np.random.default_rng(7)

base = np.array([250, 247, 238], dtype=np.float64)
canvas = np.tile(base, (H, W, 1))

grain = rng.normal(0, 3, (H, W, 1))
canvas += grain

stain_layer = Image.new("L", (W, H), 0)
sd = ImageDraw.Draw(stain_layer)
for _ in range(4):
    cx, cy = rng.integers(0, W), rng.integers(0, H)
    rx, ry = rng.integers(100, 220), rng.integers(80, 180)
    intensity = rng.integers(6, 14)
    sd.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=int(intensity))
stain_layer = stain_layer.filter(ImageFilter.GaussianBlur(90))
stain_arr = np.array(stain_layer, dtype=np.float64)[:, :, None]
canvas -= stain_arr * np.array([0.5, 0.55, 0.35])

yy, xx = np.mgrid[0:H, 0:W]
cx, cy = W / 2, H / 2
dist = np.sqrt(((xx - cx) / (W / 2)) ** 2 + ((yy - cy) / (H / 2)) ** 2)
vignette = np.clip((dist - 0.75) * 40, 0, 14)[:, :, None]
canvas -= vignette

canvas = np.clip(canvas, 0, 255).astype(np.uint8)
texture = Image.fromarray(canvas, mode="RGB")
texture = texture.filter(ImageFilter.GaussianBlur(0.5))
texture.save("estilo/textura_pagina.jpg", quality=85)
print("Textura gerada em estilo/textura_pagina.jpg")
