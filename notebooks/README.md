# 📓 NOTEBOOKS DEL PROYECTO

Esta carpeta contiene los 6 notebooks principales del proyecto de Inteligencia Artificial, organizados por secciones correspondientes a las 25 tareas evaluables.

---

## 📚 Notebooks por Sección

### 📊 seccion1.ipynb - COMPRENSIÓN DE DATOS
**Tareas 1-5** | **Duración estimada**: 15-20 minutos

**Contenido:**
- **Tarea 1**: Descripción completa del dataset (fuente, dominio, variables, problema)
- **Tarea 2**: Formulación de 6 hipótesis de predicción
- **Tarea 3**: EDA completo (missing values, outliers, distribuciones)
  - ✨ **NUEVO**: Pruebas de normalidad (Shapiro-Wilk, KS, D'Agostino-Pearson)
  - ✨ **NUEVO**: Análisis de skewness y kurtosis
- **Tarea 4**: Análisis de correlación/asociación (Pearson, Spearman, Cramér's V)
  - ✨ **NUEVO**: Análisis de multicolinealidad (VIF)
- **Tarea 5**: Visualizaciones multivariadas (scatter, boxplots, heatmaps, pair plots)

**Outputs generados:**
- `outputs/seccion1/checkpoint_seccion1_completa.json`
- `outputs/seccion1/variables_seleccionadas.txt`
- `outputs/seccion1/normality_tests.png` ✨ NUEVO
- `outputs/seccion1/vif_analysis.png` ✨ NUEVO
- Múltiples visualizaciones de EDA

---

### 🔧 seccion2.ipynb - PREPROCESAMIENTO
**Tareas 6-8** | **Duración estimada**: 10-15 minutos

**Contenido:**
- **Tarea 6**: Tratamiento de datos faltantes, codificación categóricas, normalización
- **Tarea 7**: División train/test (70/30) estratificada
- **Tarea 8**: PCA con análisis de varianza explicada

**Outputs generados:**
- `data/processed/X_train.csv`, `X_test.csv`
- `data/processed/y_train.csv`, `y_test.csv`
- `data/processed/preprocessing_objects.pkl`
- `data/processed/pca_models.pkl`
- Visualizaciones de PCA (scree plot, proyecciones 2D/3D)

---

### 🔍 seccion3.ipynb - APRENDIZAJE NO SUPERVISADO
**Tareas 9-12** | **Duración estimada**: 15-20 minutos

**Contenido:**
- **Tarea 9**: Clustering (K-Means, DBSCAN, Jerárquico)
- **Tarea 10**: Determinación de k óptimo (método del codo, silueta)
- **Tarea 11**: Visualización de clusters 2D/3D y relación con variable objetivo
- **Tarea 12**: Reducción dimensional no supervisada (PCA, t-SNE, UMAP)

**Outputs generados:**
- `outputs/seccion3/resumen_seccion3.txt`
- Visualizaciones de clusters
- Métricas de clustering (ARI, NMI, Silhouette)
- Proyecciones t-SNE y UMAP

---

### 🤖 seccion4.ipynb - APRENDIZAJE SUPERVISADO
**Tareas 13-17** | **Duración estimada**: 20-30 minutos

**Contenido:**
- **Tarea 13**: Entrenamiento de 5 modelos (Decision Tree, Random Forest, Logistic Regression, SVM, KNN)
- **Tarea 14**: Comparación con métricas completas
  - ✨ **NUEVO**: Curvas ROC-AUC multiclase (One-vs-Rest)
- **Tarea 15**: Validación cruzada (5-fold) y análisis de estabilidad
- **Tarea 16**: Grid Search para hiperparámetros
- **Tarea 17**: Feature importance y coeficientes

**Outputs generados:**
- `outputs/seccion4/*.png` (9 visualizaciones)
- `outputs/seccion4/roc_curves_multiclass.png` ✨ NUEVO
- `data/processed/modelos_entrenados.pkl`
- `data/processed/best_model.pkl`

---

### 📈 seccion5.ipynb - EVALUACIÓN E INTERPRETACIÓN
**Tareas 18-20** | **Duración estimada**: 15-20 minutos

**Contenido:**
- ✨ **NUEVA SUBSECCIÓN 19.0**: Verificación de data leakage (7 checks sistemáticos)
- **Tarea 18**: Comparación supervisado vs no supervisado
- **Tarea 19**: Mejoras metodológicas
  - ✨ **NUEVO**: Comparación de variantes de SMOTE (6 técnicas)
  - Feature Engineering (PolynomialFeatures)
  - Ensemble Methods (Voting, Stacking)
  - ✨ **NUEVO**: Regularización L1/L2 y Early Stopping
  - Nuevas métricas (Balanced Accuracy, Cohen's Kappa)
- **Tarea 20**: Discusión crítica y conclusiones

**Outputs generados:**
- `outputs/seccion5/*.png` (5 visualizaciones originales)
- `outputs/seccion5/smote_variants_comparison.png` ✨ NUEVO
- `outputs/seccion5/regularization_analysis.png` ✨ NUEVO
- `data/processed/modelo_mejorado.pkl`

---

### 💻 seccion6.ipynb - IMPLEMENTACIÓN EN C
**Tareas 21-25** | **Duración estimada**: 15-20 minutos

**Contenido:**
- **Tarea 21**: Selección y justificación de algoritmo KNN
- **Tarea 22**: Diseño de estructuras y funciones (pseudocódigo)
- ✨ **NUEVA CELDA**: Generación automática de CSVs para C
- **Tarea 23**: Implementación completa en C (701 líneas) - Con Docker
- **Tarea 24**: Evaluación y comparación Python vs C
- **Tarea 25**: Análisis de limitaciones y optimizaciones

**Outputs generados:**
- `outputs/seccion6/*.txt` y `*.png` (8 archivos)
- `data/processed/train_data_c.csv` ✨ NUEVO
- `data/processed/test_data_c.csv` ✨ NUEVO

---

## 🚀 Orden de Ejecución

**IMPORTANTE**: Ejecutar los notebooks en orden:

```
1. seccion1.ipynb  →  Genera variables_seleccionadas.txt
2. seccion2.ipynb  →  Usa variables de sección 1, genera train/test
3. seccion3.ipynb  →  Usa datos de sección 2
4. seccion4.ipynb  →  Usa datos de sección 2
5. seccion5.ipynb  →  Usa modelos de sección 4
6. seccion6.ipynb  →  Genera CSVs y ejecuta código C
```

---

## ⚙️ Configuración Global

**Parámetros consistentes en todos los notebooks:**
```python
RANDOM_STATE = 42
TARGET_COLUMN = 'DESEMP_INGLES'
TEST_SIZE = 0.30
CV_FOLDS = 5
```

---

## 📦 Dependencias

**Librerías requeridas:**
```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy \
            imbalanced-learn xgboost umap-learn plotly statsmodels
```

**Versiones recomendadas:**
- Python: 3.8+
- pandas: 1.3+
- scikit-learn: 1.0+
- numpy: 1.21+

---

## 🎨 Visualizaciones por Notebook

| Notebook | Visualizaciones Generadas | Total |
|----------|--------------------------|-------|
| Sección 1 | ~15 (EDA, correlaciones, normalidad, VIF) | 15+ |
| Sección 2 | ~3 (PCA) | 3 |
| Sección 3 | ~8 (clustering, reducción) | 8 |
| Sección 4 | ~9 (modelos, métricas, ROC-AUC) | 9 |
| Sección 5 | ~8 (comparaciones, mejoras) | 8 |
| Sección 6 | ~4 (comparación C vs Python) | 4 |
| **TOTAL** | | **47+** |

---

## ✨ Nuevas Características (Correcciones Implementadas)

Las siguientes características fueron agregadas en las correcciones:

### Sección 1:
- ✅ Subsección 3.4: Pruebas de normalidad (Shapiro-Wilk, KS, D'Agostino)
- ✅ Subsección 4.5: Análisis VIF para multicolinealidad

### Sección 4:
- ✅ Subsección 14.5: Curvas ROC-AUC multiclase (grid 2×3)

### Sección 5:
- ✅ Subsección 19.0: Verificación de data leakage (7 checks)
- ✅ Subsección 19.2: Comparación SMOTE variants (reemplaza SMOTE básico)
- ✅ Subsección 19.4: Regularización L1/L2 y Early Stopping

### Sección 6:
- ✅ Nueva celda: Generación automática de CSVs para C

**Total de líneas añadidas**: ~750 líneas de código production-ready

---

## 📝 Notas de Ejecución

### Tiempo Total Estimado
- **Ejecución completa**: ~90-120 minutos
- **Por sección**: 10-30 minutos

### Recursos Requeridos
- **RAM**: 8GB mínimo, 16GB recomendado
- **Disco**: ~5GB para datasets y outputs
- **CPU**: Multicore recomendado para modelos

### Reproducibilidad
- Todos los notebooks usan `random_state=42`
- Resultados son 100% reproducibles
- Outputs idénticos en cada ejecución

---

## 🐛 Solución de Problemas

### Problema: "FileNotFoundError: dataset_saber11_reducido_estratificado.csv"
**Solución**:
```python
# Actualizar ruta en el notebook
df = pd.read_csv('../data/raw/dataset_saber11_reducido_estratificado.xlsx')
```

### Problema: "ImportError: No module named 'imbalanced-learn'"
**Solución**:
```bash
pip install imbalanced-learn
```

### Problema: Código muy lento
**Solución**:
```python
# Usar subconjunto para pruebas
df = df.sample(n=10000, random_state=42)
```

---

## 📚 Documentación Adicional

- Ver `outputs/` para archivos generados por cada sección
- Ver `docs/quick-starts/` para guías rápidas
- Ver `docs/reportes/` para análisis completo del proyecto

---

**Generado automáticamente - Proyecto IA Universidad del Norte**
