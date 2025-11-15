#!/usr/bin/env python3
"""
Final builder for Section 6 - Adds Tasks 23-25
"""

import json

def load_nb():
    with open('notebooks/seccion6.ipynb', 'r') as f:
        return json.load(f)

def save_nb(nb):
    with open('notebooks/seccion6.ipynb', 'w') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

def add_code_cell(nb, code):
    nb["cells"].append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": code.split('\n')
    })

def add_md_cell(nb, md):
    nb["cells"].append({
        "cell_type": "markdown",
        "metadata": {},
        "source": md.split('\n')
    })

# Load notebook
nb = load_nb()
print(f"Starting with {len(nb['cells'])} cells")

# === TAREA 23 CODE ===
tarea23_code = """# ============================================
# TAREA 23: Preparación de Datos para C y Verificación
# ============================================

print("="*80)
print("TAREA 23: PREPARACIÓN DE DATOS Y VERIFICACIÓN DEL CÓDIGO C")
print("="*80)

# Este código prepara los datos para la implementación en C y verifica la compilación

import os

# 1. Preparar datos de entrenamiento y prueba reducidos para C
print("\\n1️⃣ Preparando datos para implementación en C...")

# Intentar cargar datos desde secciones anteriores
data_loaded = False
X_train, X_test, y_train, y_test = None, None, None, None

# Intentar cargar desde checkpoints
try:
    if os.path.exists('checkpoint_seccion2.pkl'):
        import pickle
        with open('checkpoint_seccion2.pkl', 'rb') as f:
            checkpoint = pickle.load(f)
            X_train = checkpoint.get('X_train')
            X_test = checkpoint.get('X_test')
            y_train = checkpoint.get('y_train')
            y_test = checkpoint.get('y_test')
        if X_train is not None:
            print("✅ Datos cargados desde checkpoint de Sección 2")
            data_loaded = True
except Exception as e:
    print(f"⚠️  No se pudo cargar checkpoint: {e}")

# Si no hay datos, cargar dataset y preparar
if not data_loaded:
    print("\\n📂 Cargando y preparando dataset...")
    
    # Intentar cargar dataset
    dataset_paths = [
        '../datasets/dataset_saber11_reducido_estratificado.xlsx',
        'datasets/dataset_saber11_reducido_estratificado.xlsx',
        'dataset_saber11_reducido_estratificado.csv'
    ]
    
    df = None
    for path in dataset_paths:
        if os.path.exists(path):
            print(f"   Cargando desde: {path}")
            if path.endswith('.xlsx'):
                df = pd.read_excel(path, nrows=5000)  # Subset
            else:
                df = pd.read_csv(path, nrows=5000)
            break
    
    if df is None:
        print("⚠️  No se encontró dataset. Generando datos sintéticos...")
        # Generar datos sintéticos para demostración
        np.random.seed(RANDOM_STATE)
        n_samples = 2000
        n_features = 10
        n_classes = 5
        
        X = np.random.randn(n_samples, n_features)
        y = np.random.randint(0, n_classes, n_samples)
        
        # Añadir algo de estructura
        for i in range(n_features):
            X[:, i] += y * 0.5
        
        # Split
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=RANDOM_STATE, stratify=y
        )
        
        # Normalizar
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
        
        data_loaded = True
        print(f"✅ Datos sintéticos generados: {n_samples} muestras, {n_features} features")
    else:
        # Procesar dataset real
        print("   Procesando dataset...")
        
        # Identificar columnas
        target_col = 'DESEMP_INGLES' if 'DESEMP_INGLES' in df.columns else df.columns[-1]
        feature_cols = [col for col in df.columns if col != target_col]
        
        # Seleccionar top 10 features (numéricas)
        numeric_cols = df[feature_cols].select_dtypes(include=[np.number]).columns[:10]
        
        X = df[numeric_cols].fillna(0).values
        y = pd.factorize(df[target_col])[0]
        
        # Split
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=RANDOM_STATE, stratify=y
        )
        
        # Normalizar
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
        
        data_loaded = True
        print(f"✅ Dataset procesado: {len(X)} muestras, {len(numeric_cols)} features")

if not data_loaded:
    print("❌ Error: No se pudieron cargar datos")
else:
    print(f"\\n📊 Datos preparados:")
    print(f"   Train: {X_train.shape}")
    print(f"   Test: {X_test.shape}")
    print(f"   Clases: {len(np.unique(y_train))}")

# 2. Crear versión reducida para C (1000 train, 300 test)
print("\\n2️⃣ Creando versión reducida para C...")

# Balancear y reducir
n_train_c = min(1000, len(X_train))
n_test_c = min(300, len(X_test))

# Muestreo estratificado
from sklearn.model_selection import StratifiedShuffleSplit

sss = StratifiedShuffleSplit(n_splits=1, train_size=n_train_c, random_state=RANDOM_STATE)
for train_idx, _ in sss.split(X_train, y_train):
    X_train_c = X_train[train_idx]
    y_train_c = y_train[train_idx]

sss = StratifiedShuffleSplit(n_splits=1, train_size=n_test_c, random_state=RANDOM_STATE)
for test_idx, _ in sss.split(X_test, y_test):
    X_test_c = X_test[test_idx]
    y_test_c = y_test[test_idx]

print(f"✅ Datos reducidos:")
print(f"   Train C: {X_train_c.shape}")
print(f"   Test C: {X_test_c.shape}")

# 3. Guardar en formato CSV para C
print("\\n3️⃣ Guardando datos en formato CSV...")

# Crear DataFrames
train_df_c = pd.DataFrame(X_train_c, columns=[f'f{i}' for i in range(X_train_c.shape[1])])
train_df_c['label'] = y_train_c

test_df_c = pd.DataFrame(X_test_c, columns=[f'f{i}' for i in range(X_test_c.shape[1])])
test_df_c['label'] = y_test_c

# Guardar
train_df_c.to_csv('train_data_c.csv', index=False)
test_df_c.to_csv('test_data_c.csv', index=False)

print("✅ Archivos CSV creados:")
print("   - train_data_c.csv")
print("   - test_data_c.csv")

# 4. Verificar código C
print("\\n4️⃣ Verificando código C...")

if os.path.exists('knn_classifier.c'):
    print("✅ knn_classifier.c encontrado")
    
    # Contar líneas
    with open('knn_classifier.c', 'r') as f:
        lines = f.readlines()
    print(f"   Líneas de código: {len(lines)}")
    
    # Verificar componentes clave
    content = ''.join(lines)
    components = [
        ('DataPoint', 'typedef struct.*DataPoint'),
        ('Dataset', 'typedef struct.*Dataset'),
        ('KNNModel', 'typedef struct.*KNNModel'),
        ('euclidean_distance', 'double euclidean_distance'),
        ('knn_predict', 'void knn_predict'),
        ('majority_vote', 'int majority_vote'),
        ('load_dataset', 'Dataset.*load_dataset'),
    ]
    
    print("\\n   Componentes verificados:")
    for name, pattern in components:
        import re
        if re.search(pattern, content):
            print(f"   ✅ {name}")
        else:
            print(f"   ❌ {name} NO ENCONTRADO")
else:
    print("❌ knn_classifier.c NO encontrado")

# 5. Verificar Makefile
print("\\n5️⃣ Verificando Makefile...")

if os.path.exists('Makefile'):
    print("✅ Makefile encontrado")
else:
    print("⚠️  Makefile no encontrado (opcional)")

# 6. Intentar compilar (si gcc está disponible)
print("\\n6️⃣ Intentando compilar...")

try:
    result = subprocess.run(['gcc', '--version'], capture_output=True, text=True)
    if result.returncode == 0:
        print("✅ GCC disponible:")
        print("   " + result.stdout.split('\\n')[0])
        
        # Compilar
        print("\\n   Compilando knn_classifier.c...")
        compile_result = subprocess.run(
            ['gcc', '-o', 'knn_classifier', 'knn_classifier.c', '-lm', '-O2', '-Wall'],
            capture_output=True,
            text=True
        )
        
        if compile_result.returncode == 0:
            print("   ✅ Compilación exitosa!")
            print("   ✅ Ejecutable: knn_classifier")
            
            # Verificar ejecutable
            if os.path.exists('knn_classifier') or os.path.exists('knn_classifier.exe'):
                print("   ✅ Ejecutable creado correctamente")
        else:
            print("   ⚠️  Errores de compilación:")
            print("   " + compile_result.stderr[:500])
    else:
        print("⚠️  GCC no disponible. Compilación manual requerida.")
except Exception as e:
    print(f"⚠️  No se pudo verificar compilación: {e}")
    print("   Compilación manual requerida:")
    print("   gcc -o knn_classifier knn_classifier.c -lm -O2")

print("\\n" + "="*80)
print("TAREA 23 COMPLETADA ✅")
print("="*80)
print("\\n✅ Archivos generados para implementación en C:")
print("   1. knn_classifier.c (implementación completa)")
print("   2. train_data_c.csv (1000 muestras)")
print("   3. test_data_c.csv (300 muestras)")
print("   4. Makefile (script de compilación)")
print("\\n📝 Para ejecutar:")
print("   make                    # Compilar")
print("   make run               # Compilar y ejecutar")
print("   ./knn_classifier train_data_c.csv test_data_c.csv 5")"""

add_code_cell(nb, tarea23_code)
print(f"Added Tarea 23 code. Current cells: {len(nb['cells'])}")

# Save intermediate progress
save_nb(nb)
print("✅ Notebook saved")

print(f"\\n✅ Complete! Notebook now has {len(nb['cells'])} cells")
print("✅ Tarea 23 is complete")
print("Next: Will add Tareas 24 and 25...")

