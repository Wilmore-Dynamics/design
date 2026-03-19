import os
from PIL import Image, ImageDraw, ImageFont

# CONFIGURATION DE L'ADN VISUEL
COLOR_SAND = "#F5F5F3"
COLOR_BLACK = "#000000"
CANVAS_SIZE = (1280, 640)

# CHEMINS RELATIFS (Basés sur ta nouvelle structure)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO_PATH = os.path.join(BASE_DIR, "../../assets/logo.png")
FONT_BOLD = os.path.join(BASE_DIR, "fonts/Inter-Bold.ttf")
FONT_MEDIUM = os.path.join(BASE_DIR, "fonts/Inter-Medium.ttf")
OUTPUT_DIR = os.path.join(BASE_DIR, "../../previews")

def generate_social_preview(title, subtitle, filename):
    # 1. Création du canevas
    img = Image.new('RGB', CANVAS_SIZE, color=COLOR_SAND)
    draw = ImageDraw.Draw(img)

    # 2. Chargement des polices
    try:
        font_title = ImageFont.truetype(FONT_BOLD, 90)
        font_sub = ImageFont.truetype(FONT_MEDIUM, 32)
    except OSError:
        print("❌ Erreur : Polices .ttf introuvables dans scripts/social-generator/fonts/")
        return

    # 3. Dessiner le titre (Centré verticalement et horizontalement)
    w, h = CANVAS_SIZE
    
    # Calcul position Titre
    bbox_t = draw.textbbox((0, 0), title, font=font_title)
    t_w, t_h = bbox_t[2] - bbox_t[0], bbox_t[3] - bbox_t[1]
    draw.text(((w - t_w) / 2, (h / 2) - 50), title, fill=COLOR_BLACK, font=font_title)
    
    # 4. Dessiner le sous-titre (Style technique //)
    label = f"// {subtitle.upper()}"
    bbox_s = draw.textbbox((0, 0), label, font=font_sub)
    s_w = bbox_s[2] - bbox_s[0]
    draw.text(((w - s_w) / 2, (h / 2) + 70), label, fill=COLOR_BLACK, font=font_sub)

    # 5. Insertion du Logo (En bas à droite, signature discrète)
    if os.path.exists(LOGO_PATH):
        logo = Image.open(LOGO_PATH).convert("RGBA")
        logo.thumbnail((70, 70)) # Taille du logo
        img.paste(logo, (w - 130, h - 130), logo)
    else:
        print(f"⚠️ Logo non trouvé à l'emplacement : {LOGO_PATH}")

    # 6. Sauvegarde
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    save_path = os.path.join(OUTPUT_DIR, f"{filename}.png")
    img.save(save_path)
    print(f"✅ Image générée avec succès : {save_path}")

# EXEMPLES DE GÉNÉRATION
if __name__ == "__main__":
    # Liste de tes projets / dossiers
    projects = [
        ("Hardened Debian", "Infrastructure & Security", "og-debian"),
        ("N8N Workflows", "Automation & Sovereignty", "og-n8n"),
        ("Wilmore Lab", "Archive Technique V2", "og-lab"),
    ]
    
    for title, sub, file in projects:
        generate_social_preview(title, sub, file)
