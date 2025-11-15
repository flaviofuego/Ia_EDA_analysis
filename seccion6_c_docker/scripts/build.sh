#!/bin/bash
# =============================================================================
# Script para construir la imagen Docker del clasificador KNN
# =============================================================================

echo "🐳 Construyendo imagen Docker para KNN Classifier..."
echo ""

# Verificar que Docker está instalado
if ! command -v docker &> /dev/null; then
    echo "❌ Error: Docker no está instalado"
    echo "   Instala Docker desde: https://docs.docker.com/get-docker/"
    exit 1
fi

# Construir la imagen
docker build -t knn_classifier_c .

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Imagen construida exitosamente: knn_classifier_c"
    echo ""
    echo "Para ejecutar:"
    echo "  ./scripts/run.sh"
    echo ""
else
    echo ""
    echo "❌ Error al construir la imagen"
    exit 1
fi
