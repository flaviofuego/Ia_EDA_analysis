# =============================================================================
# Makefile para compilar el clasificador KNN en C
# =============================================================================
# 
# Universidad del Norte - Inteligencia Artificial
# Proyecto: Predicción de Desempeño en Inglés - Saber 11
# 
# Uso:
#   make          - Compila el programa
#   make run      - Compila y ejecuta con datos de ejemplo
#   make clean    - Limpia archivos compilados
#   make test     - Ejecuta con diferentes valores de k
# 
# =============================================================================

# Compilador y flags
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
# Reglas de compilación
# =============================================================================

# Regla por defecto: compilar
all: $(TARGET)
	@echo ""
	@echo "✅ Compilación exitosa!"
	@echo "Ejecuta con: ./$(TARGET) $(TRAIN_DATA) $(TEST_DATA) $(K)"
	@echo ""

# Compilar el ejecutable
$(TARGET): $(OBJECTS)
	@echo "🔗 Enlazando..."
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)

# Compilar archivos objeto
%.o: %.c
	@echo "🔨 Compilando $<..."
	$(CC) $(CFLAGS) -c $<

# Compilar y ejecutar
run: $(TARGET)
	@echo ""
	@echo "🚀 Ejecutando KNN Classifier..."
	@echo ""
	@./$(TARGET) $(TRAIN_DATA) $(TEST_DATA) $(K)

# Ejecutar con diferentes valores de k
test: $(TARGET)
	@echo ""
	@echo "🧪 Probando con diferentes valores de K..."
	@echo ""
	@echo "=== K=3 ==="
	@./$(TARGET) $(TRAIN_DATA) $(TEST_DATA) 3 | grep "Accuracy:"
	@echo ""
	@echo "=== K=5 ==="
	@./$(TARGET) $(TRAIN_DATA) $(TEST_DATA) 5 | grep "Accuracy:"
	@echo ""
	@echo "=== K=7 ==="
	@./$(TARGET) $(TRAIN_DATA) $(TEST_DATA) 7 | grep "Accuracy:"
	@echo ""
	@echo "=== K=9 ==="
	@./$(TARGET) $(TRAIN_DATA) $(TEST_DATA) 9 | grep "Accuracy:"
	@echo ""

# Limpiar archivos compilados
clean:
	@echo "🧹 Limpiando archivos compilados..."
	rm -f $(OBJECTS) $(TARGET)
	rm -f resultados_knn_c.txt
	@echo "✅ Limpieza completada"

# Limpiar todo incluyendo archivos de datos
cleanall: clean
	@echo "🧹 Limpiando archivos de datos..."
	rm -f $(TRAIN_DATA) $(TEST_DATA)
	@echo "✅ Limpieza completa"

# Ayuda
help:
	@echo ""
	@echo "Makefile para KNN Classifier"
	@echo "============================"
	@echo ""
	@echo "Comandos disponibles:"
	@echo "  make          - Compilar el programa"
	@echo "  make run      - Compilar y ejecutar"
	@echo "  make test     - Probar con diferentes valores de K"
	@echo "  make clean    - Limpiar archivos compilados"
	@echo "  make cleanall - Limpiar todo incluyendo datos"
	@echo "  make help     - Mostrar esta ayuda"
	@echo ""
	@echo "Uso personalizado:"
	@echo "  ./$(TARGET) <train.csv> <test.csv> <k>"
	@echo ""
	@echo "Ejemplo:"
	@echo "  ./$(TARGET) train_data_c.csv test_data_c.csv 5"
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
.PHONY: all run test clean cleanall help check info
