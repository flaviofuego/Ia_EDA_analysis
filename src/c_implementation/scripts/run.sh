#!/bin/bash
# =============================================================================
# Script para ejecutar el clasificador KNN en Docker
# =============================================================================

# Valor de K (por defecto 5)
K_VALUE=${1:-5}

echo "🚀 Ejecutando KNN Classifier en C con K=$K_VALUE..."
echo ""

# Verificar que Docker está instalado
if ! command -v docker &> /dev/null; then
    echo "❌ Error: Docker no está instalado"
    echo "   Instala Docker desde: https://docs.docker.com/get-docker/"
    exit 1
fi

# Verificar que existen los archivos de datos
if [ ! -f "data/train_data_c.csv" ]; then
    echo "❌ Error: data/train_data_c.csv no encontrado"
    echo "   Ejecuta el notebook de Python para generar los datos"
    exit 1
fi

if [ ! -f "data/test_data_c.csv" ]; then
    echo "❌ Error: data/test_data_c.csv no encontrado"
    echo "   Ejecuta el notebook de Python para generar los datos"
    exit 1
fi

# Crear carpeta de resultados si no existe
mkdir -p results

# Ejecutar el contenedor
docker run --rm \
  -v "$(pwd)/data:/app/data:ro" \
  -v "$(pwd)/results:/app/results:rw" \
  knn_classifier_c \
  sh -c "
    echo '🚀 Iniciando KNN Classifier en C...' &&
    echo '📊 Parámetros: K=$K_VALUE' &&
    echo '' &&
    ./knn_classifier data/train_data_c.csv data/test_data_c.csv $K_VALUE | tee results/output.txt &&
    echo '' &&
    echo '✅ Resultados guardados en results/output.txt'
  "

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Ejecución completada"
    echo "📄 Resultados: results/output.txt"
    echo ""
else
    echo ""
    echo "❌ Error durante la ejecución"
    exit 1
fi
