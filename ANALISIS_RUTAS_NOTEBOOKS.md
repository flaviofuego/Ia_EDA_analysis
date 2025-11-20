# ANÁLISIS DE COMPATIBILIDAD DE RUTAS EN NOTEBOOKS

**Fecha**: 20 de noviembre, 2025
**Estado**: ❌ **LAS RUTAS NO SON COMPATIBLES CON LA NUEVA ESTRUCTURA**

---

## 🎯 PROBLEMA IDENTIFICADO

Después de reorganizar el proyecto en la nueva estructura de carpetas, los notebooks **NO** han sido actualizados para usar las rutas correctas. Todos los notebooks siguen usando rutas relativas que asumen que los archivos están en el mismo directorio que el notebook.

### Nueva Estructura de Carpetas
```
Ia_EDA_analysis/
├── data/
│   ├── raw/                    # Dataset original
│   └── processed/              # Datos procesados, modelos PKL
├── notebooks/                  # NOTEBOOKS ESTÁN AQUÍ
├── outputs/
│   ├── seccion1/              # Outputs de sección 1
│   ├── seccion2/              # Outputs de sección 2
│   ├── seccion3/              # Outputs de sección 3
│   ├── seccion4/              # Outputs de sección 4
│   ├── seccion5/              # Outputs de sección 5
│   └── seccion6/              # Outputs de sección 6
└── src/
```

### Navegación desde notebooks/
Desde la carpeta `notebooks/`, las rutas correctas deben ser:
- Dataset: `../data/raw/dataset_saber11_reducido_estratificado.csv`
- Datos procesados: `../data/processed/X_train.csv`
- Outputs: `../outputs/seccion{X}/archivo.png`

---

## 📋 ANÁLISIS POR NOTEBOOK

### ❌ seccion1.ipynb

**PROBLEMAS ENCONTRADOS:**

| Línea (aprox) | Código Actual | Código Correcto |
|---------------|---------------|-----------------|
| ~105 | `pd.read_csv('dataset_saber11_reducido_estratificado.csv')` | `pd.read_csv('../data/raw/dataset_saber11_reducido_estratificado.csv')` |
| ~1436 | `open('checkpoint_seccion1_tareas1-3.json', 'w')` | `open('../outputs/seccion1/checkpoint_seccion1_tareas1-3.json', 'w')` |
| ~3165 | `open('checkpoint_seccion1_completa.json', 'w')` | `open('../outputs/seccion1/checkpoint_seccion1_completa.json', 'w')` |
| Múltiples | `plt.savefig('*.png')` | `plt.savefig('../outputs/seccion1/*.png')` |
| Múltiples | `open('variables_*.txt', 'w')` | `open('../outputs/seccion1/variables_*.txt', 'w')` |

**ARCHIVOS AFECTADOS:**
- Dataset: `dataset_saber11_reducido_estratificado.csv`
- Checkpoints: `checkpoint_seccion1_tareas1-3.json`, `checkpoint_seccion1_completa.json`
- Outputs: `variables_seleccionadas.txt`, `variables_influyentes_top20.txt`
- Visualizaciones: ~15 archivos PNG

---

### ❌ seccion2.ipynb

**PROBLEMAS ENCONTRADOS:**

| Línea (aprox) | Código Actual | Código Correcto |
|---------------|---------------|-----------------|
| ~90 | `pd.read_csv('dataset_saber11_reducido_estratificado.csv')` | `pd.read_csv('../data/raw/dataset_saber11_reducido_estratificado.csv')` |
| ~98 | `open('checkpoint_seccion1_completa.json', 'r')` | `open('../outputs/seccion1/checkpoint_seccion1_completa.json', 'r')` |
| Múltiples | `to_csv('X_train.csv')` | `to_csv('../data/processed/X_train.csv')` |
| Múltiples | `to_csv('y_train.csv')` | `to_csv('../data/processed/y_train.csv')` |
| Múltiples | `open('preprocessing_objects.pkl', 'wb')` | `open('../data/processed/preprocessing_objects.pkl', 'wb')` |
| Múltiples | `open('pca_models.pkl', 'wb')` | `open('../data/processed/pca_models.pkl', 'wb')` |
| Múltiples | `plt.savefig('*.png')` | `plt.savefig('../outputs/seccion2/*.png')` |

**ARCHIVOS AFECTADOS:**
- **Lectura:**
  - Dataset: `dataset_saber11_reducido_estratificado.csv` → `../data/raw/`
  - Checkpoint: `checkpoint_seccion1_completa.json` → `../outputs/seccion1/`

- **Escritura (data/processed/):**
  - `X_train.csv`, `X_test.csv`
  - `y_train.csv`, `y_test.csv`
  - `X_train_pca.csv`, `X_test_pca.csv`
  - `preprocessing_objects.pkl`
  - `train_test_split.pkl`
  - `pca_models.pkl`

- **Escritura (outputs/seccion2/):**
  - ~3 visualizaciones PNG (PCA)

---

### ❌ seccion3.ipynb

**PROBLEMAS ENCONTRADOS (estimados):**

| Operación | Código Actual | Código Correcto |
|-----------|---------------|-----------------|
| Leer datos | `open('train_test_split.pkl', 'rb')` | `open('../data/processed/train_test_split.pkl', 'rb')` |
| Guardar outputs | `plt.savefig('*.png')` | `plt.savefig('../outputs/seccion3/*.png')` |
| Guardar texto | `open('resumen_seccion3.txt', 'w')` | `open('../outputs/seccion3/resumen_seccion3.txt', 'w')` |

**ARCHIVOS AFECTADOS:**
- **Lectura:** `train_test_split.pkl`, `preprocessing_objects.pkl` → `../data/processed/`
- **Escritura:** `resumen_seccion3.txt`, ~8 PNG → `../outputs/seccion3/`

---

### ❌ seccion4.ipynb

**PROBLEMAS ENCONTRADOS:**

| Línea (aprox) | Código Actual | Código Correcto |
|---------------|---------------|-----------------|
| ~131 | `open('train_test_split.pkl', 'rb')` | `open('../data/processed/train_test_split.pkl', 'rb')` |
| ~147 | `open('preprocessing_objects.pkl', 'rb')` | `open('../data/processed/preprocessing_objects.pkl', 'rb')` |
| ~159 | `open('pca_models.pkl', 'rb')` | `open('../data/processed/pca_models.pkl', 'rb')` |
| ~479 | `plt.savefig('model_comparison_metrics.png')` | `plt.savefig('../outputs/seccion4/model_comparison_metrics.png')` |
| ~697 | `plt.savefig('cross_validation_analysis.png')` | `plt.savefig('../outputs/seccion4/cross_validation_analysis.png')` |
| ~1024 | `plt.savefig('hyperparameter_tuning_comparison.png')` | `plt.savefig('../outputs/seccion4/hyperparameter_tuning_comparison.png')` |
| ~1028 | `open('tuned_models.pkl', 'wb')` | `open('../data/processed/tuned_models.pkl', 'wb')` |
| Múltiples | `plt.savefig('*.png')` | `plt.savefig('../outputs/seccion4/*.png')` |

**ARCHIVOS AFECTADOS:**
- **Lectura (data/processed/):**
  - `train_test_split.pkl`
  - `preprocessing_objects.pkl`
  - `pca_models.pkl`

- **Escritura (data/processed/):**
  - `tuned_models.pkl`
  - `feature_importance_analysis.pkl`
  - `seccion4_complete_results.pkl`

- **Escritura (outputs/seccion4/):**
  - `model_comparison_metrics.png`
  - `confusion_matrices.png`
  - `roc_curves_multiclass.png`
  - `cross_validation_analysis.png`
  - `hyperparameter_tuning_comparison.png`
  - `feature_importance_random_forest.png`
  - `feature_coefficients_logistic.png`
  - `decision_tree_structure.png`
  - `feature_importance_comparison.png`
  - `resumen_seccion4.txt`
  - `README_SECCION4.md`

---

### ❌ seccion5.ipynb

**PROBLEMAS ENCONTRADOS (parcialmente mitigados con lógica condicional):**

| Línea (aprox) | Código Actual | Código Correcto |
|---------------|---------------|-----------------|
| ~173-178 | Lógica condicional con rutas incorrectas | `pd.read_csv('../data/raw/dataset_saber11_reducido_estratificado.csv')` |
| Múltiples | `open('train_test_split.pkl', 'rb')` | `open('../data/processed/train_test_split.pkl', 'rb')` |
| Múltiples | `open('seccion4_complete_results.pkl', 'rb')` | `open('../data/processed/seccion4_complete_results.pkl', 'rb')` |
| Múltiples | `plt.savefig('*.png')` | `plt.savefig('../outputs/seccion5/*.png')` |

**NOTA:** Este notebook tiene lógica condicional que intenta buscar archivos en múltiples ubicaciones, pero las rutas siguen siendo incorrectas.

**ARCHIVOS AFECTADOS:**
- **Lectura (data/processed/):**
  - `train_test_split.pkl`
  - `preprocessing_objects.pkl`
  - `seccion4_complete_results.pkl`

- **Escritura (data/processed/):**
  - `modelo_mejorado.pkl`

- **Escritura (outputs/seccion5/):**
  - ~8 visualizaciones PNG
  - `seccion5_reporte_final.txt`
  - `README_SECCION5.md`

---

### ❌ seccion6.ipynb

**PROBLEMAS ENCONTRADOS:**

| Línea (aprox) | Código Actual | Código Correcto |
|---------------|---------------|-----------------|
| ~1455 | Mención de `../datasets/` (ruta obsoleta) | `../data/raw/` |
| ~1546-1549 | `pd.read_csv('X_train.csv')` | `pd.read_csv('../data/processed/X_train.csv')` |
| ~1719 | `open('train_test_split.pkl', 'rb')` | `open('../data/processed/train_test_split.pkl', 'rb')` |
| ~333 | `plt.savefig('tarea21_algorithm_selection.png')` | `plt.savefig('../outputs/seccion6/tarea21_algorithm_selection.png')` |
| ~387 | `open('tarea21_justificacion_algoritmo.txt', 'w')` | `open('../outputs/seccion6/tarea21_justificacion_algoritmo.txt', 'w')` |
| Múltiples | `plt.savefig('*.png')` | `plt.savefig('../outputs/seccion6/*.png')` |
| Múltiples | `open('tarea*.txt', 'w')` | `open('../outputs/seccion6/tarea*.txt', 'w')` |

**ARCHIVOS GENERADOS PARA C (nueva celda):**
```python
# Esta celda genera CSVs para C - las rutas están MAL
train_c.to_csv('seccion6_c_docker/data/train_data_c.csv', index=False)
test_c.to_csv('seccion6_c_docker/data/test_data_c.csv', index=False)

# Debería ser:
train_c.to_csv('../data/processed/train_data_c.csv', index=False)
test_c.to_csv('../data/processed/test_data_c.csv', index=False)
```

**ARCHIVOS AFECTADOS:**
- **Lectura (data/processed/):**
  - `train_test_split.pkl`
  - `X_train.csv`, `X_test.csv`
  - `y_train.csv`, `y_test.csv`

- **Escritura (data/processed/):**
  - `train_data_c.csv`
  - `test_data_c.csv`

- **Escritura (outputs/seccion6/):**
  - `tarea21_algorithm_selection.png`
  - `tarea21_justificacion_algoritmo.txt`
  - `tarea22_diseno_completo.txt`
  - `tarea22_arquitectura_sistema.png`
  - `tarea24_comparison_python_vs_c.png`
  - `tarea24_comparacion_completa.txt`
  - `tarea25_analisis_limitaciones.txt`
  - `tarea25_optimizaciones_comparacion.png`

---

## 📊 RESUMEN DE IMPACTO

### Total de Rutas Incorrectas

| Notebook | Rutas Lectura | Rutas Escritura | Total |
|----------|--------------|----------------|-------|
| seccion1.ipynb | 1 | ~20 | ~21 |
| seccion2.ipynb | 2 | ~12 | ~14 |
| seccion3.ipynb | 2 | ~10 | ~12 |
| seccion4.ipynb | 3 | ~15 | ~18 |
| seccion5.ipynb | 3 | ~12 | ~15 |
| seccion6.ipynb | 4 | ~10 | ~14 |
| **TOTAL** | **15** | **~79** | **~94** |

### Archivos por Destino

**data/raw/** (lectura):
- `dataset_saber11_reducido_estratificado.csv`

**data/processed/** (lectura):
- `checkpoint_seccion1_completa.json` (actualmente en outputs/seccion1/)
- `train_test_split.pkl`
- `preprocessing_objects.pkl`
- `pca_models.pkl`
- `X_train.csv`, `X_test.csv`
- `y_train.csv`, `y_test.csv`
- `seccion4_complete_results.pkl`
- `tuned_models.pkl`

**data/processed/** (escritura):
- Todos los CSVs (train/test)
- Todos los PKL (modelos, preprocesamiento, PCA)
- CSVs para C (train_data_c.csv, test_data_c.csv)

**outputs/seccion{1-6}/** (escritura):
- Todas las visualizaciones PNG
- Todos los archivos de texto (.txt)
- Todos los READMEs
- Todos los checkpoints JSON (seccion1)

---

## 🔧 SOLUCIÓN PROPUESTA

### Opción 1: Actualización Manual (Recomendado)
Actualizar cada notebook línea por línea para usar las rutas correctas. Esto garantiza control total y evita errores.

**Ventajas:**
- Control total sobre cada cambio
- Verificación visual de cada ruta
- Evita errores de reemplazo masivo

**Desventajas:**
- Requiere tiempo (~2-3 horas)
- Propenso a errores humanos

### Opción 2: Script de Reemplazo Automático
Crear un script que actualice todas las rutas automáticamente usando expresiones regulares.

**Ventajas:**
- Rápido (< 5 minutos)
- Consistente

**Desventajas:**
- Riesgo de romper código si hay casos especiales
- Requiere testing exhaustivo

### Opción 3: Función Helper
Agregar una celda al inicio de cada notebook con funciones helper que manejen las rutas:

```python
# Celda 1 de cada notebook
import os

# Configuración de rutas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_RAW = os.path.join(BASE_DIR, 'data', 'raw')
DATA_PROCESSED = os.path.join(BASE_DIR, 'data', 'processed')
OUTPUTS = os.path.join(BASE_DIR, 'outputs', 'seccionX')  # X según notebook

# Funciones helper
def load_dataset():
    return pd.read_csv(os.path.join(DATA_RAW, 'dataset_saber11_reducido_estratificado.csv'))

def load_processed(filename):
    return pd.read_csv(os.path.join(DATA_PROCESSED, filename))

def save_output(filename, **kwargs):
    filepath = os.path.join(OUTPUTS, filename)
    if filename.endswith('.png'):
        plt.savefig(filepath, **kwargs)
    elif filename.endswith('.txt'):
        return open(filepath, 'w', **kwargs)
    # etc...
```

**Ventajas:**
- Rutas centralizadas
- Fácil de mantener
- Portable entre entornos

**Desventajas:**
- Requiere refactorizar todo el código
- Cambios extensos en cada notebook

---

## 🎯 RECOMENDACIÓN

**Opción 1 (Actualización Manual)** es la más recomendada por:

1. **Seguridad**: No hay riesgo de romper código existente
2. **Claridad**: Cada ruta se actualiza explícitamente
3. **Verificación**: Se puede verificar visualmente cada cambio
4. **Aprendizaje**: Permite revisar el código mientras se actualiza

### Plan de Implementación

**Orden de actualización (para minimizar errores):**
1. ✅ seccion1.ipynb - Genera datos base
2. ✅ seccion2.ipynb - Usa datos de sección 1, genera train/test
3. ✅ seccion3.ipynb - Usa datos de sección 2
4. ✅ seccion4.ipynb - Usa datos de sección 2
5. ✅ seccion5.ipynb - Usa datos de secciones 2 y 4
6. ✅ seccion6.ipynb - Usa datos de sección 2

**Tiempo estimado**: 2-3 horas
**Complejidad**: Media
**Riesgo**: Bajo (si se hace cuidadosamente)

---

## 📝 PASOS SIGUIENTES

1. **Decidir enfoque**: Manual, Script, o Helper Functions
2. **Crear backup**: Copiar notebooks antes de modificar
3. **Actualizar notebooks**: Uno por uno, en orden de dependencia
4. **Verificar**: Revisar que todas las rutas sean correctas
5. **Probar**: Ejecutar cada notebook para verificar funcionamiento
6. **Commit**: Guardar cambios en Git con mensaje descriptivo

---

## ⚠️ NOTAS IMPORTANTES

### Carpeta `seccion6_c_docker/data/`

La nueva celda en seccion6.ipynb genera CSVs en:
```
seccion6_c_docker/data/train_data_c.csv
seccion6_c_docker/data/test_data_c.csv
```

Pero esta carpeta YA NO EXISTE en la nueva estructura. El código C está en:
```
src/c_implementation/
```

**Solución:**
1. Generar CSVs en `data/processed/train_data_c.csv`
2. Actualizar `src/c_implementation/` para leer desde la ruta correcta:
   ```bash
   # En Docker o scripts, usar:
   ../data/processed/train_data_c.csv
   ../data/processed/test_data_c.csv
   ```

3. O usar volúmenes Docker para montar `data/processed/` dentro del contenedor

### Ejecución Relativa vs Absoluta

Todos los notebooks asumen ejecución desde la carpeta `notebooks/`. Si se ejecutan desde otra ubicación, las rutas relativas `../` fallarán.

**Solución:**
- Siempre ejecutar notebooks desde Jupyter Lab/VSCode con working directory = `notebooks/`
- O usar `os.path` para rutas absolutas basadas en la ubicación del notebook

---

**Fecha de análisis**: 20 de noviembre, 2025
**Estado**: Pendiente de corrección
**Prioridad**: 🔴 **ALTA** - Los notebooks no funcionarán en la nueva estructura
