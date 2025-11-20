# 🐳 Sección 6: Implementación en C con Docker

## 📋 Descripción

Esta carpeta contiene la implementación del algoritmo K-Nearest Neighbors (KNN) en lenguaje C, containerizada con Docker para facilitar la compilación y ejecución independientemente del sistema operativo del usuario.

## 📁 Estructura de Carpetas

```
seccion6_c_docker/
├── Dockerfile              # Imagen Docker para compilar y ejecutar el código C
├── docker-compose.yml      # Orquestación para facilitar la ejecución
├── README.md              # Este archivo
├── src/
│   ├── knn_classifier.c   # Implementación completa del algoritmo KNN
│   └── Makefile           # Script de compilación
├── data/                  # Datos de entrada (generados desde Python)
│   ├── train_data_c.csv   # Datos de entrenamiento
│   └── test_data_c.csv    # Datos de prueba
├── results/               # Resultados de la ejecución
│   └── output.txt         # Salida del programa (métricas, matriz de confusión)
└── scripts/               # Scripts auxiliares
    ├── run.sh            # Script para ejecutar el contenedor
    └── build.sh          # Script para construir la imagen
```

## 🚀 Guía de Uso Rápida

### Requisitos Previos

- Docker instalado ([Instrucciones de instalación](https://docs.docker.com/get-docker/))
- Docker Compose instalado (incluido con Docker Desktop)

### Paso 1: Generar los Datos

Ejecutar el notebook de Python (`seccion6.ipynb`) hasta las celdas que generan:
- `train_data_c.csv`
- `test_data_c.csv`

Estos archivos deben estar en la carpeta `data/`.

### Paso 2: Construir y Ejecutar

**Opción A: Usando Docker Compose (Recomendado)**

```bash
# Construir y ejecutar con K=5 (por defecto)
docker-compose up --build

# Ejecutar con un valor de K personalizado
K_VALUE=7 docker-compose up

# Limpiar contenedores
docker-compose down
```

**Opción B: Usando Docker directamente**

```bash
# Construir la imagen
docker build -t knn_classifier_c .

# Ejecutar el contenedor
docker run --rm \
  -v $(pwd)/data:/app/data:ro \
  -v $(pwd)/results:/app/results:rw \
  knn_classifier_c

# Con valor de K personalizado
docker run --rm \
  -v $(pwd)/data:/app/data:ro \
  -v $(pwd)/results:/app/results:rw \
  knn_classifier_c \
  ./knn_classifier data/train_data_c.csv data/test_data_c.csv 7
```

**Opción C: Usando scripts auxiliares**

```bash
# Construir la imagen
./scripts/build.sh

# Ejecutar con K=5
./scripts/run.sh

# Ejecutar con K=7
./scripts/run.sh 7
```

### Paso 3: Ver Resultados

Los resultados se guardan automáticamente en `results/output.txt` y también se muestran en la consola.

```bash
# Ver resultados
cat results/output.txt

# O directamente en la consola durante la ejecución
```

## 📊 Salida Esperada

```
╔═══════════════════════════════════════════════════════════════════╗
║    K-NEAREST NEIGHBORS (KNN) CLASSIFIER - IMPLEMENTACIÓN EN C     ║
║                                                                    ║
║    Universidad del Norte - Inteligencia Artificial (ELP 8012)     ║
║    Proyecto: Predicción de Desempeño en Inglés - Saber 11         ║
╚═══════════════════════════════════════════════════════════════════╝

Parámetros:
  Archivo de entrenamiento: data/train_data_c.csv
  Archivo de prueba: data/test_data_c.csv
  K (vecinos): 5

📂 Cargando datos de entrenamiento...
✅ Datos de entrenamiento cargados:
  Muestras:        1000
  Features:        10
  Clases:          5

📂 Cargando datos de prueba...
✅ Datos de prueba cargados:
  Muestras:        300
  Features:        10
  Clases:          5

🔧 Creando modelo KNN con k=5...
🎯 Entrenando modelo...
✅ Modelo entrenado

Realizando predicciones...
[==================================================] 100%
✅ Predicciones completadas en 1.23 segundos

╔════════════════════════════════════════╗
║      RESULTADOS GENERALES              ║
╚════════════════════════════════════════╝
  Accuracy:              85.67%
  Total de muestras:     300
  Predicciones correctas: 257
  Predicciones incorrectas: 43

╔════════════════════════════════════════╗
║      MATRIZ DE CONFUSIÓN               ║
╚════════════════════════════════════════╝
         C0   C1   C2   C3   C4  
      -------------------------
C0  |    45    3    2    0    0 
C1  |     2   52    4    2    0 
C2  |     1    5   48    5    1 
C3  |     0    1    4   51    4 
C4  |     0    0    2    3   55 

╔════════════════════════════════════════╗
║      MÉTRICAS POR CLASE                ║
╚════════════════════════════════════════╝
Clase  Precisión  Recall    F1-Score
─────────────────────────────────────────
  0     0.9375    0.9000    0.9184
  1     0.8525    0.8667    0.8596
  2     0.8000    0.8000    0.8000
  3     0.8361    0.8500    0.8430
  4     0.9167    0.9167    0.9167
```

## 🔧 Troubleshooting

### Error: "No se pudo abrir el archivo train_data_c.csv"

**Causa**: Los archivos CSV no están en la carpeta `data/`.

**Solución**: 
1. Ejecutar el notebook de Python (`seccion6.ipynb`)
2. Copiar `train_data_c.csv` y `test_data_c.csv` a la carpeta `data/`

### Error: "docker: command not found"

**Causa**: Docker no está instalado.

**Solución**: Instalar Docker desde https://docs.docker.com/get-docker/

### Error: "permission denied while trying to connect to the Docker daemon"

**Causa**: El usuario no tiene permisos para ejecutar Docker.

**Solución Linux**:
```bash
sudo usermod -aG docker $USER
# Cerrar sesión y volver a entrar
```

### Warning durante compilación

**Causa**: Warnings normales del compilador GCC.

**Solución**: Los warnings no afectan la ejecución. Si deseas suprimirlos, edita el `Makefile` y agrega `-Wno-unused-variable` a `CFLAGS`.

## 📝 Notas Importantes

1. **Volúmenes**: 
   - `data/` se monta como **read-only** (`:ro`) para proteger los datos originales
   - `results/` se monta como **read-write** (`:rw`) para guardar los resultados

2. **Reproducibilidad**: 
   - El contenedor siempre usa la misma versión de GCC (13.2.0)
   - Garantiza resultados consistentes en cualquier sistema operativo

3. **Limpieza**:
   ```bash
   # Eliminar contenedores detenidos
   docker-compose down
   
   # Eliminar imagen
   docker rmi knn_classifier_c
   
   # Eliminar todo (contenedores, imágenes, volúmenes)
   docker system prune -a
   ```

4. **Integración con Notebook**:
   - El notebook de Python puede llamar a los scripts de Docker usando `subprocess`
   - Los resultados se leen desde `results/output.txt`

## 🎓 Ventajas del Enfoque Docker

1. **Portabilidad**: Funciona en Windows, macOS y Linux sin cambios
2. **Reproducibilidad**: Misma versión de compilador para todos
3. **Aislamiento**: No interfiere con el sistema del usuario
4. **Facilidad**: No requiere instalar GCC manualmente
5. **Profesionalismo**: Enfoque moderno usado en la industria

## 💡 Integración con el Notebook

El notebook de Python (`seccion6.ipynb`) incluye celdas para:

1. **Generar datos**: Crear `train_data_c.csv` y `test_data_c.csv`
2. **Ejecutar Docker**: Llamar a `docker-compose up` usando `subprocess`
3. **Leer resultados**: Parsear `results/output.txt` para análisis
4. **Visualizar**: Generar gráficos comparativos Python vs C

Ejemplo de código en el notebook:

```python
import subprocess
import os

# Ejecutar Docker Compose
os.chdir('seccion6_c_docker')
result = subprocess.run(
    ['docker-compose', 'up', '--build'],
    capture_output=True,
    text=True
)

# Leer resultados
with open('results/output.txt', 'r') as f:
    output = f.read()
    print(output)

# Extraer métricas para comparación
# ... (código de parsing)
```

## 📚 Referencias

- **Docker Documentation**: https://docs.docker.com/
- **Docker Compose**: https://docs.docker.com/compose/
- **GCC Docker Image**: https://hub.docker.com/_/gcc

---

**Universidad del Norte** - Ingeniería de Sistemas  
**Curso**: Inteligencia Artificial (ELP 8012)  
**Profesor**: Eduardo Zurek, Ph.D.  
**Estudiantes**: Flavio Arregoces, Cristian Gonzales  
**Fecha**: Noviembre 2025
