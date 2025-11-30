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
COPY knn_classifier.c /app/

# Crear directorios para datos y resultados
RUN mkdir -p /app/data /app/results

# Compilar el programa directamente con gcc
RUN gcc -Wall -Wextra -O2 -std=c99 -o knn_classifier knn_classifier.c -lm

# Script de ejecución por defecto
CMD ["./knn_classifier", "data/train_data_c.csv", "data/test_data_c.csv", "5"]
