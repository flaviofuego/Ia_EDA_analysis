# =============================================================================
# Dockerfile para compilar y ejecutar el clasificador KNN en C
# =============================================================================
# 
# Universidad del Norte - Inteligencia Artificial
# Proyecto: Predicción de Desempeño en Inglés - Saber 11
# 
# Este Dockerfile crea un contenedor que compila y ejecuta la implementación
# en C del algoritmo K-Nearest Neighbors (KNN) para clasificación.
# 
# =============================================================================

FROM gcc:13.2.0

# Instalar herramientas necesarias
RUN apt-get update && apt-get install -y \
    make \
    && rm -rf /var/lib/apt/lists/*

# Crear directorios de trabajo
WORKDIR /app

# Copiar código fuente
COPY src/ /app/src/

# Crear directorios para datos y resultados
RUN mkdir -p /app/data /app/results

# Compilar el programa
WORKDIR /app/src
RUN make clean || true
RUN make

# Copiar el ejecutable al directorio principal
RUN cp knn_classifier /app/

# Volver al directorio principal
WORKDIR /app

# Script de ejecución por defecto
CMD ["./knn_classifier", "data/train_data_c.csv", "data/test_data_c.csv", "5"]
