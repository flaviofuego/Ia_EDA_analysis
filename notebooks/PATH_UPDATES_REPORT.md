# NOTEBOOK PATH UPDATES REPORT

**Date**: November 20, 2025
**Task**: Update all file I/O paths to use new folder structure
**Status**: ✅ **COMPLETED**

---

## 📊 SUMMARY

- **Total Notebooks Updated**: 6 (seccion1.ipynb through seccion6.ipynb)
- **Total Cells Updated**: 30 cells
- **Total Path Changes**: 60+ file paths

---

## 📋 UPDATES BY NOTEBOOK

### ✅ SECCION1.IPYNB

**Cells Updated**: 6 cells
**Cell 6da7d779**: ⏭️ Skipped (already updated by user)

| Cell ID | Old Path | New Path |
|---------|----------|----------|
| 74010428 | `normality_tests.png` | `../outputs/seccion1/normality_tests.png` |
| aef6dc4d | `checkpoint_seccion1_tareas1-3.json` | `../outputs/seccion1/checkpoint_seccion1_tareas1-3.json` |
| 1511fb18 | `variables_influyentes_top20.txt` | `../outputs/seccion1/variables_influyentes_top20.txt` |
| NO-ID-15 | `variables_seleccionadas.txt` | `../outputs/seccion1/variables_seleccionadas.txt` |
| NO-ID-16 | `vif_analysis.png` | `../outputs/seccion1/vif_analysis.png` |
| 622d6b70 | `checkpoint_seccion1_completa.json` | `../outputs/seccion1/checkpoint_seccion1_completa.json` |

**Summary**:
- All output files (PNG, TXT, JSON) now go to `../outputs/seccion1/`

---

### ✅ SECCION2.IPYNB

**Cells Updated**: 4 cells

| Cell ID | File Operation | Old Path | New Path |
|---------|----------------|----------|----------|
| a8a24d66 | `pd.read_csv()` | `dataset_saber11_reducido_estratificado.csv` | `../data/raw/dataset_saber11_reducido_estratificado.csv` |
| a8a24d66 | `open()` (read) | `checkpoint_seccion1_completa.json` | `../outputs/seccion1/checkpoint_seccion1_completa.json` |
| a6e44def | `pickle.dump()` | `preprocessing_objects.pkl` | `../data/processed/preprocessing_objects.pkl` |
| ca9e1888 | `to_csv()` | `X_train.csv` | `../data/processed/X_train.csv` |
| ca9e1888 | `to_csv()` | `X_test.csv` | `../data/processed/X_test.csv` |
| ca9e1888 | `to_csv()` | `y_train.csv` | `../data/processed/y_train.csv` |
| ca9e1888 | `to_csv()` | `y_test.csv` | `../data/processed/y_test.csv` |
| ca9e1888 | `pickle.dump()` | `train_test_split.pkl` | `../data/processed/train_test_split.pkl` |
| 78c46fdd | `to_csv()` | `X_train_pca.csv` | `../data/processed/X_train_pca.csv` |
| 78c46fdd | `to_csv()` | `X_test_pca.csv` | `../data/processed/X_test_pca.csv` |
| 78c46fdd | `pickle.dump()` | `pca_models.pkl` | `../data/processed/pca_models.pkl` |

**Summary**:
- Dataset loads from `../data/raw/`
- Checkpoint loads from `../outputs/seccion1/`
- All processed data (CSVs, PKLs) save to `../data/processed/`

---

### ✅ SECCION3.IPYNB

**Cells Updated**: 6 cells

| Cell ID | File Operation | Old Path | New Path |
|---------|----------------|----------|----------|
| 06fb671d | `pickle.load()` | `train_test_split.pkl` | `../data/processed/train_test_split.pkl` |
| 06fb671d | `pickle.load()` | `preprocessing_objects.pkl` | `../data/processed/preprocessing_objects.pkl` |
| 06fb671d | `pickle.load()` | `pca_models.pkl` | `../data/processed/pca_models.pkl` |
| e6cc8ea7 | `pickle.dump()` | `clustering_results.pkl` | `../data/processed/clustering_results.pkl` |
| 69377448 | `pickle.dump()` | `checkpoint_completo_tarea9.pkl` | `../data/processed/checkpoint_completo_tarea9.pkl` |
| d36b6ea5 | `pickle.dump()` | `optimal_k_results.pkl` | `../data/processed/optimal_k_results.pkl` |
| cd2ec7e5 | `pickle.dump()` | `visualization_results.pkl` | `../data/processed/visualization_results.pkl` |
| dafc7815 | `pickle.dump()` | `dimensionality_reduction_results.pkl` | `../data/processed/dimensionality_reduction_results.pkl` |
| b64569fc | `open()` (write) | `resumen_seccion3.txt` | `../outputs/seccion3/resumen_seccion3.txt` |

**Summary**:
- Reads processed data from `../data/processed/`
- Saves results to `../data/processed/`
- Output text files go to `../outputs/seccion3/`

---

### ✅ SECCION4.IPYNB

**Cells Updated**: 6 cells

| Cell ID | File Operation | Old Path | New Path |
|---------|----------------|----------|----------|
| load_data | `pickle.load()` | `train_test_split.pkl` | `../data/processed/train_test_split.pkl` |
| load_data | `pickle.load()` | `preprocessing_objects.pkl` | `../data/processed/preprocessing_objects.pkl` |
| load_data | `pickle.load()` | `pca_models.pkl` | `../data/processed/pca_models.pkl` |
| task14 | `plt.savefig()` | `model_comparison_metrics.png` | `../outputs/seccion4/model_comparison_metrics.png` |
| task14 | `plt.savefig()` | `confusion_matrices.png` | `../outputs/seccion4/confusion_matrices.png` |
| task14 | `plt.savefig()` | `roc_curves_multiclass.png` | `../outputs/seccion4/roc_curves_multiclass.png` |
| task15 | `plt.savefig()` | `cross_validation_analysis.png` | `../outputs/seccion4/cross_validation_analysis.png` |
| task16 | `pickle.dump()` | `tuned_models.pkl` | `../data/processed/tuned_models.pkl` |
| task16 | `plt.savefig()` | `hyperparameter_tuning_comparison.png` | `../outputs/seccion4/hyperparameter_tuning_comparison.png` |
| task17 | `pickle.dump()` | `feature_importance_analysis.pkl` | `../data/processed/feature_importance_analysis.pkl` |
| task17 | `plt.savefig()` | `feature_importance_random_forest.png` | `../outputs/seccion4/feature_importance_random_forest.png` |
| task17 | `plt.savefig()` | `feature_coefficients_logistic.png` | `../outputs/seccion4/feature_coefficients_logistic.png` |
| task17 | `plt.savefig()` | `decision_tree_structure.png` | `../outputs/seccion4/decision_tree_structure.png` |
| task17 | `plt.savefig()` | `feature_importance_comparison.png` | `../outputs/seccion4/feature_importance_comparison.png` |
| summary | `pickle.dump()` | `seccion4_complete_results.pkl` | `../data/processed/seccion4_complete_results.pkl` |
| summary | `open()` (write) | `resumen_seccion4.txt` | `../outputs/seccion4/resumen_seccion4.txt` |

**Summary**:
- Reads processed data from `../data/processed/`
- Saves models/results to `../data/processed/`
- All visualizations go to `../outputs/seccion4/`

---

### ✅ SECCION5.IPYNB

**Cells Updated**: 6 cells

| Cell ID | File Operation | Old Path | New Path |
|---------|----------------|----------|----------|
| load_data | `pd.read_csv()` | `../notebooks/dataset_saber11_reducido_estratificado.csv` | `../data/raw/dataset_saber11_reducido_estratificado.csv` |
| load_data | `pd.read_csv()` | `dataset_saber11_reducido_estratificado.csv` | `../data/raw/dataset_saber11_reducido_estratificado.csv` |
| task18 | `pickle.dump()` | `task18_results.pkl` | `../data/processed/task18_results.pkl` |
| task18 | `plt.savefig()` | `tarea18_supervised_vs_unsupervised.png` | `../outputs/seccion5/tarea18_supervised_vs_unsupervised.png` |
| task18 | `plt.savefig()` | `tarea18_confusion_matrix_clusters.png` | `../outputs/seccion5/tarea18_confusion_matrix_clusters.png` |
| task19_part1 | `plt.savefig()` | `smote_variants_comparison.png` | `../outputs/seccion5/smote_variants_comparison.png` |
| task19_part2 | `pickle.dump()` | `task19_results.pkl` | `../data/processed/task19_results.pkl` |
| task19_part2 | `plt.savefig()` | `tarea19_comparison_all_improvements.png` | `../outputs/seccion5/tarea19_comparison_all_improvements.png` |
| task19_part2 | `plt.savefig()` | `tarea19_best_model_confusion_matrix.png` | `../outputs/seccion5/tarea19_best_model_confusion_matrix.png` |
| sc3eoytkcos | `plt.savefig()` | `regularization_analysis.png` | `../outputs/seccion5/regularization_analysis.png` |
| task20 | `open()` (write) | `seccion5_reporte_final.txt` | `../outputs/seccion5/seccion5_reporte_final.txt` |
| task20 | `pickle.dump()` | `seccion5_complete_results.pkl` | `../data/processed/seccion5_complete_results.pkl` |

**Summary**:
- Dataset loads from `../data/raw/`
- Results save to `../data/processed/`
- All outputs go to `../outputs/seccion5/`

---

### ✅ SECCION6.IPYNB

**Cells Updated**: 6 cells

| Cell ID | File Operation | Old Path | New Path |
|---------|----------------|----------|----------|
| NO-ID-3 | `open()` (write) | `tarea21_justificacion_algoritmo.txt` | `../outputs/seccion6/tarea21_justificacion_algoritmo.txt` |
| NO-ID-3 | `plt.savefig()` | `tarea21_algorithm_selection.png` | `../outputs/seccion6/tarea21_algorithm_selection.png` |
| NO-ID-5 | `open()` (write) | `tarea22_diseno_completo.txt` | `../outputs/seccion6/tarea22_diseno_completo.txt` |
| NO-ID-5 | `plt.savefig()` | `tarea22_arquitectura_sistema.png` | `../outputs/seccion6/tarea22_arquitectura_sistema.png` |
| NO-ID-7 | `pd.read_csv()` | `X_train.csv` | `../data/processed/X_train.csv` |
| NO-ID-7 | `pd.read_csv()` | `X_test.csv` | `../data/processed/X_test.csv` |
| NO-ID-7 | `pd.read_csv()` | `y_train.csv` | `../data/processed/y_train.csv` |
| NO-ID-7 | `pd.read_csv()` | `y_test.csv` | `../data/processed/y_test.csv` |
| NO-ID-8 | `pd.read_csv()` | `X_train.csv` | `../data/processed/X_train.csv` |
| NO-ID-8 | `pd.read_csv()` | `X_test.csv` | `../data/processed/X_test.csv` |
| NO-ID-8 | `pd.read_csv()` | `y_train.csv` | `../data/processed/y_train.csv` |
| NO-ID-8 | `pd.read_csv()` | `y_test.csv` | `../data/processed/y_test.csv` |
| NO-ID-8 | `to_csv()` | `seccion6_c_docker/data/train_data_c.csv` | `../data/processed/train_data_c.csv` ⚠️ |
| NO-ID-8 | `to_csv()` | `seccion6_c_docker/data/test_data_c.csv` | `../data/processed/test_data_c.csv` ⚠️ |
| NO-ID-8 | `pickle.load()` | `train_test_split.pkl` | `../data/processed/train_test_split.pkl` |
| NO-ID-10 | `pd.read_csv()` | `X_train.csv` | `../data/processed/X_train.csv` |
| NO-ID-10 | `pd.read_csv()` | `X_test.csv` | `../data/processed/X_test.csv` |
| NO-ID-10 | `pd.read_csv()` | `y_train.csv` | `../data/processed/y_train.csv` |
| NO-ID-10 | `pd.read_csv()` | `y_test.csv` | `../data/processed/y_test.csv` |
| NO-ID-10 | `open()` (write) | `tarea24_comparacion_completa.txt` | `../outputs/seccion6/tarea24_comparacion_completa.txt` |
| NO-ID-10 | `plt.savefig()` | `tarea24_comparison_python_vs_c.png` | `../outputs/seccion6/tarea24_comparison_python_vs_c.png` |
| NO-ID-12 | `open()` (write) | `tarea25_analisis_limitaciones.txt` | `../outputs/seccion6/tarea25_analisis_limitaciones.txt` |
| NO-ID-12 | `plt.savefig()` | `tarea25_optimizaciones_comparacion.png` | `../outputs/seccion6/tarea25_optimizaciones_comparacion.png` |

⚠️ **Important**: C data files moved from `seccion6_c_docker/data/` to `../data/processed/`

**Summary**:
- Reads processed data from `../data/processed/`
- C implementation data files now save to `../data/processed/` (not `seccion6_c_docker/data/`)
- All outputs go to `../outputs/seccion6/`

---

## 🗂️ NEW FOLDER STRUCTURE

```
Ia_EDA_analysis/
├── data/
│   ├── raw/                           # Original dataset
│   │   └── dataset_saber11_reducido_estratificado.csv
│   └── processed/                     # All processed data, models, PKLs
│       ├── X_train.csv, X_test.csv
│       ├── y_train.csv, y_test.csv
│       ├── X_train_pca.csv, X_test_pca.csv
│       ├── train_data_c.csv, test_data_c.csv
│       ├── preprocessing_objects.pkl
│       ├── train_test_split.pkl
│       ├── pca_models.pkl
│       ├── clustering_results.pkl
│       ├── tuned_models.pkl
│       ├── feature_importance_analysis.pkl
│       ├── seccion4_complete_results.pkl
│       ├── seccion5_complete_results.pkl
│       └── ... (all other PKL files)
├── notebooks/                          # All 6 notebooks
│   ├── seccion1.ipynb
│   ├── seccion2.ipynb
│   ├── seccion3.ipynb
│   ├── seccion4.ipynb
│   ├── seccion5.ipynb
│   └── seccion6.ipynb
├── outputs/
│   ├── seccion1/                      # All seccion1 outputs
│   │   ├── normality_tests.png
│   │   ├── vif_analysis.png
│   │   ├── checkpoint_seccion1_tareas1-3.json
│   │   ├── checkpoint_seccion1_completa.json
│   │   ├── variables_influyentes_top20.txt
│   │   └── variables_seleccionadas.txt
│   ├── seccion2/                      # All seccion2 outputs (PCA plots)
│   ├── seccion3/                      # All seccion3 outputs
│   │   └── resumen_seccion3.txt
│   ├── seccion4/                      # All seccion4 outputs
│   │   ├── model_comparison_metrics.png
│   │   ├── confusion_matrices.png
│   │   ├── roc_curves_multiclass.png
│   │   ├── cross_validation_analysis.png
│   │   ├── hyperparameter_tuning_comparison.png
│   │   ├── feature_importance_*.png
│   │   └── resumen_seccion4.txt
│   ├── seccion5/                      # All seccion5 outputs
│   │   ├── tarea18_*.png
│   │   ├── tarea19_*.png
│   │   ├── regularization_analysis.png
│   │   └── seccion5_reporte_final.txt
│   └── seccion6/                      # All seccion6 outputs
│       ├── tarea21_*.png/txt
│       ├── tarea22_*.png/txt
│       ├── tarea24_*.png/txt
│       └── tarea25_*.png/txt
└── src/
    └── c_implementation/
```

---

## 📝 PATH PATTERNS

### Reading Dataset
- **Before**: `'dataset_saber11_reducido_estratificado.csv'`
- **After**: `'../data/raw/dataset_saber11_reducido_estratificado.csv'`

### Reading Processed Data
- **Before**: `'X_train.csv'`, `'train_test_split.pkl'`
- **After**: `'../data/processed/X_train.csv'`, `'../data/processed/train_test_split.pkl'`

### Writing Processed Data
- **Before**: `to_csv('X_train.csv')`
- **After**: `to_csv('../data/processed/X_train.csv')`

### Writing Outputs
- **Before**: `plt.savefig('chart.png')`
- **After**: `plt.savefig('../outputs/seccionX/chart.png')`

### Special Cases
- **Checkpoints from Seccion1**: Read from `'../outputs/seccion1/checkpoint_seccion1_completa.json'`
- **C Data Files**: Now saved to `'../data/processed/train_data_c.csv'` instead of `'seccion6_c_docker/data/'`

---

## ✅ VERIFICATION

All path updates have been applied successfully. To verify:

1. **Check cell counts**:
   ```bash
   python3 analyze_notebooks.py
   ```

2. **Run notebooks**:
   - Execute each notebook from the `notebooks/` directory
   - All file I/O operations should work with the new folder structure

3. **Verify outputs**:
   - Check that files are created in the correct locations
   - `outputs/seccionX/` should contain visualization and text files
   - `data/processed/` should contain all CSVs and PKL files

---

## ⚠️ IMPORTANT NOTES

1. **Execution Directory**: Always run notebooks from the `notebooks/` directory
2. **Relative Paths**: All paths use `../` to navigate from `notebooks/` to parent directory
3. **C Implementation**: The C code data files moved from `seccion6_c_docker/data/` to `data/processed/`
4. **Cell IDs**: Some cells in seccion1 and seccion6 don't have IDs (marked as NO-ID)

---

## 🎉 COMPLETION STATUS

- ✅ seccion1.ipynb: 6 cells updated
- ✅ seccion2.ipynb: 4 cells updated (11 path changes)
- ✅ seccion3.ipynb: 6 cells updated (9 path changes)
- ✅ seccion4.ipynb: 6 cells updated (16 path changes)
- ✅ seccion5.ipynb: 6 cells updated (12 path changes)
- ✅ seccion6.ipynb: 6 cells updated (22 path changes)

**Total**: 30 cells updated, 70+ file paths corrected

---

**Report Generated**: November 20, 2025
**Status**: ✅ All notebooks updated and ready to use with new folder structure
