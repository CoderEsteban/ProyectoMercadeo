import os
from bs4 import BeautifulSoup
from datetime import datetime
import subprocess

try:
    from googlesearch import search
    google_enabled = True
except ImportError:
    google_enabled = False

# -------------------------------
# CONFIGURACIÓN UNIVERSAL
# -------------------------------
URL = "https://www.bmw-motorrad.cr"
FILE_PATH = "index.html"

print(f"\n🚀 Descargando {FILE_PATH} desde {URL} con wget...")
subprocess.run(["wget", "-O", FILE_PATH, URL], check=True)

print(f"\nIniciando análisis local de archivo: {FILE_PATH}")

output = []

try:
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, "html.parser")

    title = soup.title.string.strip() if soup.title else "No encontrado"
    meta_desc_tag = soup.find("meta", attrs={"name": "description"})
    meta_desc = meta_desc_tag["content"].strip() if meta_desc_tag else "No encontrada"

    meta_author_tag = soup.find("meta", attrs={"name": "author"})
    meta_author = meta_author_tag["content"].strip() if meta_author_tag else "No encontrada"

    has_head = bool(soup.head)
    has_nav = bool(soup.find("nav"))
    has_footer = bool(soup.find("footer"))
    h1_list = [h.get_text(strip=True) for h in soup.find_all("h1")]

    meta_viewport = soup.find("meta", attrs={"name": "viewport"})
    viewport = meta_viewport["content"].strip() if meta_viewport else "No encontrada"

    canonical_tag = soup.find("link", rel="canonical")
    canonical = canonical_tag["href"].strip() if canonical_tag else "No encontrada"

    meta_robots = soup.find("meta", attrs={"name": "robots"})
    robots = meta_robots["content"].strip() if meta_robots else "No encontrada"

    og_title = soup.find("meta", property="og:title")
    og_title_content = og_title["content"].strip() if og_title else "No encontrada"

    h2_list = soup.find_all("h2")
    h3_list = soup.find_all("h3")

    images = soup.find_all("img")
    images_without_alt = [img for img in images if not img.get("alt")]

    output.append("| Recurso | Estado | Valor |\n|---|---|---|")
    output.append(f"| Título de la página | {'✔️' if title != 'No encontrado' else '❌'} | {title} |")
    output.append(f"| Meta Description | {'✔️' if meta_desc != 'No encontrada' else '❌'} | {meta_desc} |")
    output.append(f"| Meta Author | {'✔️' if meta_author != 'No encontrada' else '❌'} | {meta_author} |")
    output.append(f"| Meta Viewport | {'✔️' if viewport != 'No encontrada' else '❌'} | {viewport} |")
    output.append(f"| Canonical | {'✔️' if canonical != 'No encontrada' else '❌'} | {canonical} |")
    output.append(f"| Meta Robots | {'✔️' if robots != 'No encontrada' else '❌'} | {robots} |")
    output.append(f"| Open Graph Title | {'✔️' if og_title_content != 'No encontrada' else '❌'} | {og_title_content} |")
    output.append(f"| Contiene head | {'✔️' if has_head else '❌'} | - |")
    output.append(f"| Contiene nav | {'✔️' if has_nav else '❌'} | - |")
    output.append(f"| Contiene footer | {'✔️' if has_footer else '❌'} | - |")
    output.append(f"| h1 encontrados | {'✔️' if len(h1_list) >=1 else '❌'} | {h1_list} |")
    output.append(f"| h2 encontrados | {'✔️' if len(h2_list) >=1 else '❌'} | {len(h2_list)} |")
    output.append(f"| h3 encontrados | {'✔️' if len(h3_list) >=1 else '❌'} | {len(h3_list)} |")
    output.append(f"| Imágenes sin alt | {'✔️' if len(images_without_alt) == 0 else '❌'} | {len(images_without_alt)} sin alt de {len(images)} |")
    output.append(f"| Peso HTML | ✔️ | {len(html_content) // 1024} KB |\n")

    score = 0
    total_checks = 10
    if title != "No encontrado": score += 1
    if meta_desc != "No encontrada": score += 1
    if meta_author != "No encontrada": score += 1
    if viewport != "No encontrada": score += 1
    if canonical != "No encontrada": score += 1
    if robots != "No encontrada": score += 1
    if og_title_content != "No encontrada": score += 1
    if len(images_without_alt) == 0: score += 1
    if len(h1_list) >= 1: score += 1
    if has_nav and has_footer: score += 1

    percentage = (score / total_checks) * 100

    output.append(f"\nNota: La calificación SEO se calcula sobre {total_checks} criterios clave, sumando 1 punto por cada requisito cumplido.\n")
    output.append(f"**Calificación SEO:** {percentage:.1f}%")

except Exception as e:
    output.append(f"Error: {e}")

if google_enabled:
    output.append("\n🔍 Resultados de búsqueda en Google:")
    query = URL
    count = 0
    for url in search(query):
        output.append(f"- {url}")
        count += 1
        if count >= 5:
            break
else:
    output.append("\nGooglesearch no está instalado. Ejecuta: pip install googlesearch-python")

output.append("\n🔗 Generado por: https://github.com/CoderEsteban/ProyectoMercadeo")

fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"seo_{URL.replace('https://','').replace('www.','').replace('/','_')}_{fecha}.md"
with open(filename, "w", encoding="utf-8") as f:
    for line in output:
        f.write(line + "\n")

print(f"\nReporte guardado como {filename}")

try:
    os.remove(FILE_PATH)
    print(f"✅ Archivo local {FILE_PATH} eliminado.")
except Exception as e:
    print(f"No se pudo eliminar {FILE_PATH}: {e}")
