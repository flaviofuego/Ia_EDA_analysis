# 🚀 SECCIÓN 6: GUÍA RÁPIDA - Implementación en C con Docker

## 📋 Resumen Ejecutivo

La Sección 6 implementa el algoritmo K-Nearest Neighbors (KNN) en lenguaje C puro, containerizado con Docker para máxima portabilidad y facilidad de uso.

**Tiempo estimado**: 15-20 minutos (incluyendo construcción de Docker)

---

## ⚡ Inicio Rápido (3 pasos)

### 1. Generar Datos desde Python

```bash
cd notebooks
jupyter notebook seccion6.ipynb
# Ejecutar celdas de TAREA 23 para generar train_data_c.csv y test_data_c.csv
```

### 2. Ejecutar con Docker Compose

```bash
cd ../seccion6_c_docker
docker-compose up --build
```

### 3. Ver Resultados

```bash
cat results/output.txt
```

**¡Listo!** 🎉

---

## 🎯 ¿Qué hace esta sección?

### Tareas Implementadas

- **TAREA 21**: Selección y justificación del algoritmo (KNN elegido)
- **TAREA 22**: Diseño de estructuras de datos y funciones
- **TAREA 23**: Implementación completa en C (595 líneas)
- **TAREA 24**: Evaluación y comparación con Python/sklearn
- **TAREA 25**: Análisis de limitaciones y optimizaciones

### Estructura del Proyecto

```
seccion6_c_docker/
├── Dockerfile              # ✅ Imagen Docker (gcc:13.2.0)
├── docker-compose.yml      # ✅ Orquestación simplificada
├── README.md              # ✅ Documentación completa
├── src/
│   ├── knn_classifier.c   # ✅ Implementación KNN (595 líneas)
│   └── Makefile           # ✅ Script de compilación
├── data/
│   ├── train_data_c.csv   # ⬅️ Generado desde Python
│   └── test_data_c.csv    # ⬅️ Generado desde Python  
├── results/
│   └── output.txt         # ➡️ Resultados de ejecución
└── scripts/
    ├── build.sh           # 🔧 Construir imagen Docker
    └── run.sh             # 🚀 Ejecutar contenedor
```

---

## 🐳 Opciones de Ejecución

### Opción A: Docker Compose (Recomendado)

```bash
cd seccion6_c_docker

# Con K=5 (por defecto)
docker-compose up --build

# Con K personalizado
K_VALUE=7 docker-compose up

# Limpiar
docker-compose down
```

### Opción B: Scripts Auxiliares

```bash
cd seccion6_c_docker

# Construir imagen
./scripts/build.sh

# Ejecutar con K=5
./scripts/run.sh

# Ejecutar con K=7
./scripts/run.sh 7
```

### Opción C: Docker Manual

```bash
cd seccion6_c_docker

# Construir
docker build -t knn_classifier_c .

# Ejecutar
docker run --rm \
  -v $(pwd)/data:/app/data:ro \
  -v $(pwd)/results:/app/results:rw \
  knn_classifier_c
```

### Opción D: Compilación Local (Sin Docker)

```bash
cd seccion6_c_docker/src

# Compilar
make

# Ejecutar
./knn_classifier ../data/train_data_c.csv ../data/test_data_c.csv 5

# Limpiar
make clean
```

---

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

---

## 🔧 Troubleshooting

### ❌ "No se pudo abrir el archivo train_data_c.csv"

**Solución**: 
```bash
# Ejecutar notebook de Python primero
cd notebooks
jupyter notebook seccion6.ipynb
# Ejecutar TAREA 23 para generar los CSV
```

### ❌ "docker: command not found"

**Solución**: Instalar Docker
- **Windows**: [Docker Desktop](https://docs.docker.com/desktop/install/windows-install/)
- **Mac**: [Docker Desktop](https://docs.docker.com/desktop/install/mac-install/)
- **Linux**: `sudo apt install docker.io docker-compose`

### ❌ "permission denied while trying to connect to Docker"

**Solución** (Linux):
```bash
sudo usermod -aG docker $USER
# Cerrar sesión y volver a entrar
```

### ⚠️ "WARNING: The K_VALUE variable is not set"

**Solución**: Especificar K_VALUE:
```bash
K_VALUE=5 docker-compose up
```

---

## 🎓 Ventajas del Enfoque Docker

| Aspecto | Sin Docker | Con Docker |
|---------|------------|------------|
| **Instalación** | Instalar GCC, Make, libs | Solo Docker |
| **Portabilidad** | Diferencias entre OS | Funciona igual en todos |
| **Reproducibilidad** | Versión de compilador varía | Siempre gcc:13.2.0 |
| **Limpieza** | Archivos .o, binarios | Todo dentro del contenedor |
| **Profesionalismo** | Enfoque tradicional | Enfoque moderno (DevOps) |

---

## 📝 Checklist de Ejecución

- [ ] Docker instalado y funcionando
- [ ] Ejecutar notebook `seccion6.ipynb` hasta TAREA 23
- [ ] Verificar que `data/train_data_c.csv` y `data/test_data_c.csv` existen
- [ ] Ejecutar `docker-compose up --build`
- [ ] Ver resultados en `results/output.txt`
- [ ] Continuar con TAREA 24 en el notebook para comparación

---

## 🔗 Enlaces Útiles

- **Documentación Completa**: `seccion6_c_docker/README.md`
- **Código Fuente C**: `seccion6_c_docker/src/knn_classifier.c`
- **Notebook**: `notebooks/seccion6.ipynb`
- **Dockerfile**: `seccion6_c_docker/Dockerfile`
- **Docker Compose**: `seccion6_c_docker/docker-compose.yml`

---

## 💡 Tips Pro

1. **Múltiples valores de K**:
   ```bash
   for k in 3 5 7 9 11; do
       echo "Testing K=$k"
       K_VALUE=$k docker-compose up 2>&1 | grep "Accuracy:"
   done
   ```

2. **Ver logs en tiempo real**:
   ```bash
   docker-compose up | tee realtime_output.txt
   ```

3. **Ejecutar sin rebuild**:
   ```bash
   docker-compose up  # Sin --build si ya está construido
   ```

4. **Limpiar todo**:
   ```bash
   docker-compose down
   docker rmi knn_classifier_c
   docker system prune
   ```

---

## 📈 Comparación Python vs C

| Métrica | Python (sklearn) | C (Manual) |
|---------|-----------------|------------|
| **Líneas de Código** | 3 | 595 |
| **Accuracy** | ~85% | ~85% (similar) |
| **Velocidad** | Optimizado (KD-Tree) | Básico (fuerza bruta) |
| **Memoria** | ~100-500 MB | ~1-10 MB |
| **Facilidad de Uso** | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| **Valor Educativo** | ⭐⭐ | ⭐⭐⭐⭐⭐ |

**Conclusión**: Python para producción, C para aprendizaje profundo.

---

**Universidad del Norte** - Ingeniería de Sistemas  
**Curso**: Inteligencia Artificial (ELP 8012)  
**Profesor**: Eduardo Zurek, Ph.D.  
**Estudiantes**: Flavio Arregoces, Cristian Gonzales  
**Fecha**: Noviembre 2025

---

## ✅ ¿Listo para empezar?

```bash
cd seccion6_c_docker && docker-compose up --build
```

🎉 **¡Disfruta tu implementación en C!**
