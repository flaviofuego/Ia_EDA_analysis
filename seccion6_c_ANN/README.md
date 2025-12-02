# Perceptrón Multicapa (MLP) en C

Implementación desde cero de un Perceptrón Multicapa para clasificación multiclase del desempeño en inglés (Pruebas Saber 11).

## Estructura del Proyecto

```plant
seccion6_c_ANN/
├── include/           # Headers (.h)
│   ├── types.h
│   ├── activation.h
│   ├── data_utils.h
│   ├── mlp_core.h
│   ├── forward.h
│   ├── backward.h
│   ├── optimizer.h
│   ├── training.h
│   ├── prediction.h
│   └── metrics.h
├── src/               # Implementaciones (.c)
│   ├── activation.c
│   ├── data_utils.c
│   ├── mlp_core.c
│   ├── forward.c
│   ├── backward.c
│   ├── optimizer.c
│   ├── training.c
│   ├── prediction.c
│   ├── metrics.c
│   └── main.c
├── data/              # Datasets
│   └── dataset_processed.csv
├── Makefile
└── README.md
```

## Requisitos

- GCC (C compiler)
- Make
- Librería matemática estándar (libm)

## Compilación

```bash
make clean
make
```

Esto generará el ejecutable en `bin/mlp_classifier`.

## Uso

### Sistema de Configuración

El modelo soporta configuración mediante archivos de texto. Ver [CONFIG_GUIDE.md](CONFIG_GUIDE.md) para detalles completos.

### Ejecución básica

```bash
make run                    # Configuración por defecto
make run-fast              # Configuración rápida (50 epochs)
make run-accurate          # Configuración precisa (200 epochs)
```

### Con archivo de configuración personalizado

```bash
make run-custom CONFIG=mi_config.txt
```

### Override de parámetros desde línea de comandos

```bash
./bin/mlp_classifier data/dataset_processed.csv --config mlp_config.txt --lr 0.02
./bin/mlp_classifier data/dataset_processed.csv --epochs 75 --batch 128
```

### Opciones disponibles

- `--config <archivo>`: Archivo de configuración (default: mlp_config.txt)
- `--epochs <n>`: Número de épocas (override)
- `--batch <n>`: Tamaño de mini-batch (override)
- `--lr <f>`: Learning rate inicial (override)
- `--hidden <n,n>`: Neuronas por capa oculta (override)

## Arquitectura del Modelo

**Configuración por defecto:**

- Input: 10 features (variables seleccionadas)
- Hidden 1: 20 neuronas (ReLU)
- Hidden 2: 10 neuronas (ReLU)
- Output: 5 neuronas (Softmax)

**Optimizaciones:**

- Inicialización He para capas ReLU
- Momentum SGD (β=0.9)
- Regularización L2 (λ=0.0001)
- Learning rate decay exponencial (0.98 por época)
- Early stopping (patience=15)
- Mini-batch training

## Dataset

Formato CSV esperado:

```text
feat1,feat2,feat3,...,feat10,label
0.5,1.2,-0.3,...,0.8,0
...
```

- 10 features numéricas (normalizadas)
- Label: clase 0-4 (correspondiente a A-, A1, A2, B+, B1)

## Métricas de Evaluación

El programa calcula:

- Accuracy global
- Balanced accuracy
- F1-score ponderado
- Precision y Recall (macro)
- Métricas por clase
- Matriz de confusión

## Resultados

Los resultados se guardan automáticamente en la carpeta `tasks/`:

- `tasks/tarea23_resultados_entrenamiento.txt`: Reporte completo con métricas y fragmentos de código

## Características de Implementación

### Módulos Principales

1. **activation.c**: Funciones ReLU, Sigmoid, Tanh, Softmax y derivadas
2. **data_utils.c**: Carga, normalización, split y shuffle de datos
3. **mlp_core.c**: Creación y gestión de la estructura del MLP
4. **forward.c**: Propagación hacia adelante
5. **backward.c**: Retropropagación y cálculo de gradientes
6. **optimizer.c**: Actualización de pesos (SGD, Momentum)
7. **training.c**: Loop de entrenamiento con validación
8. **prediction.c**: Inferencia y predicción batch
9. **metrics.c**: Cálculo de métricas de evaluación

### Optimizaciones de Rendimiento

- Flags de compilación: `-O3 -march=native`
- Operaciones vectorizadas cuando posible
- Gestión eficiente de memoria
- Cálculo numericamente estable de softmax

## Comparación con Implementación en Python

### Script de Comparación Automática

```bash
python3 compare_mlp_implementations.py
```

Este script ejecuta y compara:

1. **C (custom)**: Lee resultados de `tasks/tarea23_resultados_entrenamiento.txt`
2. **Scikit-learn**: MLPClassifier con arquitectura idéntica
3. **TensorFlow/Keras**: Sequential MLP (si está instalado)
4. **PyTorch**: Custom nn.Module (si está instalado)

**Salidas generadas:**

- Tabla comparativa en consola (Accuracy, Bal.Acc, F1-Score, Tiempo, Epochs)
- Reporte detallado en `comparacion_completa.txt`
- Análisis de speedup (C vs Python frameworks)

**Resultados típicos:**

| Framework | Accuracy | Tiempo | Speedup vs C |
|-----------|----------|--------|--------------|
| C (custom) | 92.42% | 2.03s | 1.00x |
| Scikit-learn | 92.41% | 6.61s | 0.31x (3.25x más lento) |
| PyTorch | 92.52% | 30.12s | 0.07x (14.84x más lento) |

**Ventajas de C:**

- 3-15x más rápido que Python frameworks
- ~15-40x menos consumo de memoria
- Sin dependencias externas (solo libc/libm)
- Ideal para producción y sistemas embebidos

**Ventajas de Python:**

- Desarrollo más rápido
- Ecosistema rico (visualización, debugging)
- Soporte GPU (TensorFlow/PyTorch)
- Accuracy ligeramente superior (~0.1-0.5%)

Ver también: `tarea24_comparacion_resultados.txt` para análisis detallado

## Limitaciones

- Arquitectura fija (modificable en código)
- Solo optimizador SGD con momentum
- Sin soporte para GPU
- Dataset debe caber en memoria RAM

## Autores

Universidad del Norte - Ingeniería de Sistemas
Curso: Inteligencia Artificial (ELP 8012)
Noviembre 2025
