from datetime import datetime
import matplotlib.pyplot as plt

marcas = []

num_marcas = int(input("¿Cuántas etiquetas (marcas) quieres registrar?: "))

for i in range(num_marcas):
    print(f"\n=== Marca #{i+1} ===")
    nombre = input("Nombre de la etiqueta: ")

    # Facebook
    fb_seguidores = int(input("Seguidores Facebook: "))
    fb_interacciones = 0
    print("Ingresa datos de las últimas 5 publicaciones en Facebook:")
    for j in range(5):
        likes = int(input(f"Post #{j+1} Likes: "))
        comentarios = int(input(f"Post #{j+1} Comentarios: "))
        fb_interacciones += (likes + comentarios)
    fb_promedio = fb_interacciones / 5
    fb_engagement = (fb_promedio / fb_seguidores) * 100

    # Instagram
    ig_seguidores = int(input("Seguidores Instagram: "))
    ig_interacciones = 0
    print("Ingresa datos de las últimas 5 publicaciones en Instagram:")
    for j in range(5):
        likes = int(input(f"Post #{j+1} Likes: "))
        comentarios = int(input(f"Post #{j+1} Comentarios: "))
        ig_interacciones += (likes + comentarios)
    ig_promedio = ig_interacciones / 5
    ig_engagement = (ig_promedio / ig_seguidores) * 100

    marca = {
        "Nombre": nombre,
        "FB_Seguidores": fb_seguidores,
        "FB_Engagement": fb_engagement,
        "IG_Seguidores": ig_seguidores,
        "IG_Engagement": ig_engagement
    }
    marcas.append(marca)

# Confirmar procesar
continuar = input("\n¿Procesar resultados? (Si/No): ").strip().lower()

if continuar != "si":
    print("\n🚫 Proceso cancelado.")
    exit()

# Generar tabla Markdown
output = []
output.append("| Marca | Seguidores FB | Engagement FB (%) | Seguidores IG | Engagement IG (%) |")
output.append("|-------|----------------|--------------------|----------------|---------------------|")
for m in marcas:
    output.append(f"| {m['Nombre']} | {m['FB_Seguidores']} | {m['FB_Engagement']:.2f} | {m['IG_Seguidores']} | {m['IG_Engagement']:.2f} |")

# Generar gráfico
nombres = [m['Nombre'] for m in marcas]
fb_rates = [m['FB_Engagement'] for m in marcas]
ig_rates = [m['IG_Engagement'] for m in marcas]

plt.figure(figsize=(10,6))
bar_width = 0.35
x = range(len(nombres))

plt.bar(x, fb_rates, width=bar_width, label='Facebook Engagement')
plt.bar([i + bar_width for i in x], ig_rates, width=bar_width, label='Instagram Engagement')
plt.xticks([i + bar_width/2 for i in x], nombres)

plt.ylabel("Engagement %")
plt.title("Comparativa de Engagement por Marca")
plt.legend()
plt.tight_layout()

fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
grafico_name = f"ProyectoMercadeo-Metrics-Grafico-{fecha}.png"
plt.savefig(grafico_name)
#plt.show()

# Guardar archivo Markdown
md_name = f"ProyectoMercadeo-Metrics-Informe-{fecha}.md"
with open(md_name, "w", encoding="utf-8") as f:
    for line in output:
        f.write(line + "\n")

print(f"\n✅ Informe guardado como {md_name}")
print(f"✅ Gráfico guardado como {grafico_name}")
print("\nProceso finalizado con éxito.")
