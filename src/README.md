# 💻 CÓDIGO FUENTE

Esta carpeta contiene todo el código fuente del proyecto (scripts Python e implementación en C).

---

## 📂 Estructura

### 🐍 python/ - Scripts Python
Scripts auxiliares y herramientas de generación:

**Archivos:**
- `carga_analisis_base.ipynb` - Notebook de carga y análisis preliminar
- `carga_base.ipynb` - Notebook de carga del dataset base
- `seccion2_script.py` - Script de preprocesamiento (Sección 2)
- `generate_section6_complete.py` - Generador completo de Sección 6

**Uso:**
```bash
# Ejecutar script de preprocesamiento
python src/python/seccion2_script.py

# Generar sección 6
python src/python/generate_section6_complete.py
```

---

### 🔧 c_implementation/ - Implementación KNN en C

**Arquitectura Docker:**
```
c_implementation/
├── Dockerfile              # Imagen Docker (gcc:13.2.0)
├── docker-compose.yml      # Orquestación de contenedores
├── .dockerignore          # Archivos excluidos de Docker
├── .gitignore             # Archivos excluidos de Git
├── README.md              # Documentación completa de la implementación
│
├── src/                   # Código fuente C
│   ├── knn_classifier.c   # Implementación KNN (701 líneas)
│   └── Makefile          # Sistema de compilación
│
├── data/                  # Datos para C (generados desde Python)
│   ├── train_data_c.csv  # 5,000 observaciones
│   └── test_data_c.csv   # 2,000 observaciones
│
├── results/               # Resultados de ejecución
│   └── [outputs del programa C]
│
└── scripts/               # Scripts de utilidad
    ├── build.sh          # Construir imagen Docker
    └── run.sh            # Ejecutar contenedor
```

---

## 🎯 Implementación KNN en C (Tarea 23)

### Características Principales

**Algoritmo:** K-Nearest Neighbors (KNN)
- **K óptimo**: 5 vecinos
- **Métrica de distancia**: Euclidiana
- **Método de votación**: Mayoría simple
- **Clases**: 5 (A-, A1, A2, B1, B+)

**Código:**
- **Líneas totales**: 701 líneas de código puro C
- **Funciones**: 12 funciones principales
- **Estructuras de datos**: 4 estructuras (DataPoint, Dataset, Neighbor, KNNModel)

### Funciones Implementadas

**Carga de datos:**
1. `load_dataset()` - Carga CSV y parsea datos
2. `free_dataset()` - Libera memoria
3. `print_dataset_info()` - Muestra información del dataset

**Algoritmo KNN:**
4. `euclidean_distance()` - Calcula distancia entre puntos
5. `compare_neighbors()` - Comparador para qsort
6. `find_k_nearest_neighbors()` - Encuentra k vecinos más cercanos
7. `majority_vote()` - Votación por mayoría
8. `predict()` - Predice clase de una muestra

**Evaluación:**
9. `evaluate_model()` - Calcula accuracy
10. `compute_confusion_matrix()` - Matriz de confusión
11. `print_confusion_matrix()` - Imprime matriz
12. `compute_classification_metrics()` - Precision, Recall, F1-Score

---

## 🐳 Ejecución con Docker (Recomendado)

### Opción 1: Docker Compose (Más fácil)
```bash
cd src/c_implementation
docker-compose up --build
```

### Opción 2: Docker CLI
```bash
cd src/c_implementation

# Construir imagen
docker build -t knn-classifier .

# Ejecutar contenedor
docker run -v $(pwd)/data:/app/data -v $(pwd)/results:/app/results knn-classifier
```

---

## 🔨 Compilación Manual (Sin Docker)

### Requisitos
- GCC 13.2.0 o superior
- Make
- Linux/Unix (recomendado) o WSL en Windows

### Compilación
```bash
cd src/c_implementation/src

# Compilar
make

# Ejecutar
./knn_classifier ../data/train_data_c.csv ../data/test_data_c.csv 5

# Limpiar binarios
make clean
```

---

## 📊 Complejidad del Algoritmo

**Complejidad temporal:**
- **Entrenamiento**: O(1) (solo almacena datos)
- **Predicción (por muestra)**: O(n × d)
  - n = tamaño del training set
  - d = número de features
- **Predicción total**: O(m × n × d)
  - m = tamaño del test set

**Complejidad espacial:**
- **Almacenamiento**: O(n × d)
- **Vecinos temporales**: O(k)

---

## 🎨 Características de la Implementación

### ✅ Implementado

- ✅ Lectura de archivos CSV
- ✅ Parseo de datos numéricos
- ✅ Cálculo de distancia Euclidiana
- ✅ Búsqueda de k vecinos (con qsort)
- ✅ Votación por mayoría
- ✅ Evaluación completa (Accuracy, Precision, Recall, F1-Score)
- ✅ Matriz de confusión
- ✅ Barra de progreso
- ✅ Gestión de memoria (malloc/free)
- ✅ Manejo básico de errores

### 🔧 Optimizaciones Propuestas (Tarea 25)

**Alto impacto (10-100x):**
- KD-Tree para búsqueda de vecinos (O(log n))
- Paralelización con OpenMP (speedup ~8x)

**Impacto medio (2-5x):**
- Partial Heap Sort (solo primeros k vecinos)
- SIMD para distancias (vectorización)
- Memory Pool para allocaciones

**Bajo impacto (1.2-2x):**
- Distance Caching
- Branch prediction hints
- Compiler flags de optimización (-O3)

---

## 📈 Resultados Esperados

**Métricas de desempeño:**
- Accuracy: ~45-50% (dataset desbalanceado)
- Tiempo de ejecución: ~2-5 segundos (5000 train, 2000 test)
- Memoria usada: ~2-3 MB

**Comparación Python vs C:**
- C es ~10-20x más rápido que Python puro
- C usa ~5-10x menos memoria
- Python con sklearn es más rápido (optimizado en C++)

---

## 📝 Notas de Desarrollo

### Decisiones de Diseño

1. **¿Por qué KNN?**
   - Simplicidad conceptual
   - No requiere entrenamiento complejo
   - Implementable en C sin bibliotecas externas
   - Valor educativo alto

2. **¿Por qué k=5?**
   - Balance entre bias y variance
   - Funciona bien para 5 clases
   - Evita empates en votación

3. **¿Por qué qsort?**
   - Biblioteca estándar de C
   - Implementación eficiente
   - No requiere código adicional

### Limitaciones Conocidas

- **MAX_FEATURES**: Limitado a 100 features (constante)
- **Sin normalización**: Los datos deben venir normalizados
- **Sin manejo de missing values**: Los datos deben estar completos
- **Sin paralelización**: Ejecución secuencial

---

## 🚀 Próximos Pasos

Para mejorar la implementación:
1. Implementar KD-Tree
2. Agregar paralelización con OpenMP
3. Optimizar con SIMD
4. Agregar validación cruzada
5. Implementar grid search para k óptimo

---

**Generado automáticamente - Proyecto IA Universidad del Norte**
