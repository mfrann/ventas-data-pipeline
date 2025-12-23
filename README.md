# 📊 Ventas Data Pipeline – Proyecto ETL con Python

Proyecto de **Data Engineering** que implementa un **pipeline ETL (Extract, Transform, Load)** para procesar datos de ventas usando **Python, Pandas y SQL**.

---

## 🎯 Objetivo del Proyecto

Construir un pipeline ETL que:

* Extrae datos desde múltiples archivos CSV
* Limpia y transforma la información aplicando reglas de negocio
* Prepara los datos para análisis y carga en una base de datos
* Sigue buenas prácticas de ingeniería de datos

---

## 🏗️ Arquitectura del Proyecto

```
ventas-data-pipeline/
│
├── etl/
│   ├── __init__.py
│   ├── extract.py      # Extracción de datos (CSV)
│   ├── transform.py    # Limpieza y transformación
│   └── main.py         # Orquestador del ETL
│
├── datos/
│   ├── ventas.csv
│   ├── productos.csv
│   ├── clientes.csv
│   └── vendedores.csv
│
├── outputs/            # Resultados del pipeline (futuro)
├── requirements.txt
└── README.md
```

---

## 🔄 Flujo ETL

### 1️⃣ Extract

* Lectura de 4 archivos CSV
* Validación de existencia de archivos

### 2️⃣ Transform

* Eliminación de duplicados
* Identificación y manejo de valores nulos

  * Nulos críticos → eliminación
  * Nulos no críticos → imputación
* Conversión de columnas de fecha a `datetime`
* (En progreso) Validación de IDs e integridad referencial

### 3️⃣ Load *(próximamente)*

* Carga de datos limpios a:

  * Archivos CSV
  * Base de datos PostgreSQL

---

## 📊 Datos Utilizados

* **ventas.csv**: registros de ventas (fecha, producto, cliente, vendedor, monto)
* **productos.csv**: catálogo de productos
* **clientes.csv**: información de clientes
* **vendedores.csv**: equipo de ventas

---

## 🚀 Cómo Ejecutar el Pipeline

```bash
git clone https://github.com/mfrann/ventas-data-pipeline.git
cd ventas-data-pipeline
pip install -r requirements.txt
python etl/main.py
```

---

## 🛠️ Tecnologías

* Python 3.8+
* Pandas
* SQLAlchemy
* Git / GitHub

---

## 📈 Estado del Proyecto

✔ Extract implementado
✔ Transform (limpieza y tipos de datos)
🚧 Transform (validación de integridad referencial)
🚧 Load (PostgreSQL / CSV)

---

## 👤 Autor

**Martin Caycho**
GitHub: [@mfrann](https://github.com/mfrann)

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.

---

⭐ Si te gusta el proyecto, dale una estrella en GitHub
