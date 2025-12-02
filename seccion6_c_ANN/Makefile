CC = gcc
CFLAGS = -Wall -Wextra -O3 -march=native -I./include
LDFLAGS = -lm
SRC_DIR = src
INC_DIR = include
OBJ_DIR = obj
BIN_DIR = bin

TARGET = $(BIN_DIR)/mlp_classifier

SOURCES = $(wildcard $(SRC_DIR)/*.c)
OBJECTS = $(SOURCES:$(SRC_DIR)/%.c=$(OBJ_DIR)/%.o)

all: directories $(TARGET)

directories:
	@mkdir -p $(OBJ_DIR) $(BIN_DIR)

$(TARGET): $(OBJECTS)
	$(CC) $(OBJECTS) $(LDFLAGS) -o $@
	@echo "Build completo: $@"

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -rf $(OBJ_DIR) $(BIN_DIR)
	rm -f tasks/tarea23_resultados_entrenamiento.txt
	@echo "Limpieza completada"

run: $(TARGET)
	./$(TARGET) data/dataset_processed.csv

run-custom: $(TARGET)
	@echo "Ejecutando con configuración personalizada: $(CONFIG)"
	./$(TARGET) data/dataset_processed.csv --config $(CONFIG)

# Configuraciones predefinidas
run-fast: $(TARGET)
	@echo "Ejecutando con configuración RÁPIDA..."
	./$(TARGET) data/dataset_processed.csv --config mlp_config_fast.txt

run-accurate: $(TARGET)
	@echo "Ejecutando con configuración PRECISA..."
	./$(TARGET) data/dataset_processed.csv --config mlp_config_accurate.txt

# Override de parámetros individuales
run-lr: $(TARGET)
	@echo "Ejecutando con learning rate personalizado: $(LR)"
	./$(TARGET) data/dataset_processed.csv --lr $(LR)

test: $(TARGET)
	./$(TARGET) data/dataset_processed.csv --epochs 50 --batch 32 --lr 0.015

compare:
	@echo "Ejecutando comparación C vs Python..."
	cd compare && python3 compare_mlp_implementations.py

visualize:
	@echo "Generando visualizaciones de comparación..."
	cd compare && python3 generate_visualizations.py
	@echo "✓ Gráficas de comparación guardadas en graficas/"

visualize-training:
	@echo "Generando visualizaciones de entrenamiento..."
	cd compare && python3 visualize_training.py
	@echo "✓ Gráficas de entrenamiento guardadas en graficas/"

visualize-all: visualize visualize-training
	@echo "✓ Todas las visualizaciones generadas"

full:
	@echo "🔄 Iniciando pipeline completo..."
	@echo ""
	@echo "Paso 1: Limpieza y recompilación..."
	@$(MAKE) clean
	@$(MAKE) directories $(TARGET)
	@echo ""
	@echo "✓ Compilación completa realizada"
	@echo ""
	@echo "Paso 2: Comparación (incluye ejecución de C)..."
	@$(MAKE) compare
	@echo ""
	@echo "Paso 3: Generación de visualizaciones..."
	@$(MAKE) visualize
	@echo ""
	@echo "✅ Pipeline completo ejecutado: recompilación + comparación + visualizaciones"

# Variables para configuración personalizada
CONFIG ?= mlp_config.txt
LR ?= 0.01
EPOCHS ?= 100
BATCH ?= 64

.PHONY: all clean directories run run-custom run-fast run-accurate run-lr test compare visualize visualize-training visualize-all full
