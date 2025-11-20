# 💾 DATOS DEL PROYECTO

Esta carpeta contiene todos los datasets y archivos de datos procesados del proyecto.

---

## 📂 Estructura

### 📦 raw/ - Datasets Originales
Contiene el dataset original sin procesar:

**dataset_saber11_reducido_estratificado.xlsx**
- **Fuente**: Instituto Colombiano para la Evaluación (ICFES)
- **Periodo**: 2019-2020
- **Tamaño**: 217,581 observaciones × 51 variables
- **Tipo**: Pruebas Saber 11° - Resultados académicos
- **Variable Objetivo**: `DESEMP_INGLES` (5 clases: A-, A1, A2, B1, B+)
- **Características**:
  - Demográficas: 9 variables
  - Escolares: 14 variables
  - Socioeconómicas: 11 variables
  - Desempeño académico: 6 variables (puntajes)
  - Objetivo: 1 variable (nivel de inglés)

**dataset_reducido_info.txt**
- Información sobre el dataset reducido
- Metodología de muestreo estratificado
- Distribución de clases

---

### 🔄 processed/ - Datos Procesados
Contiene checkpoints y datos intermedios generados durante el análisis:

**Checkpoints JSON** (generados por Sección 1):
- Contienen variables seleccionadas
- Resultados de análisis de correlación
- Configuraciones de preprocesamiento

**Archivos esperados:**
- `X_train.csv` - Features de entrenamiento (152,306 × 20)
- `X_test.csv` - Features de prueba (65,275 × 20)
- `y_train.csv` - Labels de entrenamiento
- `y_test.csv` - Labels de prueba
- `X_train_pca.csv` - Features con PCA (8 componentes)
- `X_test_pca.csv` - Features con PCA
- `*.pkl` - Modelos y objetos de preprocesamiento

---

## 📊 Características del Dataset

### Variable Objetivo
**DESEMP_INGLES**: Nivel de desempeño en inglés
- **A-**: Pre-A1 (nivel más bajo)
- **A1**: Básico
- **A2**: Pre-intermedio
- **B1**: Intermedio
- **B+**: Intermedio-Alto (nivel más alto)

### Desbalanceo de Clases
```
A-: 49.52% (107,784 estudiantes)
A1: 28.16% (61,261 estudiantes)
A2: 14.59% (31,744 estudiantes)
B1:  6.39% (13,902 estudiantes)
B+:  1.34% (2,890 estudiantes)
```
**Ratio de desbalanceo**: 37:1 (A- vs B+)

---

## 🔑 Variables Principales

### Top 10 Variables Influyentes (por correlación/asociación):

**Numéricas:**
1. PUNT_GLOBAL - Puntaje global del examen
2. PUNT_C_NATURALES - Ciencias naturales
3. PUNT_LECTURA_CRITICA - Lectura crítica
4. PUNT_SOCIALES_CIUDADANAS - Sociales y ciudadanas
5. PUNT_MATEMATICAS - Matemáticas

**Categóricas:**
1. FAMI_TIENEINTERNET - Acceso a internet (V de Cramér: 0.326)
2. FAMI_TIENECOMPUTADOR - Acceso a computador (V: 0.325)
3. COLE_NATURALEZA - Tipo de colegio (V: 0.306)
4. FAMI_TIENEAUTOMOVIL - Propiedad de vehículo (V: 0.263)
5. FAMI_EDUCACIONMADRE - Nivel educativo de la madre (V: 0.225)

---

## 📈 Preprocesamiento Aplicado

### 1. Imputación de Valores Faltantes
- **Numéricas**: Mediana
- **Categóricas**: Moda

**Variables con missing values:**
- FAMI_TIENEINTERNET: 5.61%
- FAMI_EDUCACIONMADRE: 5.52%
- FAMI_TIENEAUTOMOVIL: 3.26%
- FAMI_TIENECOMPUTADOR: 3.06%

### 2. Codificación
- **Binarias**: Label Encoding
- **Multicategóricas**: One-Hot Encoding
- **Target**: Label Encoding (0-4)

### 3. Normalización
- **Método**: StandardScaler
- **Variables**: Solo numéricas
- **Resultado**: Media=0, Std=1

### 4. Reducción Dimensional
- **Método**: PCA
- **Componentes óptimas**: 8 (explican 91.13% varianza)
- **Reducción**: 60% (de 20 a 8 features)

---

## 🎯 División Train/Test

**Configuración:**
- **Split**: 70% train / 30% test
- **Método**: Estratificado por DESEMP_INGLES
- **Random State**: 42 (reproducibilidad)

**Tamaños:**
- Training: 152,306 observaciones
- Test: 65,275 observaciones

**Verificación:**
```
Clase  Original_%  Train_%  Test_%
A-     49.52       49.52    49.52
A1     28.16       28.16    28.15
A2     14.59       14.59    14.60
B+     1.34        1.34     1.34
B1     6.39        6.39     6.39
```
✅ Distribución idéntica en train/test

---

## 💻 Datos para Implementación C

**Subconjunto reducido** (Sección 6):
- `train_data_c.csv`: 5,000 observaciones (muestreo estratificado)
- `test_data_c.csv`: 2,000 observaciones (muestreo estratificado)
- Mantiene distribución de clases
- Usado para validar implementación KNN en C

---

## 📝 Uso Recomendado

1. **Dataset original**: Usa `raw/dataset_saber11_reducido_estratificado.xlsx`
2. **Datos preprocesados**: Usa archivos en `processed/` (*.csv, *.pkl)
3. **Para C**: Usa `train_data_c.csv` y `test_data_c.csv`
4. **Para reproducir**: Ejecuta notebooks en orden (1 → 2 → 3 → 4 → 5 → 6)

---

## ⚠️ Notas Importantes

- **NUNCA modificar** el dataset original en `raw/`
- Los archivos en `processed/` son regenerables ejecutando los notebooks
- Todos los archivos CSV usan encoding UTF-8
- Los archivos pickle son específicos de la versión de Python/scikit-learn usada

---

**Generado automáticamente - Proyecto IA Universidad del Norte**
