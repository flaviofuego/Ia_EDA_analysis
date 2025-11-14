# Sección 4: Aprendizaje Supervisado

## 📋 Descripción General

Esta sección implementa **5 tareas evaluables** (Tareas 13-17) del proyecto final de Inteligencia Artificial, enfocadas en el entrenamiento, evaluación y optimización de modelos de clasificación supervisada.

## 🎯 Objetivo

Predecir el nivel de desempeño en inglés (`DESEMP_INGLES`) de estudiantes utilizando múltiples algoritmos de machine learning, comparando su rendimiento y optimizando sus hiperparámetros.

## 📊 Estructura del Notebook

El notebook `seccion4.ipynb` contiene **9 celdas** organizadas de la siguiente manera:

### 1. Header (Markdown)
- Información del proyecto y objetivos

### 2. Configuración Inicial
- Importación de bibliotecas
- Configuración de random_state y estilos
- Definición de constantes

### 3. Carga de Datos
- Carga de train/test split de Sección 2
- Carga de objetos de preprocesamiento
- Verificación de distribución de clases

### 4. TAREA 13: Entrenamiento de Modelos
Implementa **5 modelos de clasificación**:
- ✅ Decision Tree Classifier
- ✅ Random Forest Classifier (100 árboles)
- ✅ Logistic Regression (multinomial)
- ✅ Support Vector Machine (RBF kernel)
- ✅ K-Nearest Neighbors (k=7)

**Salidas**:
- Modelos entrenados
- Predicciones en conjunto de test
- Tiempos de entrenamiento

### 5. TAREA 14: Comparación de Modelos
Evalúa todos los modelos con múltiples métricas:
- Accuracy, Precision, Recall, F1-Score
- Matrices de confusión (normalizadas)
- Classification reports detallados
- Visualizaciones comparativas

**Archivos generados**:
- `model_comparison_metrics.png`
- `confusion_matrices.png`

### 6. TAREA 15: Validación Cruzada
Análisis de estabilidad con 5-Fold Stratified CV:
- Distribución de scores por fold
- Análisis de overfitting (Train-Test Gap)
- Métricas de estabilidad (desviación estándar)
- Comparación de varianza

**Archivos generados**:
- `cross_validation_analysis.png`

### 7. TAREA 16: Ajuste de Hiperparámetros
Optimización de los mejores modelos:
- **Grid Search** para Random Forest y Logistic Regression
- **Random Search** para Decision Tree
- Comparación Before/After
- Guardado de modelos optimizados

**Archivos generados**:
- `hyperparameter_tuning_comparison.png`
- `tuned_models.pkl`

### 8. TAREA 17: Feature Importance
Análisis de importancia de variables:
- **Random Forest**: Importancia basada en reducción de impureza
- **Logistic Regression**: Análisis de coeficientes por clase
- **Decision Tree**: Visualización de estructura del árbol
- **Consenso**: Ranking agregado de features

**Archivos generados**:
- `feature_importance_random_forest.png`
- `feature_coefficients_logistic.png`
- `decision_tree_structure.png`
- `feature_importance_comparison.png`
- `feature_importance_analysis.pkl`

### 9. Resumen Final
- Tabla resumen de todas las tareas
- Conclusiones y hallazgos clave
- Recomendaciones para Sección 5
- Guardado de resultados completos

**Archivos generados**:
- `seccion4_complete_results.pkl`
- `resumen_seccion4.txt`

## 🔧 Requisitos Previos

### Archivos Necesarios
El notebook requiere que **Sección 2** haya sido ejecutada previamente para generar:
- `train_test_split.pkl` - División train/test estratificada
- `preprocessing_objects.pkl` - Encoders, scalers, mapeos
- `pca_models.pkl` - Modelos PCA (opcional)

### Bibliotecas Python
```python
pandas
numpy
matplotlib
seaborn
scikit-learn
scipy
pickle
json
```

## ▶️ Cómo Ejecutar

### Opción 1: Jupyter Notebook
```bash
cd notebooks/
jupyter notebook seccion4.ipynb
```
Ejecutar todas las celdas en orden: `Cell → Run All`

### Opción 2: JupyterLab
```bash
cd notebooks/
jupyter lab seccion4.ipynb
```

### Opción 3: VS Code
Abrir `seccion4.ipynb` con la extensión de Jupyter en VS Code

## 📈 Resultados Esperados

### Métricas Típicas
- **Accuracy**: 0.45 - 0.55 (problema multiclase desafiante)
- **F1-Score**: 0.44 - 0.54
- **Tiempo de entrenamiento**: 5-120 segundos según modelo

### Modelos con Mejor Rendimiento
Típicamente:
1. **Random Forest**: Balance entre precisión y estabilidad
2. **Logistic Regression**: Rápido y interpretable
3. **Decision Tree**: Interpretable pero propenso a overfitting

### Insights Comunes
- Clases extremas (A-, B+) son más distinguibles
- Traslape significativo entre clases intermedias (A1, A2, B1)
- 10-15 features explican 90% de la importancia
- Puntuaciones de pruebas SABER 11 son las features más importantes

## 📁 Archivos Generados

| Archivo | Descripción | Tamaño Aprox. |
|---------|-------------|---------------|
| `model_comparison_metrics.png` | Gráficos comparativos de métricas | ~500KB |
| `confusion_matrices.png` | Matrices de confusión de todos los modelos | ~800KB |
| `cross_validation_analysis.png` | Análisis de CV y estabilidad | ~600KB |
| `hyperparameter_tuning_comparison.png` | Comparación antes/después tuning | ~400KB |
| `feature_importance_*.png` | Visualizaciones de importancia | ~500KB c/u |
| `tuned_models.pkl` | Modelos optimizados | ~50MB |
| `feature_importance_analysis.pkl` | Resultados de análisis | ~500KB |
| `seccion4_complete_results.pkl` | Todos los resultados | ~100MB |
| `resumen_seccion4.txt` | Resumen textual | ~5KB |

## ⚠️ Consideraciones Importantes

### Rendimiento
- **SVM**: Usa muestra de 20,000 observaciones por eficiencia
- **Grid Search**: Puede tardar 10-30 minutos según configuración
- **Random Forest**: Usa n_jobs=-1 para paralelización

### Memoria
- Dataset completo: ~217K filas requiere ~2GB RAM
- Modelos entrenados: ~500MB adicionales
- Se recomienda mínimo 4GB RAM disponible

### Reproducibilidad
- Todos los modelos usan `random_state=42`
- Resultados deberían ser idénticos en múltiples ejecuciones
- Pequeñas variaciones pueden ocurrir por paralelización

## 🐛 Troubleshooting

### Error: "FileNotFoundError: train_test_split.pkl"
**Solución**: Ejecutar primero `seccion2.ipynb` para generar archivos de preprocesamiento

### Error: "MemoryError"
**Solución**: 
- Reducir tamaño de muestra para SVM
- Disminuir n_estimators de Random Forest
- Ejecutar en entorno con más RAM

### Error: "ConvergenceWarning" en Logistic Regression
**Solución**: Aumentar `max_iter` a 2000 o más

### Ejecución muy lenta
**Solución**:
- Reducir iteraciones de Grid/Random Search
- Usar muestras más pequeñas
- Verificar que n_jobs=-1 esté funcionando

## 📚 Referencias

### Algoritmos Implementados
- Scikit-learn Documentation: https://scikit-learn.org/
- Decision Trees: https://scikit-learn.org/stable/modules/tree.html
- Random Forests: https://scikit-learn.org/stable/modules/ensemble.html
- SVM: https://scikit-learn.org/stable/modules/svm.html

### Métricas y Evaluación
- Classification Metrics: https://scikit-learn.org/stable/modules/model_evaluation.html
- Cross-Validation: https://scikit-learn.org/stable/modules/cross_validation.html

## 👥 Autor

**Proyecto Final - Inteligencia Artificial ELP 8012**  
Universidad del Norte - Ingeniería de Sistemas  
Profesor: Eduardo Zurek, Ph.D.

## 📝 Notas de Versión

**Versión 1.0** (Noviembre 2024)
- ✅ Implementación completa de 5 tareas (13-17)
- ✅ 5 modelos de clasificación
- ✅ Validación cruzada estratificada
- ✅ Optimización de hiperparámetros
- ✅ Análisis exhaustivo de feature importance
- ✅ Visualizaciones publication-ready
- ✅ Código modular y bien documentado

---

## 🚀 Próximos Pasos

Después de completar esta sección, continuar con:
- **Sección 5**: Evaluación e Interpretación
  - Comparación supervisado vs no supervisado
  - Técnicas de mejora (SMOTE, Ensemble, Feature Engineering)
  - Discusión crítica y aplicabilidad real

- **Sección 6**: Implementación en C
  - Selección de algoritmo para implementar
  - Diseño de estructuras de datos
  - Código C con entrenamiento y predicción
  - Comparación con versión Python
