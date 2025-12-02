import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import sys
import os

def load_and_prepare_dataset(input_path, output_path, sample_size=None):
    """
    Carga el dataset de Saber 11 y prepara datos para MLP en C
    """
    print("=" * 80)
    print("PREPARACIÓN DE DATASET PARA MLP EN C")
    print("=" * 80)
    
    if not os.path.exists(input_path):
        print(f"Error: No se encuentra el archivo {input_path}")
        sys.exit(1)
    
    print(f"\n1. Cargando dataset desde {input_path}...")
    try:
        df = pd.read_csv(input_path)
        print(f"   Dataset cargado: {df.shape[0]} filas, {df.shape[1]} columnas")
    except Exception as e:
        print(f"Error al cargar dataset: {e}")
        sys.exit(1)
    
    print("\n2. Seleccionando features más importantes...")
    selected_features = [
        'PUNT_GLOBAL',
        'PUNT_C_NATURALES',
        'PUNT_LECTURA_CRITICA',
        'PUNT_SOCIALES_CIUDADANAS',
        'PUNT_MATEMATICAS',
        'FAMI_TIENEINTERNET',
        'FAMI_TIENECOMPUTADOR',
        'COLE_NATURALEZA',
        'FAMI_TIENEAUTOMOVIL',
        'FAMI_EDUCACIONMADRE'
    ]
    
    target = 'DESEMP_INGLES'
    
    available_features = [f for f in selected_features if f in df.columns]
    if target not in df.columns:
        print(f"Error: Variable objetivo '{target}' no encontrada")
        sys.exit(1)
    
    print(f"   Features disponibles: {len(available_features)}/{len(selected_features)}")
    for feat in available_features:
        print(f"   - {feat}")
    
    df_subset = df[available_features + [target]].copy()
    
    print("\n3. Limpiando datos...")
    print(f"   Filas antes de limpieza: {len(df_subset)}")
    df_subset = df_subset.dropna()
    print(f"   Filas después de limpieza: {len(df_subset)}")
    
    print("\n4. Codificando variables categóricas...")
    categorical_features = df_subset.select_dtypes(include=['object']).columns.tolist()
    if target in categorical_features:
        categorical_features.remove(target)
    
    label_encoders = {}
    for col in categorical_features:
        le = LabelEncoder()
        df_subset[col] = le.fit_transform(df_subset[col].astype(str))
        print(f"   - {col}: {len(le.classes_)} categorías")
        label_encoders[col] = le
    
    print("\n5. Codificando variable objetivo...")
    class_mapping = {'A-': 0, 'A1': 1, 'A2': 2, 'B+': 3, 'B1': 4}
    df_subset[target] = df_subset[target].map(class_mapping)
    
    if df_subset[target].isna().any():
        print("   Advertencia: Clases no reconocidas encontradas")
        df_subset = df_subset.dropna(subset=[target])
    
    df_subset[target] = df_subset[target].astype(int)
    
    print("\n   Distribución de clases:")
    class_dist = df_subset[target].value_counts().sort_index()
    class_names = ['A-', 'A1', 'A2', 'B+', 'B1']
    for label, count in class_dist.items():
        pct = 100.0 * count / len(df_subset)
        print(f"   Clase {label} ({class_names[label]}): {count:6d} ({pct:5.2f}%)")
    
    if sample_size and sample_size < len(df_subset):
        print(f"\n6. Muestreando {sample_size} observaciones (estratificado)...")
        from sklearn.model_selection import train_test_split
        df_subset, _ = train_test_split(
            df_subset, 
            train_size=sample_size, 
            stratify=df_subset[target],
            random_state=42
        )
        print(f"   Dataset reducido: {len(df_subset)} filas")
    
    print("\n7. Organizando datos para exportación...")
    X = df_subset[available_features].values
    y = df_subset[target].values
    
    print(f"   Shape final: X={X.shape}, y={y.shape}")
    print(f"   Tipos de datos: X={X.dtype}, y={y.dtype}")
    
    print("\n8. Guardando dataset procesado...")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w') as f:
        for i in range(len(X)):
            features_str = ','.join([f'{val:.6f}' for val in X[i]])
            f.write(f"{features_str},{y[i]}\n")
    
    print(f"   Dataset guardado en: {output_path}")
    print(f"   Formato: {len(available_features)} features + 1 label por línea")
    
    metadata_path = output_path.replace('.csv', '_metadata.txt')
    with open(metadata_path, 'w') as f:
        f.write("=" * 80 + "\n")
        f.write("METADATA DEL DATASET PROCESADO\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Archivo de salida: {output_path}\n")
        f.write(f"Número de muestras: {len(df_subset)}\n")
        f.write(f"Número de features: {len(available_features)}\n")
        f.write(f"Número de clases: {len(class_dist)}\n\n")
        f.write("FEATURES SELECCIONADAS:\n")
        for i, feat in enumerate(available_features):
            f.write(f"{i+1:2d}. {feat}\n")
        f.write(f"\nVARIABLE OBJETIVO: {target}\n")
        f.write("Mapeo de clases:\n")
        for name, label in class_mapping.items():
            f.write(f"  {name} -> {label}\n")
        f.write("\nDISTRIBUCIÓN DE CLASES:\n")
        for label, count in class_dist.items():
            pct = 100.0 * count / len(df_subset)
            f.write(f"  Clase {label} ({class_names[label]}): {count:6d} ({pct:5.2f}%)\n")
        f.write("\nCODIFICACIONES CATEGÓRICAS:\n")
        for col, le in label_encoders.items():
            f.write(f"\n{col}:\n")
            for i, cls in enumerate(le.classes_):
                f.write(f"  {cls} -> {i}\n")
    
    print(f"   Metadata guardada en: {metadata_path}")
    
    print("\n" + "=" * 80)
    print("PREPARACIÓN COMPLETADA EXITOSAMENTE")
    print("=" * 80)
    
    return df_subset, available_features, class_mapping

if __name__ == "__main__":
    base_path = "/workspaces/Ia_EDA_analysis"
    
    input_csv = os.path.join(base_path, "datasets", "dataset_reducido.csv")
    output_csv = os.path.join(base_path, "seccion6_c_ANN", "data", "dataset_processed.csv")
    
    if len(sys.argv) > 1:
        input_csv = sys.argv[1]
    if len(sys.argv) > 2:
        output_csv = sys.argv[2]
    
    sample_size = 50000
    if len(sys.argv) > 3:
        sample_size = int(sys.argv[3])
    
    df, features, mapping = load_and_prepare_dataset(input_csv, output_csv, sample_size)
    
    print(f"\nPara entrenar el modelo, ejecuta:")
    print(f"  cd {os.path.dirname(output_csv)}/..")
    print(f"  make")
    print(f"  ./bin/mlp_classifier data/dataset_processed.csv")
