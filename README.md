# 🚀 ProyectoMercadeo

**ProyectoMercadeo** es una colección de scripts Python diseñados para realizar análisis básicos de marketing digital, visibilidad SEO, tráfico de interés y métricas de redes sociales, orientados principalmente a **uso académico y demostrativo**.

---

## 📑 Scripts incluidos

### 1️⃣ ProyectoMercadeo-SEO.py

Realiza una auditoría SEO de un sitio web:

* Descarga la página principal.
* Verifica etiquetas clave (`<title>`, `meta description`, `canonical`, `robots`, Open Graph, encabezados).
* Revisa estructura básica (`head`, `nav`, `footer`).
* Calcula una **calificación SEO** sobre 10 puntos.
* Guarda un informe `.md` con tabla y nota explicativa.

---

### 2️⃣ ProyectoMercadeo-Trafic.py

Consulta el **interés de búsqueda** mediante **PyTrends**:

* Permite comparar múltiples términos (marcas, palabras clave).
* Recupera tendencias de los últimos 12 meses.
* Genera un gráfico `.png` de popularidad relativa.
* Muestra tabla de datos para análisis complementario.

---

### 3️⃣ ProyectoMercadeo-Metrics.py

Permite comparar **métricas clave de redes sociales**:

* Registra dinámicamente marcas y datos.
* Calcula **engagement rate** de Facebook e Instagram basándose en las interacciones de las últimas 5 publicaciones.
* Crea una **tabla Markdown** y un **gráfico de barras** comparativo.
* Guarda ambos con nombre dinámico y fecha.

---

## 📈 Fórmula del engagement

El **engagement rate** se calcula como:

```
Engagement (%) = ((Likes + Comentarios) ÷ Nº de Seguidores) × 100
```

> Referencia: Ryan, D., & Jones, C. (2022). *Understanding Digital Marketing* (5th ed.). Kogan Page.

---

## ⚙️ Requisitos

* Python 3
* Librerías:

  * `beautifulsoup4`
  * `requests`
  * `matplotlib`
  * `pytrends`

Instala dependencias con:

```
pip install beautifulsoup4 requests matplotlib pytrends
```

---

## 📂 Estructura recomendada

```
ProyectoMercadeo/
├── ProyectoMercadeo-SEO.py
├── ProyectoMercadeo-Trafic.py
├── ProyectoMercadeo-Metrics.py
├── README.md
├── .gitignore
├── LICENSE (MIT)
```

---

## ⚖️ Licencia

Este proyecto está licenciado bajo la **Licencia MIT**.

---

## 📚 Uso académico

⚠️ **Nota:** Este proyecto fue desarrollado como práctica de análisis digital con fines **académicos y demostrativos**.
El autor no se responsabiliza por usos indebidos ni por la explotación comercial sin autorización expresa.

---

## 👤 Autor

Desarrollado y mantenido por [CoderEsteban](https://github.com/CoderEsteban/ProyectoMercadeo).

---

## ✅ Resultado final

* Informes `.md` y gráficos `.png` claros y exportables.
* Estructura modular y reutilizable para auditorías simples.
* Ideal para prácticas de análisis de marketing digital.

---
