# 🎓 PROYECTO FINAL - INTELIGENCIA ARTIFICIAL
## Análisis y Predicción de Desempeño en Inglés - Pruebas Saber 11

---

## 📋 INFORMACIÓN GENERAL

**Estudiantes**: Flavio Arregoces, Cristian Gonzales  
**Universidad**: Universidad del Norte - Ingeniería de Sistemas  
**Profesor**: Eduardo Zurek, Ph.D.  
**Curso**: Inteligencia Artificial (ELP 8012)  
**Fecha de Entrega**: 29 de noviembre, 2025  
**Valor**: 25% de la nota final

---

## 🎯 OBJETIVO DEL PROYECTO

Aplicar técnicas de aprendizaje automático supervisado y no supervisado para explorar, modelar y evaluar el dataset de resultados de Pruebas Saber 11, prediciendo el nivel de desempeño en inglés (DESEMP_INGLES) y demostrando comprensión algorítmica mediante implementación en lenguaje C.

**Variable Objetivo**: `DESEMP_INGLES` (5 clases: A-, A1, A2, B1, B+)

---

## 📂 ESTRUCTURA DEL PROYECTO

```
proyecto_saber11/
│
├── README.md                                          # Este archivo
├── dataset_saber11_reducido_estratificado.csv        # Dataset (217K filas)
│
├── NOTEBOOKS (Ejecutar en este orden):
│   ├── PROYECTO_SABER11_PARTE_1_SECCION_1.py        # Tareas 1-3
│   ├── PROYECTO_SABER11_PARTE_2_SECCION_1_TAREAS_4_5.py  # Tareas 4-5
│   ├── PROYECTO_SABER11_SECCION_2_PREPROCESAMIENTO.py    # Tareas 6-8
│   ├── PROYECTO_SABER11_SECCION_3_NO_SUPERVISADO.py      # Tareas 9-12
│   ├── PROYECTO_SABER11_SECCION_4_SUPERVISADO.py         # Tareas 13-17
│   ├── PROYECTO_SABER11_SECCION_5_EVALUACION.py          # Tareas 18-20
│   └── PROYECTO_SABER11_SECCION_6_IMPLEMENTACION_C.py    # Tareas 21-25
│
├── CHECKPOINTS (Generados automáticamente):
│   ├── checkpoint_seccion1_tareas1-3.json
│   ├── checkpoint_seccion1_completa.json
│   ├── variables_seleccionadas.txt
│   └── [otros checkpoints por sección]
│
└── IMPLEMENTACIÓN EN C:
    ├── modelo_knn.c                                  # Implementación de KNN en C
    ├── funciones_auxiliares.c                        # Funciones de utilidad
    ├── main.c                                        # Programa principal
    └── README_C.md                                   # Instrucciones de compilación
```

---

## 🚀 GUÍA DE EJECUCIÓN RÁPIDA

### 1. Requisitos Previos

```bash
# Python 3.8+
pip install pandas numpy matplotlib seaborn scikit-learn scipy imbalanced-learn xgboost
```

### 2. Preparar el Dataset

- Coloca el archivo `dataset_saber11_reducido_estratificado.csv` en el directorio de trabajo
- Alternativamente, usa el dataset completo y ejecuta el código de estratificación de la Fase 1

### 3. Ejecutar las Tareas en Orden

**OPCIÓN A: Jupyter Notebook** (Recomendado)
```bash
# Convierte los archivos .py a .ipynb o copia el código en celdas
jupyter notebook
```

**OPCIÓN B: Python Scripts**
```bash
python PROYECTO_SABER11_PARTE_1_SECCION_1.py
python PROYECTO_SABER11_PARTE_2_SECCION_1_TAREAS_4_5.py
# ... y así sucesivamente
```

**OPCIÓN C: Todo en uno**
```bash
# Concatena todos los archivos en un solo notebook
cat PROYECTO_SABER11_*.py > PROYECTO_COMPLETO.py
```

---

## 📊 DESCRIPCIÓN DE CADA SECCIÓN

### ✅ SECCIÓN 1: COMPRENSIÓN DE DATOS (Tareas 1-5)

**Archivos**: `PARTE_1_SECCION_1.py` + `PARTE_2_SECCION_1_TAREAS_4_5.py`

- **Tarea 1**: Descripción completa del dataset (fuente, dominio, variables, problema)
- **Tarea 2**: Formulación de 7 hipótesis de predicción basadas en teoría educativa
- **Tarea 3**: EDA completo (missing values, outliers, distribuciones)
- **Tarea 4**: Análisis de correlación/asociación (Pearson, Spearman, Cramér's V)
- **Tarea 5**: Visualizaciones multivariadas (scatter plots, boxplots, heatmaps, pair plots)

**Outputs**: 
- `checkpoint_seccion1_completa.json`
- `variables_seleccionadas.txt` (top 15 variables influyentes)
- Múltiples visualizaciones

**Tiempo estimado**: 15-20 minutos

---

### 🔧 SECCIÓN 2: PREPROCESAMIENTO (Tareas 6-8)

**Archivo**: `PROYECTO_SABER11_SECCION_2_PREPROCESAMIENTO.py`

- **Tarea 6**: Tratamiento de missing values, codificación categóricas, normalización
- **Tarea 7**: División train/test (70/30) estratificada
- **Tarea 8**: PCA con análisis de varianza explicada

**Outputs**:
- `X_train.csv`, `X_test.csv`, `y_train.csv`, `y_test.csv`
- `scaler.pkl`, `encoder.pkl`, `pca_model.pkl`
- Análisis de componentes principales

**Tiempo estimado**: 10-15 minutos

---

### 🔍 SECCIÓN 3: APRENDIZAJE NO SUPERVISADO (Tareas 9-12)

**Archivo**: `PROYECTO_SABER11_SECCION_3_NO_SUPERVISADO.py`

- **Tarea 9**: Clustering (K-means, DBSCAN, Jerárquico)
- **Tarea 10**: Determinación de k óptimo (Elbow, Silhouette)
- **Tarea 11**: Visualización 2D/3D y relación con variable objetivo
- **Tarea 12**: t-SNE/UMAP para identificar separaciones entre clases

**Outputs**:
- `cluster_labels.csv`
- Visualizaciones de clusters
- Métricas de clustering

**Tiempo estimado**: 15-20 minutos

---

### 🤖 SECCIÓN 4: APRENDIZAJE SUPERVISADO (Tareas 13-17)

**Archivo**: `PROYECTO_SABER11_SECCION_4_SUPERVISADO.py`

- **Tarea 13**: Entrenar múltiples modelos (Random Forest, XGBoost, Logistic Regression, SVM, KNN)
- **Tarea 14**: Comparación con métricas completas
- **Tarea 15**: Validación cruzada (5-fold)
- **Tarea 16**: Grid Search para hiperparámetros
- **Tarea 17**: Feature importance

**Outputs**:
- `modelos_entrenados.pkl`
- `resultados_comparacion.csv`
- `best_model.pkl`
- Matriz de confusión y curvas ROC

**Tiempo estimado**: 20-30 minutos

---

### 📈 SECCIÓN 5: EVALUACIÓN E INTERPRETACIÓN (Tareas 18-20)

**Archivo**: `PROYECTO_SABER11_SECCION_5_EVALUACION.py`

- **Tarea 18**: Comparación supervisado vs no supervisado
- **Tarea 19**: Mejoras metodológicas:
  - SMOTE para balanceo
  - Ensemble methods (Voting, Stacking)
  - Feature engineering
  - Métricas adicionales (Balanced Accuracy, Cohen's Kappa)
- **Tarea 20**: Discusión crítica y conclusiones

**Outputs**:
- `modelo_mejorado.pkl`
- `reporte_final.txt`
- Análisis comparativo completo

**Tiempo estimado**: 15-20 minutos

---

### 💻 SECCIÓN 6: IMPLEMENTACIÓN EN C (Tareas 21-25)

**Archivo**: `PROYECTO_SABER11_SECCION_6_IMPLEMENTACION_C.py` + archivos `.c`

- **Tarea 21**: Selección y justificación de algoritmo (KNN)
- **Tarea 22**: Diseño de estructuras y funciones (pseudocódigo)
- **Tarea 23**: Implementación completa en C
- **Tarea 24**: Evaluación y comparación con Python
- **Tarea 25**: Optimización y reflexión técnica

**Outputs**:
- `modelo_knn.c`, `funciones_auxiliares.c`, `main.c`
- `train_data_c.csv`, `test_data_c.csv`
- `resultados_comparacion_python_c.txt`
- Ejecutable compilado: `./knn_classifier`

**Compilación**:
```bash
gcc -o knn_classifier modelo_knn.c funciones_auxiliares.c main.c -lm
./knn_classifier train_data_c.csv test_data_c.csv
```

**Tiempo estimado**: 30-40 minutos

---

## 📝 NOTAS IMPORTANTES

### 🔑 Variables Clave del Proyecto

- **Variable Objetivo**: `DESEMP_INGLES` (A-, A1, A2, B1, B+)
- **Desafío Principal**: Alto desbalanceo de clases (ratio 37:1)
- **Dataset**: 217,581 observaciones × 51 variables
- **Random State**: 42 (para reproducibilidad)

### ⚙️ Configuraciones Importantes

```python
# Parámetros globales usados en todo el proyecto
RANDOM_STATE = 42
TARGET_COLUMN = 'DESEMP_INGLES'
TEST_SIZE = 0.30
CV_FOLDS = 5
```

### 📊 Métricas de Evaluación

- **Accuracy** (baseline: 49.5%)
- **F1-Score** macro y weighted
- **Precision** y **Recall** por clase
- **Balanced Accuracy** (importante por desbalanceo)
- **Cohen's Kappa**
- **Confusion Matrix**
- **ROC-AUC** (multiclass OvR)

---

## 🎨 VISUALIZACIONES GENERADAS

El proyecto genera más de 30 visualizaciones incluyendo:

✅ Distribuciones de variables  
✅ Análisis de outliers (boxplots)  
✅ Matrices de correlación (heatmaps)  
✅ Scatter plots multivariados  
✅ Pair plots  
✅ Análisis de componentes principales  
✅ Visualizaciones de clusters (2D y 3D)  
✅ Curvas de aprendizaje  
✅ Matrices de confusión  
✅ Curvas ROC multiclass  
✅ Feature importance  

---

## 🐛 TROUBLESHOOTING

### Problema: "FileNotFoundError: dataset_saber11_reducido_estratificado.csv"
**Solución**: Asegúrate de que el archivo CSV esté en el mismo directorio que los scripts, o actualiza la ruta en el código:
```python
df = pd.read_csv('ruta/completa/al/dataset.csv')
```

### Problema: "ImportError: No module named 'imbalanced-learn'"
**Solución**: 
```bash
pip install imbalanced-learn
```

### Problema: Código muy lento al ejecutar
**Solución**: Reduce el tamaño del dataset para pruebas:
```python
df = df.sample(n=10000, random_state=42)  # Usar solo 10K filas para pruebas
```

### Problema: Memoria insuficiente
**Solución**: Ejecuta el código por secciones y libera memoria:
```python
import gc
del variable_grande
gc.collect()
```

---

## 📚 RECURSOS ADICIONALES

- **Documentación ICFES**: https://www.icfes.gov.co/
- **Scikit-learn**: https://scikit-learn.org/
- **Pandas**: https://pandas.pydata.org/
- **Seaborn**: https://seaborn.pydata.org/

---

## ✅ CHECKLIST DE ENTREGA

Antes de entregar, asegúrate de tener:

- [ ] Todos los archivos `.py` o notebook `.ipynb` ejecutables
- [ ] Código C compilable y funcional
- [ ] README.md (este archivo)
- [ ] Repositorio GitHub con documentación
- [ ] Presentación en PowerPoint (20 min aprox.)
- [ ] Todos los outputs guardados (checkpoints, modelos, gráficos)

---


## 📄 LICENCIA

Este proyecto es parte de un trabajo académico para la Universidad del Norte.
Desarrollado en Noviembre 2025.

---

