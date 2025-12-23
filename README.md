# 📊 Análisis de Ventas con Python y SQL

Proyecto básico de análisis de datos que procesa información de ventas usando **Pandas** y **SQL**.

## 🎯 ¿Qué hace este proyecto?

Toma 4 archivos CSV con datos de ventas y genera:

- ✅ Reporte de productos más vendidos
- ✅ Ventas totales por mes
- ✅ Top 10 mejores clientes
- ✅ Performance de vendedores

## 📁 Archivos del Proyecto

```
ventas-data-pipeline/
├── README.md           # Este archivo
├── requirements.txt    # Librerías necesarias
├── datos/             # Carpeta con los 4 CSVs
│   ├── clientes.csv
│   ├── productos.csv
│   ├── ventas.csv
│   └── vendedores.csv
└── etl.py             # Código principal
```

## 📊 Datos que Usa

- **ventas.csv**: Todas las ventas realizadas (fecha, producto, cantidad, precio)
- **productos.csv**: Catálogo de productos (nombre, categoría, costo)
- **clientes.csv**: Información de clientes (nombre, ciudad, segmento)
- **vendedores.csv**: Equipo de ventas (nombre, sucursal)

## 🚀 Cómo Usar

### 1. Instalar Python

Necesitas Python 3.8 o superior instalado.

### 2. Clonar el proyecto

```bash
git clone https://github.com/mfrann/ventas-data-pipeline.git
cd ventas-data-pipeline
```

### 3. Instalar librerías

```bash
pip install -r requirements.txt
```

### 4. Ejecutar el análisis

```bash
python etl.py
```

¡Listo! El programa te mostrará los resultados en pantalla.

## 🔧 Tecnologías

- **Python 3.8+**
- **Pandas**: Para manipular datos
- **SQLAlchemy**: Para trabajar con SQL

## 📝 Resultados

Después de ejecutar el programa verás:

```
=== TOP 10 PRODUCTOS ===
1. Laptop Dell XPS 13 - $5,460.00
2. Monitor LG 27" - $2,999.94
...

=== VENTAS POR MES ===
Enero 2024: $12,345.50
Febrero 2024: $10,987.30
...

=== TOP CLIENTES ===
1. Juan Pérez - $2,500.00
2. María González - $1,850.00
...
```

## 👤 Autor

**[Martin Caycho]**

- GitHub: [@mfrann](https://github.com/tu-usuario)

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la Licencia MIT.

---

⭐ **Si te gusta el proyecto, dale una estrella en GitHub**
