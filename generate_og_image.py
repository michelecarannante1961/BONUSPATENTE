"""
Generatore di immagine Open Graph (1200x630 px) ad alto impatto per social media.
Combina la copertina del libro con un layout professionale, badge e testi in evidenza.
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

base_dir = r"C:\Users\pcù\.gemini\antigravity\scratch\landing-autista-camion-2026"
assets_dir = os.path.join(base_dir, "assets")
cover_path = os.path.join(assets_dir, "cover.jpg")
output_path = os.path.join(assets_dir, "og-banner.jpg")

width, height = 1200, 630
img = Image.new("RGB", (width, height), color=(15, 23, 42))  # Slate 900
draw = ImageDraw.Draw(img)

# 1. Background gradient (dark navy to deep blue)
for y in range(height):
    r = int(15 + (y / height) * 12)
    g = int(23 + (y / height) * 20)
    b = int(42 + (y / height) * 45)
    draw.line([(0, y), (width, y)], fill=(r, g, b))

# 2. Glowing accent circles in background
glow = Image.new("RGBA", (width, height), (0, 0, 0, 0))
glow_draw = ImageDraw.Draw(glow)
glow_draw.ellipse([700, -100, 1300, 500], fill=(255, 153, 0, 45))   # Amazon Amber glow
glow_draw.ellipse([-100, 200, 400, 700], fill=(14, 165, 233, 30))  # Sky blue glow
glow = glow.filter(ImageFilter.GaussianBlur(80))
img.paste(glow, (0, 0), glow)

# Re-obtain draw after paste
draw = ImageDraw.Draw(img)

# 3. Load cover and create 3D styled thumbnail with shadow
if os.path.exists(cover_path):
    cover = Image.open(cover_path).convert("RGBA")
    # Target height 500px maintaining aspect ratio
    target_h = 500
    w_ratio = target_h / cover.height
    target_w = int(cover.width * w_ratio)
    cover_resized = cover.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    # Shadow
    shadow_pad = 40
    shadow = Image.new("RGBA", (target_w + shadow_pad * 2, target_h + shadow_pad * 2), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow)
    s_draw.rectangle([shadow_pad, shadow_pad, shadow_pad + target_w, shadow_pad + target_h], fill=(0, 0, 0, 190))
    shadow = shadow.filter(ImageFilter.GaussianBlur(25))
    
    pos_x = 800
    pos_y = 65
    img.paste(shadow, (pos_x - shadow_pad + 15, pos_y - shadow_pad + 15), shadow)
    img.paste(cover_resized, (pos_x, pos_y), cover_resized)
    
    # Add subtle border around cover
    draw = ImageDraw.Draw(img)
    draw.rectangle([pos_x, pos_y, pos_x + target_w, pos_y + target_h], outline=(255, 255, 255, 80), width=2)

# 4. Fonts
def get_font(size, bold=False):
    # Try Windows system fonts (Segoe UI, Arial, Calibri)
    font_names = ["segoeuib.ttf", "arialbd.ttf"] if bold else ["segoeui.ttf", "arial.ttf"]
    win_fonts = r"C:\Windows\Fonts"
    for name in font_names:
        p = os.path.join(win_fonts, name)
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()

font_badge = get_font(20, bold=True)
font_title = get_font(46, bold=True)
font_sub = get_font(24, bold=False)
font_highlight = get_font(26, bold=True)

# 5. Badge pill: "BANDO MIT 2026 ATTIVO"
badge_text = " ★  BANDO MIT 2026 UFFICIALMENTE ATTIVO  ★ "
bx1, by1 = 70, 75
badge_box = draw.textbbox((bx1, by1), badge_text, font=font_badge)
bw = badge_box[2] - badge_box[0] + 30
bh = badge_box[3] - badge_box[1] + 16
draw.rounded_rectangle([bx1, by1, bx1 + bw, by1 + bh], radius=20, fill=(255, 153, 0), outline=(255, 184, 77), width=2)
draw.text((bx1 + 15, by1 + 7), badge_text, fill=(15, 23, 42), font=font_badge)

# 6. Title
draw.text((70, 140), "AUTISTA DI CAMION 2026", fill=(255, 255, 255), font=font_title)

# 7. Subtitle / Value Prop lines
line1 = "Guida al Bonus MIT da 2.500 € a Fondo Perduto"
line2 = "& Accesso a oltre 30.000 Assunzioni Immediate"
draw.text((70, 210), line1, fill=(255, 184, 77), font=font_highlight)
draw.text((70, 248), line2, fill=(56, 189, 248), font=font_highlight)

desc_p = (
    "Come ottenere l'80% di rimborso per CQC e Patenti C, CE, D,\n"
    "vincere il click-day con SPID/CIE e accedere a stipendi da\n"
    "1.800 € a 2.800 € netti al mese nel trasporto merci e persone."
)
draw.text((70, 310), desc_p, fill=(203, 213, 225), font=font_sub)

# 8. Highlights Boxes (Stats)
stat_y = 430
stats = [
    ("2.500 €", "Bonus MIT"),
    ("30.000+", "Posti Vacanti"),
    ("CQC + C/CE/D", "Patenti Finanziate")
]
cur_x = 70
for val, lbl in stats:
    box_w = 210
    draw.rounded_rectangle([cur_x, stat_y, cur_x + box_w, stat_y + 70], radius=12, fill=(30, 41, 59), outline=(51, 65, 85), width=1)
    draw.text((cur_x + 16, stat_y + 10), val, fill=(255, 255, 255), font=get_font(22, bold=True))
    draw.text((cur_x + 16, stat_y + 40), lbl, fill=(148, 163, 184), font=get_font(15, bold=False))
    cur_x += box_w + 15

# 9. Bottom CTA Bar
cta_y = 535
draw.text((70, cta_y + 10), "Libro di Roberto Moretti  •  Disponibile su Amazon Kindle a 6,99 € (Gratis con KU)", fill=(226, 232, 240), font=get_font(18, bold=False))

# Save image
img.save(output_path, quality=95)
print(f"Generated {output_path} successfully ({os.path.getsize(output_path)} bytes)")
