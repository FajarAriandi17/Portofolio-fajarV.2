#!/usr/bin/env python3
"""Buat og-image.jpg + favicon dari aset yang sudah ter-embed di index.html.

Font (Bowlby One, Caveat Brush, Patrick Hand) dan foto diekstrak langsung dari
data-URI di dalam index.html, jadi hasilnya konsisten dengan tampilan situs dan
tidak butuh aset eksternal.
"""
import base64
import io
import re
from pathlib import Path

from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
HTML = (ROOT / "index.html").read_text(encoding="utf-8")

PAPER = (246, 243, 236)
INK = (21, 17, 46)
INDIGO = (70, 54, 184)
INDIGO2 = (58, 44, 163)
LAV = (217, 210, 247)
LIME = (230, 255, 90)


def extract_font(family: str) -> Path:
    """Ambil woff2 base64 dari @font-face, konversi ke ttf sementara."""
    pattern = (
        r'@font-face\{font-family:"' + re.escape(family) +
        r'";src:url\(data:font/woff2;base64,([A-Za-z0-9+/=]+)\)'
    )
    match = re.search(pattern, HTML)
    if not match:
        raise SystemExit(f"font {family} tidak ditemukan di index.html")
    out = Path("/tmp") / (family.replace(" ", "") + ".ttf")
    font = TTFont(io.BytesIO(base64.b64decode(match.group(1))))
    font.flavor = None
    font.save(out)
    return out


def extract_image(var_name: str) -> Image.Image:
    match = re.search(
        r"--" + var_name + r":url\(data:image/png;base64,([A-Za-z0-9+/=]+)\)", HTML
    )
    if not match:
        raise SystemExit(f"gambar --{var_name} tidak ditemukan di index.html")
    return Image.open(io.BytesIO(base64.b64decode(match.group(1)))).convert("RGBA")


def sticker_outline(img: Image.Image, width: int, color) -> Image.Image:
    """Tiru efek stiker: outline mengelilingi alpha channel."""
    alpha = img.split()[3]
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    solid = Image.new("RGBA", img.size, color + (255,))
    for dx in range(-width, width + 1):
        for dy in range(-width, width + 1):
            if dx * dx + dy * dy > width * width:
                continue
            shifted = Image.new("L", img.size, 0)
            shifted.paste(alpha, (dx, dy))
            layer.paste(solid, (0, 0), shifted)
    layer.alpha_composite(img)
    return layer


def main() -> None:
    bowlby = extract_font("Bowlby One")
    caveat = extract_font("Caveat Brush")
    patrick = extract_font("Patrick Hand")

    W, H = 1200, 630
    canvas = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(canvas)

    # Pita indigo di sisi kanan (mengikuti blok "Selected Work")
    draw.polygon([(760, 0), (W, 0), (W, H), (690, H)], fill=INDIGO)

    f_title = ImageFont.truetype(str(bowlby), 132)
    f_name = ImageFont.truetype(str(caveat), 62)
    f_body = ImageFont.truetype(str(patrick), 34)
    f_tag = ImageFont.truetype(str(bowlby), 27)
    f_small = ImageFont.truetype(str(patrick), 27)

    # Judul PORTFOLIO dengan bayangan keras ala poster
    for line, y in (("PORT", 54), ("FOLIO", 176)):
        draw.text((62 + 6, y + 6), line, font=f_title, fill=(23, 18, 63))
        draw.text((62, y), line, font=f_title, fill=INDIGO)

    draw.text((66, 330), "Muhammad Fajar Ariandi", font=f_name, fill=INK)

    # Label profesi bergaya stempel
    label = "IT / JARINGAN & KONTEN KREATOR"
    lw = draw.textlength(label, font=f_tag)
    draw.rectangle([66, 404, 66 + lw + 44, 460], fill=INK)
    draw.text((88, 415), label, font=f_tag, fill=PAPER)

    # Highlight kutipan
    quote = "Jaringan stabil bikin semua jalan,"
    quote2 = "konten rapi bikin terlihat."
    draw.rectangle([64, 486, 64 + draw.textlength(quote, font=f_body) + 20, 528], fill=LAV)
    draw.text((74, 490), quote, font=f_body, fill=INK)
    draw.text((74, 532), quote2, font=f_body, fill=INK)

    # Foto cutout dengan outline stiker
    photo = extract_image("photo")
    target_h = 600
    ratio = target_h / photo.height
    photo = photo.resize((int(photo.width * ratio), target_h), Image.LANCZOS)
    photo = sticker_outline(photo, 4, INDIGO)
    photo = sticker_outline(photo, 5, (255, 255, 255))
    canvas.paste(photo, (W - photo.width - 70, H - photo.height), photo)

    # Handle sosial media di pojok kanan bawah
    draw.text((W - 330, H - 46), "@fjrarndii_ · fajarariandi17", font=f_small, fill=LIME)

    canvas.save(ROOT / "og-image.jpg", quality=86, optimize=True)

    # Favicon: huruf F di atas kotak indigo
    ico = Image.new("RGBA", (256, 256), INDIGO + (255,))
    d = ImageDraw.Draw(ico)
    f_ico = ImageFont.truetype(str(bowlby), 190)
    box = d.textbbox((0, 0), "F", font=f_ico)
    d.text(
        ((256 - (box[2] - box[0])) / 2 - box[0], (256 - (box[3] - box[1])) / 2 - box[1]),
        "F",
        font=f_ico,
        fill=PAPER,
    )
    ico.save(ROOT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
    ico.resize((180, 180), Image.LANCZOS).convert("RGB").save(
        ROOT / "apple-touch-icon.png"
    )

    print("selesai:", (ROOT / "og-image.jpg").stat().st_size, "bytes")


if __name__ == "__main__":
    main()
