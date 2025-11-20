# 🚀 QUICK START - SECCIÓN 6

## ⚡ Ejecución Rápida

### Opción 1: Usar Makefile (Recomendado)

```bash
cd /path/to/Ia_EDA_analysis

# Compilar
make

# Ejecutar con k=5
make run

# Probar diferentes valores de k
make test

# Ver ayuda
make help
```

### Opción 2: Compilación Manual

```bash
# Compilar
gcc -o knn_classifier knn_classifier.c -lm -O2 -Wall -Wextra -std=c99

# Ejecutar
./knn_classifier train_data_c.csv test_data_c.csv 5
```

---

## 📋 Pre-requisitos

1. **Generar datos de entrenamiento y prueba**:
   - Abrir `notebooks/seccion6.ipynb`
   - Ejecutar hasta la celda de Tarea 23 que genera los CSV
   - Esto crea `train_data_c.csv` y `test_data_c.csv`

2. **Compilador C**:
   - Linux: `sudo apt install build-essential`
   - Mac: `xcode-select --install`
   - Windows: MinGW o WSL

---

## 📊 Output Esperado

```
╔═══════════════════════════════════════════════════════════════════╗
║    K-NEAREST NEIGHBORS (KNN) CLASSIFIER - IMPLEMENTACIÓN EN C     ║
╚═══════════════════════════════════════════════════════════════════╝

✅ Datos de entrenamiento cargados: 1000 muestras, 10 features
✅ Datos de prueba cargados: 300 muestras
✅ Modelo entrenado
[==================================================] 100%
✅ Predicciones completadas en ~1-2 segundos

Accuracy: 85-90% (típico)

╔════════════════════════════════════════╗
║      MATRIZ DE CONFUSIÓN               ║
╚════════════════════════════════════════╝
[matriz 5x5 con predicciones]

╔════════════════════════════════════════╗
║      MÉTRICAS POR CLASE                ║
╚════════════════════════════════════════╝
[Precision, Recall, F1-Score por clase]
```

---

## 🎯 Parámetros

```bash
./knn_classifier <train.csv> <test.csv> <k>
```

- `train.csv`: Archivo de entrenamiento
- `test.csv`: Archivo de prueba  
- `k`: Número de vecinos (recomendado: 3, 5, 7, 9)

---

## 📁 Archivos Clave

```
Ia_EDA_analysis/
├── knn_classifier.c          # Implementación (595 líneas)
├── Makefile                  # Compilación fácil
├── notebooks/seccion6.ipynb  # Notebook completo
├── train_data_c.csv          # Datos (generado por notebook)
├── test_data_c.csv           # Datos (generado por notebook)
└── README_SECCION6.md        # Documentación completa
```

---

## 🔧 Troubleshooting

### Error: "No se pudo abrir train_data_c.csv"
**Solución**: Ejecutar notebook primero para generar los CSV

### Error: "undefined reference to sqrt"
**Solución**: Agregar `-lm` a la compilación

### Error: "gcc: command not found"
**Solución**: Instalar GCC (ver pre-requisitos arriba)

---

## 📚 Más Información

- Documentación completa: `README_SECCION6.md`
- Resumen ejecutivo: `TRABAJO_COMPLETADO_SECCION6.md`
- Notebook completo: `notebooks/seccion6.ipynb`

---

## ⭐ Características

- ✅ Implementación KNN desde cero (sin librerías ML)
- ✅ 595 líneas de C profesional
- ✅ Evaluación completa (accuracy, confusion matrix, per-class metrics)
- ✅ Comparación con sklearn
- ✅ Análisis de optimizaciones (100-500x potencial)

---

**Universidad del Norte** - Inteligencia Artificial  
**Proyecto Final** - Predicción de Desempeño en Inglés

---
