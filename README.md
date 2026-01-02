# 📊 Ventas Data Pipeline (ETL con Python)

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-green.svg)

## 📝 Descripción

Proyecto de Data Engineering que implementa un proceso ETL (Extract, Transform, Load) para analizar datos de ventas a partir de archivos CSV, generando métricas de negocio listas para análisis o carga en bases de datos.

## 🎯 Objetivo

Construir un pipeline ETL que:

- Procese datos crudos de ventas
- Limpie y transforme la información
- Enriquezca los datos con métricas clave
- Genere resultados agregados persistentes

## ❓ Preguntas de Negocio que Responde

El pipeline responde a las siguientes preguntas:

- ¿Cuánto se vende cada mes?
- ¿Qué productos generan más ingresos?
- ¿Cuáles son los clientes más importantes por volumen de compra?
- ¿Cuál es el desempeño de cada vendedor?

      - Ventas totales
      - Unidades vendidas
      - Número de transacciones
      - Ticket promedio

## 📂 Estructura del Proyecto

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
├── README.md
├── requirements.txt
```

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

## 🔧 Instalación

### Prerrequisitos

- Python 3.8 o superior
- pip

### Pasos

1. **Clonar el repositorio**

```bash
git clone https://github.com/mfrann/ventas-data-pipeline.git
cd ventas-data-pipeline
```

2. **Crear entorno virtual (recomendado)**

```bash
python -m venv .env
source .env/bin/activate  # En Windows: .env\Scripts\activate
```

3. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

## 🚀 Uso

### Ejecutar el pipeline completo

```bash
python etl/main.py
```

## 🛠️ Tecnologías Utilizadas

- **Python 3.8+**: Lenguaje principal
- **Pandas**: Manipulación y análisis de datos
- **CSV**: Formato de datos de entrada/salida

## 👨‍💻 Autor

**Martin Caycho**

- GitHub: [@mfrann](https://github.com/mfrann)

---

⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub :)

