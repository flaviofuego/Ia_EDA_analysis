# 📊 OUTPUTS - ARCHIVOS GENERADOS

Esta carpeta contiene todos los archivos generados por cada sección del proyecto (visualizaciones, checkpoints, reportes, análisis).

---

## 📂 Estructura por Sección

### 📍 seccion1/ - Comprensión de Datos (Tareas 1-5)
**Archivos generados:**
- `checkpoint_seccion1_completa.json` - Checkpoint final de la sección
- `checkpoint_seccion1_tareas1-3.json` - Checkpoint parcial
- `variables_seleccionadas.txt` - Top 15 variables para modelado
- `variables_influyentes_top20.txt` - Variables más influyentes

**Visualizaciones esperadas (cuando se ejecute):**
- `normality_tests.png` - Pruebas de normalidad (4 gráficos)
- `vif_analysis.png` - Análisis de multicolinealidad (2 gráficos)
- Distribuciones de variables
- Matrices de correlación
- Scatter plots multivariados

---

### 🔧 seccion2/ - Preprocesamiento (Tareas 6-8)
**Archivos esperados:**
- `X_train.csv`, `X_test.csv` - Datos divididos
- `y_train.csv`, `y_test.csv` - Labels
- `preprocessing_objects.pkl` - Objetos de preprocesamiento
- `train_test_split.pkl` - División train/test
- `pca_models.pkl` - Modelos PCA
- `X_train_pca.csv`, `X_test_pca.csv` - Datos con PCA

**Visualizaciones:**
- Scree plots de PCA
- Proyecciones en componentes principales

---

### 🔍 seccion3/ - Aprendizaje No Supervisado (Tareas 9-12)
**Archivos generados:**
- `resumen_seccion3.txt` - Resumen de resultados
- `cluster_labels.csv` - Etiquetas de clusters

**Visualizaciones esperadas:**
- Visualizaciones 2D/3D de clusters
- Método del codo
- Coeficiente de silueta
- t-SNE y UMAP proyections

---

### 🤖 seccion4/ - Aprendizaje Supervisado (Tareas 13-17)
**Archivos generados:**
- `confusion_matrices.png` - Matrices de confusión de todos los modelos
- `cross_validation_analysis.png` - Análisis de validación cruzada
- `decision_tree_structure.png` - Estructura del árbol de decisión
- `feature_coefficients_logistic.png` - Coeficientes de regresión logística
- `feature_importance_comparison.png` - Comparación de importancia de features
- `feature_importance_random_forest.png` - Importancia en Random Forest
- `hyperparameter_tuning_comparison.png` - Comparación de hiperparámetros
- `model_comparison_metrics.png` - Comparación de métricas
- `resumen_seccion4.txt` - Resumen de resultados
- `README_SECCION4.md` - Documentación de la sección

**Nuevas visualizaciones (correcciones):**
- `roc_curves_multiclass.png` - Curvas ROC-AUC multiclase (grid 2×3)

**Modelos entrenados:**
- `modelos_entrenados.pkl`
- `best_model.pkl`
- `tuned_models.pkl`

---

### 📈 seccion5/ - Evaluación e Interpretación (Tareas 18-20)
**Archivos generados:**
- `tarea18_confusion_matrix_clusters.png` - Matriz de confusión clusters vs clases
- `tarea18_supervised_vs_unsupervised.png` - Comparación supervisado vs no supervisado
- `tarea19_best_model_confusion_matrix.png` - Matriz del mejor modelo
- `tarea19_comparison_all_improvements.png` - Comparación de todas las mejoras
- `seccion5_reporte_final.txt` - Reporte final de la sección
- `README_SECCION5.md` - Documentación de la sección

**Nuevas visualizaciones (correcciones):**
- `smote_variants_comparison.png` - Comparación de variantes de SMOTE (4 gráficos)
- `regularization_analysis.png` - Análisis de regularización L1/L2 (2 gráficos)

**Modelos mejorados:**
- `modelo_mejorado.pkl`
- Resultados de SMOTE, Feature Engineering, Ensemble Methods

---

### 💻 seccion6/ - Implementación en C (Tareas 21-25)
**Archivos generados:**
- `tarea21_algorithm_selection.png` - Visualización de selección de algoritmo
- `tarea21_justificacion_algoritmo.txt` - Justificación detallada
- `tarea22_arquitectura_sistema.png` - Diagrama de arquitectura
- `tarea22_diseno_completo.txt` - Diseño completo (pseudocódigo)
- `tarea24_comparacion_completa.txt` - Comparación Python vs C
- `tarea24_comparison_python_vs_c.png` - Gráfico comparativo
- `tarea25_analisis_limitaciones.txt` - Análisis de limitaciones
- `tarea25_optimizaciones_comparacion.png` - Comparación de optimizaciones

**Datos para C:**
- `train_data_c.csv` - Training set para C (5000 muestras)
- `test_data_c.csv` - Test set para C (2000 muestras)

**Resultados de ejecución C:**
- Outputs del programa KNN en C
- Métricas de desempeño

---

## 📊 Total de Archivos por Sección

| Sección | Archivos Actuales | Visualizaciones | Total |
|---------|------------------|-----------------|-------|
| Sección 1 | 4 | 2+ | 6+ |
| Sección 2 | 0 | 2+ | 2+ |
| Sección 3 | 1 | 5+ | 6+ |
| Sección 4 | 9 | 9 | 18 |
| Sección 5 | 5 | 7+ | 12+ |
| Sección 6 | 8 | 4 | 12 |
| **TOTAL** | **27** | **29+** | **56+** |

---

## 🎨 Visualizaciones Totales del Proyecto

El proyecto genera **47+ visualizaciones profesionales**:
- Sección 1: ~15 visualizaciones (EDA, correlaciones, normalidad, VIF)
- Sección 2: ~3 visualizaciones (PCA)
- Sección 3: ~8 visualizaciones (clustering, reducción dimensional)
- Sección 4: ~9 visualizaciones (modelos, ROC-AUC)
- Sección 5: ~8 visualizaciones (comparaciones, mejoras)
- Sección 6: ~4 visualizaciones (comparación C vs Python)

---

## 📝 Notas

- Los archivos marcados como "esperados" se generarán al ejecutar los notebooks
- Todos los archivos usan `random_state=42` para reproducibilidad
- Las imágenes se guardan en formato PNG a 300 DPI
- Los modelos se guardan en formato pickle (.pkl)

---

**Generado automáticamente - Proyecto IA Universidad del Norte**
