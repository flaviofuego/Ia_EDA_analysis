import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import os
import sys

def generate_synthetic_dataset(n_samples=50000, output_path=None):
    """
    Genera un dataset sintético con características similares al problema real
    basado en las distribuciones observadas en el análisis previo
    """
    print("=" * 80)
    print("GENERACIÓN DE DATASET SINTÉTICO PARA MLP")
    print("=" * 80)
    
    np.random.seed(42)
    
    print(f"\n1. Generando {n_samples} muestras sintéticas...")
    
    class_probs = [0.495, 0.282, 0.146, 0.013, 0.064]
    class_names = ['A-', 'A1', 'A2', 'B+', 'B1']
    
    labels = np.random.choice(5, size=n_samples, p=class_probs)
    
    print("\n2. Generando features correlacionadas con clases...")
    
    data = {}
    
    base_scores = {
        0: {'mean': 45, 'std': 8},   # A-
        1: {'mean': 55, 'std': 7},   # A1
        2: {'mean': 65, 'std': 6},   # A2
        3: {'mean': 75, 'std': 5},   # B+
        4: {'mean': 80, 'std': 4}    # B1
    }
    
    features_numeric = [
        'PUNT_GLOBAL',
        'PUNT_C_NATURALES',
        'PUNT_LECTURA_CRITICA',
        'PUNT_SOCIALES_CIUDADANAS',
        'PUNT_MATEMATICAS'
    ]
    
    for feat in features_numeric:
        values = np.zeros(n_samples)
        for class_id in range(5):
            mask = labels == class_id
            n_class = mask.sum()
            values[mask] = np.random.normal(
                base_scores[class_id]['mean'],
                base_scores[class_id]['std'],
                n_class
            ) + np.random.uniform(-3, 3, n_class)
        
        values = np.clip(values, 0, 100)
        data[feat] = values
    
    print("   - Features numéricas generadas (puntajes)")
    
    categorical_binary = [
        'FAMI_TIENEINTERNET',
        'FAMI_TIENECOMPUTADOR',
        'FAMI_TIENEAUTOMOVIL'
    ]
    
    for i, feat in enumerate(categorical_binary):
        probs_by_class = {
            0: 0.3 + i * 0.05,
            1: 0.5 + i * 0.05,
            2: 0.7 + i * 0.05,
            3: 0.85 + i * 0.02,
            4: 0.90 + i * 0.02
        }
        
        values = np.zeros(n_samples)
        for class_id in range(5):
            mask = labels == class_id
            n_class = mask.sum()
            values[mask] = np.random.binomial(1, probs_by_class[class_id], n_class)
        
        data[feat] = values.astype(int)
    
    print("   - Features categóricas binarias generadas")
    
    data['COLE_NATURALEZA'] = np.zeros(n_samples, dtype=int)
    for class_id in range(5):
        mask = labels == class_id
        n_class = mask.sum()
        if class_id < 2:
            data['COLE_NATURALEZA'][mask] = np.random.choice([0, 1], n_class, p=[0.7, 0.3])
        else:
            data['COLE_NATURALEZA'][mask] = np.random.choice([0, 1], n_class, p=[0.3, 0.7])
    
    data['FAMI_EDUCACIONMADRE'] = np.zeros(n_samples, dtype=int)
    for class_id in range(5):
        mask = labels == class_id
        n_class = mask.sum()
        if class_id <= 1:
            data['FAMI_EDUCACIONMADRE'][mask] = np.random.choice([0, 1, 2, 3], n_class, p=[0.4, 0.3, 0.2, 0.1])
        elif class_id <= 3:
            data['FAMI_EDUCACIONMADRE'][mask] = np.random.choice([0, 1, 2, 3], n_class, p=[0.2, 0.3, 0.3, 0.2])
        else:
            data['FAMI_EDUCACIONMADRE'][mask] = np.random.choice([0, 1, 2, 3], n_class, p=[0.1, 0.2, 0.3, 0.4])
    
    print("   - Features categóricas multi-clase generadas")
    
    df = pd.DataFrame(data)
    df['DESEMP_INGLES'] = labels
    
    print(f"\n3. Dataset generado: {df.shape}")
    print(f"   Features: {df.shape[1] - 1}")
    print(f"   Muestras: {df.shape[0]}")
    
    print("\n4. Distribución de clases:")
    for class_id in range(5):
        count = (labels == class_id).sum()
        pct = 100.0 * count / n_samples
        print(f"   Clase {class_id} ({class_names[class_id]}): {count:6d} ({pct:5.2f}%)")
    
    if output_path:
        print(f"\n5. Guardando dataset temporal...")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False)
        print(f"   Dataset guardado en: {output_path}")
    
    print("\n" + "=" * 80)
    
    return df

def prepare_for_c(df, output_path):
    """
    Convierte el dataframe a formato CSV para el programa en C
    """
    print("\n6. Preparando datos para MLP en C...")
    
    feature_cols = [col for col in df.columns if col != 'DESEMP_INGLES']
    X = df[feature_cols].values
    y = df['DESEMP_INGLES'].values
    
    print(f"   Shape: X={X.shape}, y={y.shape}")
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w') as f:
        for i in range(len(X)):
            features_str = ','.join([f'{val:.6f}' for val in X[i]])
            f.write(f"{features_str},{y[i]}\n")
    
    print(f"   Dataset procesado guardado en: {output_path}")
    
    metadata_path = output_path.replace('.csv', '_metadata.txt')
    with open(metadata_path, 'w') as f:
        f.write("=" * 80 + "\n")
        f.write("METADATA DEL DATASET SINTÉTICO\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Archivo: {output_path}\n")
        f.write(f"Muestras: {len(df)}\n")
        f.write(f"Features: {len(feature_cols)}\n")
        f.write(f"Clases: 5\n\n")
        f.write("FEATURES:\n")
        for i, feat in enumerate(feature_cols):
            f.write(f"{i+1:2d}. {feat}\n")
        f.write("\nVARIABLE OBJETIVO: DESEMP_INGLES\n")
        f.write("Mapeo: A-=0, A1=1, A2=2, B+=3, B1=4\n\n")
        f.write("DISTRIBUCIÓN DE CLASES:\n")
        class_names = ['A-', 'A1', 'A2', 'B+', 'B1']
        for class_id in range(5):
            count = (y == class_id).sum()
            pct = 100.0 * count / len(y)
            f.write(f"  Clase {class_id} ({class_names[class_id]}): {count:6d} ({pct:5.2f}%)\n")
        f.write("\nESTADÍSTICAS DE FEATURES:\n")
        for feat in feature_cols:
            f.write(f"\n{feat}:\n")
            f.write(f"  Min:  {df[feat].min():.2f}\n")
            f.write(f"  Max:  {df[feat].max():.2f}\n")
            f.write(f"  Mean: {df[feat].mean():.2f}\n")
            f.write(f"  Std:  {df[feat].std():.2f}\n")
    
    print(f"   Metadata guardada en: {metadata_path}")

if __name__ == "__main__":
    base_path = "/workspaces/Ia_EDA_analysis/seccion6_c_ANN"
    
    n_samples = 50000
    if len(sys.argv) > 1:
        n_samples = int(sys.argv[1])
    
    temp_csv = os.path.join(base_path, "data", "dataset_synthetic.csv")
    output_csv = os.path.join(base_path, "data", "dataset_processed.csv")
    
    df = generate_synthetic_dataset(n_samples, temp_csv)
    
    prepare_for_c(df, output_csv)
    
    print("\n" + "=" * 80)
    print("PREPARACIÓN COMPLETADA")
    print("=" * 80)
    print(f"\nPara compilar y entrenar el modelo:")
    print(f"  cd {base_path}")
    print(f"  make clean && make")
    print(f"  ./bin/mlp_classifier data/dataset_processed.csv")
    print("\n" + "=" * 80)
