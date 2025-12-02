# Configuración del Perceptrón Multicapa

Este documento explica cómo usar el sistema de configuración del MLP.

## Archivos de Configuración

El proyecto incluye tres archivos de configuración predefinidos:

### 1. `mlp_config.txt` (Por defecto)
Configuración balanceada para uso general:
- Epochs: 100
- Batch size: 64
- Learning rate: 0.01
- Capas ocultas: 20,10

### 2. `mlp_config_fast.txt`
Configuración rápida para pruebas y desarrollo:
- Epochs: 50
- Batch size: 128 (más rápido)
- Learning rate: 0.02 (convergencia rápida)
- Capas ocultas: 15,8 (red más pequeña)

### 3. `mlp_config_accurate.txt`
Configuración para máxima precisión:
- Epochs: 200
- Batch size: 32 (más estable)
- Learning rate: 0.005 (más preciso)
- Capas ocultas: 30,20,10 (red más profunda)

## Uso desde Make

### Ejecutar con configuración por defecto:
```bash
make run
```

### Ejecutar con configuración rápida:
```bash
make run-fast
```

### Ejecutar con configuración precisa:
```bash
make run-accurate
```

### Ejecutar con archivo de configuración personalizado:
```bash
make run-custom CONFIG=mi_config.txt
```

### Override de parámetros individuales:

**Learning rate:**
```bash
make run-lr LR=0.025
```

**Desde línea de comandos directa:**
```bash
./bin/mlp_classifier data/dataset_processed.csv --lr 0.015 --epochs 75 --batch 128
```

## Formato del Archivo de Configuración

```ini
# Comentarios con #
epochs=100
batch_size=64
learning_rate=0.01
lr_decay=0.98
momentum=0.9
weight_decay=0.0001
early_stopping_patience=15
min_delta=0.001
hidden_layers=20,10
seed=42
verbose=1
```

## Parámetros Disponibles

| Parámetro | Tipo | Descripción | Rango típico |
|-----------|------|-------------|--------------|
| `epochs` | int | Número máximo de épocas | 50-200 |
| `batch_size` | int | Tamaño del mini-batch | 16-128 |
| `learning_rate` | float | Tasa de aprendizaje inicial | 0.001-0.1 |
| `lr_decay` | float | Decaimiento del learning rate | 0.9-0.99 |
| `momentum` | float | Momentum del SGD | 0.8-0.95 |
| `weight_decay` | float | Regularización L2 | 0.00001-0.001 |
| `early_stopping_patience` | int | Epochs sin mejora antes de parar | 10-20 |
| `min_delta` | float | Mejora mínima para early stopping | 0.0001-0.001 |
| `hidden_layers` | string | Neuronas por capa (separadas por coma) | Ejemplo: "20,10" o "30,20,10" |
| `seed` | int | Semilla aleatoria | Cualquier entero |
| `verbose` | int | Nivel de salida (0=silencioso, 1=normal) | 0-1 |

## Crear Tu Propia Configuración

1. Copia uno de los archivos existentes:
```bash
cp mlp_config.txt mi_config.txt
```

2. Edita los parámetros según tus necesidades

3. Ejecuta con tu configuración:
```bash
make run-custom CONFIG=mi_config.txt
```

## Ejemplos de Uso

### Entrenamiento rápido para debugging:
```bash
./bin/mlp_classifier data/dataset_processed.csv --epochs 10 --batch 256
```

### Experimentar con learning rates:
```bash
make run-lr LR=0.001
make run-lr LR=0.01
make run-lr LR=0.1
```

### Red más profunda:
Edita `mlp_config.txt`:
```ini
hidden_layers=40,30,20,10
```

### Experimentación sistemática:
```bash
for lr in 0.001 0.005 0.01 0.05; do
    echo "Testing LR=$lr"
    make run-lr LR=$lr
done
```

## Prioridad de Parámetros

Los parámetros se aplican en el siguiente orden (del más bajo al más alto):

1. Valores por defecto hardcodeados en el código
2. Valores del archivo de configuración
3. Parámetros de línea de comandos (override)

Esto permite tener una configuración base y sobrescribir valores específicos cuando sea necesario.

## Tips de Configuración

### Para convergencia rápida:
- Aumenta `learning_rate` (0.02-0.05)
- Aumenta `batch_size` (128-256)
- Reduce `epochs` (30-50)

### Para máxima precisión:
- Reduce `learning_rate` (0.001-0.005)
- Reduce `batch_size` (16-32)
- Aumenta `epochs` (150-300)
- Aumenta `early_stopping_patience` (20-30)

### Para evitar overfitting:
- Aumenta `weight_decay` (0.0005-0.001)
- Usa `early_stopping_patience` moderado (10-15)
- Considera reducir el tamaño de la red

### Para redes más profundas:
- Reduce `learning_rate` (0.005-0.01)
- Aumenta `weight_decay` ligeramente
- Usa inicialización He (ya implementada)

---

**Universidad del Norte - Ingeniería de Sistemas**  
Curso: Inteligencia Artificial (ELP 8012)  
Sección 6: Implementación de MLP en C
