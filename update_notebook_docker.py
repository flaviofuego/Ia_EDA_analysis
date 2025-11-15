#!/usr/bin/env python3
"""
Script para actualizar el notebook seccion6.ipynb para usar Docker
en lugar de código C inline en la Tarea 23
"""

import json
import os

def update_tarea23_to_docker():
    """
    Actualiza TAREA 23 para usar Docker en lugar de mostrar código C inline
    """
    
    notebook_path = '/home/runner/work/Ia_EDA_analysis/Ia_EDA_analysis/notebooks/seccion6.ipynb'
    
    # Leer notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # Nuevo contenido para TAREA 23
    new_tarea23_code = """# ============================================
# TAREA 23: Implementación Completa en C
# ============================================

# En lugar de mostrar el código C directamente en el notebook,
# la implementación se encuentra en una estructura Docker profesional
# para facilitar la compilación y ejecución en cualquier sistema operativo.

print("=" * 80)
print("TAREA 23: IMPLEMENTACIÓN COMPLETA EN C CON DOCKER")
print("=" * 80)
print()

# ESTRUCTURA DEL PROYECTO C CON DOCKER
docker_structure = '''
📁 seccion6_c_docker/
├── Dockerfile              # Imagen Docker para compilar y ejecutar
├── docker-compose.yml      # Orquestación simplificada
├── README.md              # Documentación completa
├── src/
│   ├── knn_classifier.c   # Implementación KNN (595 líneas)
│   └── Makefile           # Script de compilación
├── data/
│   ├── train_data_c.csv   # Datos de entrenamiento
│   └── test_data_c.csv    # Datos de prueba  
├── results/
│   └── output.txt         # Resultados de ejecución
└── scripts/
    ├── build.sh           # Construir imagen Docker
    └── run.sh             # Ejecutar contenedor
'''

print("📂 ESTRUCTURA DEL PROYECTO:")
print(docker_structure)
print()

# PREPARAR DATOS PARA C
print("🔧 PREPARANDO DATOS PARA LA IMPLEMENTACIÓN EN C...")
print()

# Cargar datos preprocesados de secciones anteriores
try:
    # Intentar cargar datos procesados
    X_train = pd.read_csv('X_train.csv')
    X_test = pd.read_csv('X_test.csv')
    y_train = pd.read_csv('y_train.csv').values.ravel()
    y_test = pd.read_csv('y_test.csv').values.ravel()
    
    print(f"✅ Datos cargados:")
    print(f"   Train: {X_train.shape[0]} muestras, {X_train.shape[1]} features")
    print(f"   Test: {X_test.shape[0]} muestras, {X_test.shape[1]} features")
    print()
    
except FileNotFoundError:
    print("⚠️  Archivos de datos no encontrados. Generando datos de ejemplo...")
    # Generar datos de ejemplo para demostración
    from sklearn.datasets import make_classification
    X, y = make_classification(
        n_samples=1300, n_features=10, n_informative=8, 
        n_redundant=2, n_classes=5, n_clusters_per_class=2,
        random_state=42
    )
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    print(f"✅ Datos de ejemplo generados:")
    print(f"   Train: {X_train.shape[0]} muestras, {X_train.shape[1]} features")
    print(f"   Test: {X_test.shape[0]} muestras, {X_test.shape[1]} features")
    print()

# Crear versión reducida para C (para eficiencia)
n_train_c = min(1000, len(X_train))
n_test_c = min(300, len(X_test))

X_train_c = X_train[:n_train_c]
y_train_c = y_train[:n_train_c]
X_test_c = X_test[:n_test_c]
y_test_c = y_test[:n_test_c]

print(f"📊 Versión reducida para C:")
print(f"   Train: {n_train_c} muestras")
print(f"   Test: {n_test_c} muestras")
print()

# PREPARAR ARCHIVOS CSV PARA C
docker_data_path = '../seccion6_c_docker/data'
os.makedirs(docker_data_path, exist_ok=True)

# Función para guardar datos en formato CSV para C
def save_for_c(X, y, filename):
    df = pd.DataFrame(X)
    df['label'] = y
    filepath = os.path.join(docker_data_path, filename)
    df.to_csv(filepath, index=False, header=False)
    return filepath

# Guardar datos
train_path = save_for_c(X_train_c, y_train_c, 'train_data_c.csv')
test_path = save_for_c(X_test_c, y_test_c, 'test_data_c.csv')

print(f"✅ Datos guardados para C:")
print(f"   Training: {train_path}")
print(f"   Testing: {test_path}")
print()

# INFORMACIÓN SOBRE LA IMPLEMENTACIÓN EN C
print("=" * 80)
print("CARACTERÍSTICAS DE LA IMPLEMENTACIÓN EN C")
print("=" * 80)
print()

features = [
    "✅ 595 líneas de código C profesional",
    "✅ Algoritmo: K-Nearest Neighbors (KNN)",
    "✅ Estructuras de datos optimizadas",
    "✅ Gestión robusta de memoria (malloc/free)",
    "✅ Manejo completo de errores",
    "✅ Carga de datos desde CSV",
    "✅ Cálculo de distancia euclidiana",
    "✅ Votación por mayoría para clasificación",
    "✅ Evaluación con múltiples métricas",
    "✅ Matriz de confusión",
    "✅ Métricas por clase (Precision, Recall, F1)",
    "✅ Output formateado profesional"
]

for feature in features:
    print(f"  {feature}")
print()

# VENTAJAS DEL ENFOQUE DOCKER
print("=" * 80)
print("VENTAJAS DE USAR DOCKER")
print("=" * 80)
print()

advantages = [
    "🐳 Portabilidad: Funciona en Windows, macOS y Linux sin cambios",
    "🔄 Reproducibilidad: Misma versión de compilador para todos",
    "🔒 Aislamiento: No interfiere con el sistema del usuario",
    "⚡ Facilidad: No requiere instalar GCC manualmente",
    "🎓 Profesionalismo: Enfoque moderno usado en la industria",
    "📦 Limpieza: No deja archivos compilados en el repositorio",
    "🚀 Automatización: Un comando para compilar y ejecutar"
]

for advantage in advantages:
    print(f"  {advantage}")
print()

# INSTRUCCIONES DE USO
print("=" * 80)
print("CÓMO EJECUTAR LA IMPLEMENTACIÓN EN C")
print("=" * 80)
print()

instructions = '''
1. USANDO DOCKER COMPOSE (Recomendado):
   
   cd ../seccion6_c_docker
   docker-compose up --build
   
   # Con valor de K personalizado:
   K_VALUE=7 docker-compose up

2. USANDO DOCKER DIRECTAMENTE:
   
   cd ../seccion6_c_docker
   docker build -t knn_classifier_c .
   docker run --rm -v $(pwd)/data:/app/data:ro -v $(pwd)/results:/app/results:rw knn_classifier_c

3. USANDO SCRIPTS AUXILIARES:
   
   cd ../seccion6_c_docker
   ./scripts/build.sh    # Construir imagen
   ./scripts/run.sh      # Ejecutar con K=5
   ./scripts/run.sh 7    # Ejecutar con K=7

4. VER RESULTADOS:
   
   cat ../seccion6_c_docker/results/output.txt
'''

print(instructions)
print()

print("=" * 80)
print("✅ TAREA 23 COMPLETADA")
print("=" * 80)
print()
print("📝 NOTA: El código C completo está en:")
print("   seccion6_c_docker/src/knn_classifier.c")
print()
print("📚 Documentación completa en:")
print("   seccion6_c_docker/README.md")
print()
"""

    # Buscar y actualizar TAREA 23
    for i, cell in enumerate(nb['cells']):
        source = ''.join(cell.get('source', []))
        
        # Si es una celda de código que contiene TAREA 23 y tiene código C
        if cell['cell_type'] == 'code' and 'TAREA 23' in source and ('knn_classifier.c' in source or 'FILE *fp' in source or '#include' in source):
            # Reemplazar con el nuevo código
            nb['cells'][i]['source'] = new_tarea23_code.split('\n')
            # Añadir salto de línea al final de cada línea excepto la última
            nb['cells'][i]['source'] = [line + '\n' if idx < len(nb['cells'][i]['source']) - 1 else line 
                                         for idx, line in enumerate(nb['cells'][i]['source'])]
            print(f"✅ Celda {i} actualizada con Docker integration")
            break
    
    # Guardar notebook actualizado
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    
    print(f"\n✅ Notebook actualizado: {notebook_path}")
    return True

if __name__ == '__main__':
    update_tarea23_to_docker()
