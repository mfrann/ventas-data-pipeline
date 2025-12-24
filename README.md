# 📊 Ventas Data Pipeline (ETL con Python)

Proyecto de **Data Engineering** que implementa un proceso **ETL (Extract, Transform, Load)** para analizar datos de ventas a partir de archivos CSV, generando métricas de negocio listas para análisis o carga en bases de datos.

---

## 🎯 Objetivo del Proyecto

Construir un pipeline ETL que:

- Procese datos crudos de ventas
- Limpie y transforme la información
- Enriquezca los datos con métricas clave
- Genere resultados agregados persistentes

El proyecto está diseñado como **portfolio de Data Engineering**, aplicando buenas prácticas de modularidad y arquitectura.

---

## ❓ Preguntas de Negocio que Responde

El pipeline responde a las siguientes preguntas:

1. **¿Cuánto se vende cada mes?**
2. **¿Qué productos generan más ingresos?**
3. **¿Cuáles son los clientes más importantes por volumen de compra?**
4. **¿Cuál es el desempeño de cada vendedor?**

   - Ventas totales
   - Unidades vendidas
   - Número de transacciones
   - Ticket promedio

---

## 📊 Resultados que Genera

El proceso ETL genera los siguientes archivos en la carpeta `outputs/`:

- `ventas_mes.csv` → Ventas totales agregadas por mes
- `top_productos.csv` → Productos con mayor generación de ingresos
- `top_clientes.csv` → Clientes con mayor volumen de compras
- `perf_vendedores.csv` → Métricas de desempeño por vendedor

Estos archivos quedan listos para:

- Análisis en Excel, Power BI o Tableau
- Carga en bases de datos SQL
- Uso en dashboards o reportes

---

## 🏗️ Arquitectura del Proyecto

```
ventas-data-pipeline/
│
├── etl/                     # Lógica del pipeline
│   ├── __init__.py
│   ├── extract.py           # Extracción de datos (CSV)
│   ├── transform.py         # Limpieza, enriquecimiento y métricas
│   ├── load.py              # Carga de resultados (CSV)
│   └── main.py              # Orquestador del ETL
│
├── datos/                   # Datos crudos (RAW)
│   ├── ventas.csv
│   ├── productos.csv
│   ├── clientes.csv
│   └── vendedores.csv
│
├── outputs/                 # Resultados finales (ANALYTICS)
│   ├── ventas_mes.csv
│   ├── top_productos.csv
│   ├── top_clientes.csv
│   └── perf_vendedores.csv
│
├── .gitignore
├── requirements.txt
├── README.md
```

---

## 🔄 Proceso ETL

### 1️⃣ Extract

- Lectura de archivos CSV
- Validación de existencia de datos

### 2️⃣ Transform

- Eliminación de duplicados
- Manejo de valores nulos (críticos y no críticos)
- Conversión de tipos de datos (fechas)
- Enriquecimiento de la tabla de ventas
- Agregaciones y métricas de negocio

### 3️⃣ Load

- Exportación de resultados finales a archivos CSV
- Creación automática de la carpeta `outputs/`

---

## 🚀 Cómo Ejecutar el Proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/mfrann/ventas-data-pipeline.git
cd ventas-data-pipeline
```

### 2. (Opcional) Crear entorno virtual

```bash
python -m venv .ventas-pipeline
source .ventas-pipeline/bin/activate   # Linux / Mac
.ventas-pipeline\Scripts\activate      # Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar el pipeline ETL

```bash
python etl/main.py
```

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.8+**
- **Pandas**
- **Pathlib**
- **Git & GitHub**

---

## 📌 Buenas Prácticas Aplicadas

- Separación clara de responsabilidades (Extract / Transform / Load)
- Código modular y reutilizable
- Manejo correcto de rutas relativas al proyecto
- Outputs persistentes y reproducibles
- Arquitectura escalable a SQL o herramientas de orquestación

---

## 👤 Autor

**Martin Caycho**
GitHub: [https://github.com/mfrann](https://github.com/mfrann)

---

## 📄 Licencia

Este proyecto está licenciado bajo la **Licencia MIT**.
Puedes usarlo, modificarlo y distribuirlo libremente.

⭐ Si te gustó el proyecto, ¡dale una estrella en GitHub!
