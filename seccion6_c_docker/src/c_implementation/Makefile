# =============================================================================
# Makefile para compilar el clasificador KNN en C usando Docker
# =============================================================================
# 
# Universidad del Norte - Inteligencia Artificial
# Proyecto: Predicción de Desempeño en Inglés - Saber 11
# 
# Uso:
#   make build    - Construye la imagen Docker
#   make run      - Ejecuta el clasificador con Docker
#   make test     - Ejecuta con diferentes valores de k
#   make clean    - Limpia archivos compilados y contenedores
# 
# =============================================================================

# Configuración Docker
DOCKER_IMAGE = knn-classifier
DOCKER_COMPOSE = docker-compose

# Compilador y flags (para compilación local si es necesario)
CC = gcc
CFLAGS = -Wall -Wextra -O2 -std=c99
LDFLAGS = -lm

# Nombre del ejecutable
TARGET = knn_classifier

# Archivos fuente
SOURCES = knn_classifier.c
OBJECTS = $(SOURCES:.c=.o)

# Archivos de datos (generados desde Python)
TRAIN_DATA = train_data_c.csv
TEST_DATA = test_data_c.csv

# Valor por defecto de K
K = 5

# =============================================================================
# Reglas de compilación usando Docker
# =============================================================================

# Regla por defecto: construir y ejecutar con Docker
all: build run

# Construir la imagen Docker
build:
	@echo "🐳 Construyendo imagen Docker..."
	@$(DOCKER_COMPOSE) build
	@echo "✅ Imagen construida exitosamente!"

# Ejecutar el clasificador con Docker
run:
	@echo ""
	@echo "🚀 Ejecutando KNN Classifier en Docker..."
	@echo ""
	@$(DOCKER_COMPOSE) up

# Ejecutar con diferentes valores de k
test:
	@echo ""
	@echo "🧪 Probando con diferentes valores de K en Docker..."
	@echo ""
	@echo "=== K=3 ==="
	@$(DOCKER_COMPOSE) run --rm knn ./knn_classifier data/train_data_c.csv data/test_data_c.csv 3 | grep "Accuracy:" || true
	@echo ""
	@echo "=== K=5 ==="
	@$(DOCKER_COMPOSE) run --rm knn ./knn_classifier data/train_data_c.csv data/test_data_c.csv 5 | grep "Accuracy:" || true
	@echo ""
	@echo "=== K=7 ==="
	@$(DOCKER_COMPOSE) run --rm knn ./knn_classifier data/train_data_c.csv data/test_data_c.csv 7 | grep "Accuracy:" || true
	@echo ""
	@echo "=== K=9 ==="
	@$(DOCKER_COMPOSE) run --rm knn ./knn_classifier data/train_data_c.csv data/test_data_c.csv 9 | grep "Accuracy:" || true
	@echo ""

# Limpiar contenedores y volúmenes Docker
clean:
	@echo "🧹 Limpiando contenedores Docker..."
	@$(DOCKER_COMPOSE) down -v
	@echo "✅ Limpieza completada"

# Limpiar todo incluyendo la imagen Docker
cleanall: clean
	@echo "🧹 Eliminando imagen Docker..."
	@docker rmi $(DOCKER_IMAGE) 2>/dev/null || true
	@echo "✅ Limpieza completa"

# =============================================================================
# Reglas de compilación local (sin Docker)
# =============================================================================

# Compilar localmente (requiere gcc instalado)
local: $(TARGET)
	@echo ""
	@echo "✅ Compilación local exitosa!"
	@echo "Ejecuta con: ./$(TARGET) $(TRAIN_DATA) $(TEST_DATA) $(K)"
	@echo ""

# Compilar el ejecutable (local)
$(TARGET): $(OBJECTS)
	@echo "🔗 Enlazando..."
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)

# Compilar archivos objeto (local)
%.o: %.c
	@echo "🔨 Compilando $<..."
	$(CC) $(CFLAGS) -c $<

# Ejecutar localmente
local-run: local
	@echo ""
	@echo "🚀 Ejecutando KNN Classifier (local)..."
	@echo ""
	@./$(TARGET) $(TRAIN_DATA) $(TEST_DATA) $(K)

# Limpiar archivos compilados locales
local-clean:
	@echo "🧹 Limpiando archivos compilados locales..."
	rm -f $(OBJECTS) $(TARGET)
	rm -f resultados_knn_c.txt
	@echo "✅ Limpieza local completada"

# =============================================================================
# Utilidades
# =============================================================================

# Ayuda
help:
	@echo ""
	@echo "Makefile para KNN Classifier con Docker"
	@echo "========================================"
	@echo ""
	@echo "Comandos Docker (Recomendado):"
	@echo "  make          - Construir y ejecutar con Docker"
	@echo "  make build    - Construir imagen Docker"
	@echo "  make run      - Ejecutar con Docker"
	@echo "  make test     - Probar con diferentes valores de K"
	@echo "  make clean    - Limpiar contenedores Docker"
	@echo "  make cleanall - Limpiar todo incluyendo imagen"
	@echo ""
	@echo "Comandos locales (requiere gcc):"
	@echo "  make local     - Compilar localmente"
	@echo "  make local-run - Compilar y ejecutar localmente"
	@echo "  make local-clean - Limpiar compilación local"
	@echo ""
	@echo "Otros:"
	@echo "  make check    - Verificar archivos de datos"
	@echo "  make info     - Información del sistema"
	@echo "  make help     - Mostrar esta ayuda"
	@echo ""

# Verificar que existen los archivos de datos
check:
	@echo "Verificando archivos de datos..."
	@if [ -f "$(TRAIN_DATA)" ]; then \
		echo "✅ $(TRAIN_DATA) encontrado"; \
	else \
		echo "❌ $(TRAIN_DATA) no encontrado"; \
		echo "   Ejecuta el notebook de Python para generar los datos"; \
	fi
	@if [ -f "$(TEST_DATA)" ]; then \
		echo "✅ $(TEST_DATA) encontrado"; \
	else \
		echo "❌ $(TEST_DATA) no encontrado"; \
		echo "   Ejecuta el notebook de Python para generar los datos"; \
	fi

# Información del sistema
info:
	@echo ""
	@echo "Información del sistema:"
	@echo "========================"
	@echo "Compilador: $(CC)"
	@echo "Versión:"
	@$(CC) --version | head -1
	@echo "Flags: $(CFLAGS)"
	@echo "Librerías: $(LDFLAGS)"
	@echo ""

# Evitar conflictos con archivos que se llamen igual que las reglas
.PHONY: all build run test clean cleanall local local-run local-clean help check info
