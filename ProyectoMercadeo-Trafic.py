from pytrends.request import TrendReq
import matplotlib.pyplot as plt

# 1️⃣ Conexión
pytrends = TrendReq(hl='es-CR', tz=360)

# 2️⃣ Entradas de usuario
num_sites = int(input("¿Cuántos sitios quieres comparar?: "))

terms = []
for i in range(num_sites):
    term = input(f"Dame el nombre del sitio o término #{i+1}: ")
    terms.append(term.strip())

# 3️⃣ Payload
pytrends.build_payload(terms, timeframe='today 12-m')

# 4️⃣ Obtener datos
data = pytrends.interest_over_time()

print(data.head())

# 5️⃣ Graficar
plt.figure(figsize=(12,6))
for term in terms:
    plt.plot(data.index, data[term], label=term)

plt.legend(loc='upper left')
plt.title('Comparativa de interés de búsqueda (últimos 12 meses)')
plt.xlabel('Fecha')
plt.ylabel('Interés relativo')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('trafico_trend.png')
plt.show()

print("\\n✅ Gráfico guardado como trafico_trend.png")
