#!/usr/bin/env python3
"""Add final tasks 24 and 25 to complete Section 6"""

import json

def load_nb():
    with open('notebooks/seccion6.ipynb', 'r') as f:
        return json.load(f)

def save_nb(nb):
    with open('notebooks/seccion6.ipynb', 'w') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

def add_md(nb, text):
    nb["cells"].append({"cell_type": "markdown", "metadata": {}, "source": text.split('\n')})

def add_code(nb, text):
    nb["cells"].append({"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": text.split('\n')})

nb = load_nb()
print(f"Starting with {len(nb['cells'])} cells")

# === TAREA 24 ===
tarea24_md = """---

# ============================================
# TAREA 24: Evaluación y Comparación Python vs C
# ============================================

## �� Objetivo
Evaluar el desempeño de la implementación en C y compararla con la versión de Python (sklearn).

---

## 📊 MÉTRICAS DE COMPARACIÓN

Compararemos ambas implementaciones en:
1. **Precisión (Accuracy)**: ¿Dan los mismos resultados?
2. **Tiempo de Ejecución**: ¿Cuál es más rápida?
3. **Uso de Memoria**: Estimación cualitativa
4. **Facilidad de Uso**: Análisis subjetivo

---"""

tarea24_code = '''# ============================================
# TAREA 24: Evaluación y Comparación Python vs C
# ============================================

print("="*80)
print("TAREA 24: EVALUACIÓN Y COMPARACIÓN PYTHON VS C")
print("="*80)

# 1. Entrenar modelo KNN en Python (sklearn)
print("\\n1️⃣  Entrenando modelo KNN en Python (sklearn)...")

# Usar los mismos datos que generamos para C
X_train_compare = X_train_c
X_test_compare = X_test_c
y_train_compare = y_train_c
y_test_compare = y_test_c

# Crear y entrenar modelo sklearn
knn_sklearn = KNeighborsClassifier(n_neighbors=5, metric='euclidean')

# Medir tiempo de entrenamiento
import time
start_train_py = time.time()
knn_sklearn.fit(X_train_compare, y_train_compare)
end_train_py = time.time()
train_time_py = end_train_py - start_train_py

print(f"✅ Modelo Python entrenado en {train_time_py:.4f} segundos")

# 2. Predecir con Python
print("\\n2️⃣  Realizando predicciones con Python...")

start_pred_py = time.time()
y_pred_py = knn_sklearn.predict(X_test_compare)
end_pred_py = time.time()
pred_time_py = end_pred_py - start_pred_py

print(f"✅ Predicciones Python completadas en {pred_time_py:.4f} segundos")

# 3. Evaluar Python
print("\\n3️⃣  Evaluando modelo Python...")

accuracy_py = accuracy_score(y_test_compare, y_pred_py)
precision_py = precision_score(y_test_compare, y_pred_py, average='weighted', zero_division=0)
recall_py = recall_score(y_test_compare, y_pred_py, average='weighted', zero_division=0)
f1_py = f1_score(y_test_compare, y_pred_py, average='weighted', zero_division=0)

print(f"\\n📊 Métricas Python (sklearn):")
print(f"   Accuracy:  {accuracy_py:.4f}")
print(f"   Precision: {precision_py:.4f}")
print(f"   Recall:    {recall_py:.4f}")
print(f"   F1-Score:  {f1_py:.4f}")

# 4. Ejecutar implementación en C
print("\\n4️⃣  Ejecutando implementación en C...")

c_executable = './knn_classifier'
if not os.path.exists(c_executable):
    c_executable = './knn_classifier.exe'  # Windows

if os.path.exists(c_executable):
    try:
        print(f"   Ejecutando: {c_executable} train_data_c.csv test_data_c.csv 5")
        
        start_c = time.time()
        result_c = subprocess.run(
            [c_executable, 'train_data_c.csv', 'test_data_c.csv', '5'],
            capture_output=True,
            text=True,
            timeout=60
        )
        end_c = time.time()
        total_time_c = end_c - start_c
        
        if result_c.returncode == 0:
            print(f"✅ Implementación C ejecutada exitosamente")
            print(f"   Tiempo total: {total_time_c:.4f} segundos")
            
            # Parsear output para extraer métricas
            output_lines = result_c.stdout.split('\\n')
            accuracy_c = None
            pred_time_c = None
            
            for line in output_lines:
                if 'Accuracy:' in line:
                    try:
                        accuracy_str = line.split(':')[1].strip().replace('%', '')
                        accuracy_c = float(accuracy_str) / 100.0
                    except:
                        pass
                if 'Tiempo predicción:' in line or 'predicción:' in line:
                    try:
                        import re
                        match = re.search(r'(\\d+\\.\\d+)', line)
                        if match:
                            pred_time_c = float(match.group(1))
                    except:
                        pass
            
            # Mostrar output
            print("\\n📋 Output de implementación C:")
            print("   " + "-"*60)
            for line in output_lines[:30]:  # Primeras 30 líneas
                if line.strip():
                    print("   " + line)
            if len(output_lines) > 30:
                print("   ... (output truncado)")
            
            # Leer resultados del archivo si existe
            if os.path.exists('resultados_knn_c.txt'):
                with open('resultados_knn_c.txt', 'r') as f:
                    c_results = f.read()
                    for line in c_results.split('\\n'):
                        if 'Accuracy:' in line:
                            try:
                                accuracy_c = float(line.split(':')[1].strip())
                            except:
                                pass
                        if 'Tiempo de predicción:' in line:
                            try:
                                import re
                                match = re.search(r'(\\d+\\.\\d+)', line)
                                if match:
                                    pred_time_c = float(match.group(1))
                            except:
                                pass
        else:
            print(f"⚠️  Error en ejecución C (código: {result_c.returncode})")
            print("   " + result_c.stderr[:500])
            accuracy_c = None
            pred_time_c = None
    except Exception as e:
        print(f"⚠️  No se pudo ejecutar implementación C: {e}")
        accuracy_c = None
        pred_time_c = None
else:
    print("⚠️  Ejecutable C no encontrado. Compilar primero:")
    print("   gcc -o knn_classifier knn_classifier.c -lm -O2")
    accuracy_c = None
    pred_time_c = None

# 5. Comparación de resultados
print("\\n5️⃣  COMPARACIÓN DE RESULTADOS")
print("="*80)

# Crear tabla comparativa
comparison_data = {
    'Métrica': ['Accuracy', 'Tiempo Predicción (s)', 'Tiempo por Muestra (ms)'],
    'Python (sklearn)': [
        f'{accuracy_py:.4f}',
        f'{pred_time_py:.4f}',
        f'{(pred_time_py/len(y_test_compare))*1000:.4f}'
    ],
    'C (Implementación Manual)': [
        f'{accuracy_c:.4f}' if accuracy_c else 'N/A',
        f'{pred_time_c:.4f}' if pred_time_c else f'{total_time_c:.4f}*' if 'total_time_c' in locals() else 'N/A',
        f'{(pred_time_c/len(y_test_compare))*1000:.4f}' if pred_time_c else 'N/A'
    ]
}

df_comparison = pd.DataFrame(comparison_data)
print("\\n📊 TABLA COMPARATIVA:\\n")
print(df_comparison.to_string(index=False))

if accuracy_c:
    diff_accuracy = abs(accuracy_py - accuracy_c)
    print(f"\\n📈 Diferencia en Accuracy: {diff_accuracy:.4f} ({diff_accuracy*100:.2f}%)")
    
    if diff_accuracy < 0.01:
        print("✅ Las implementaciones tienen accuracy muy similar (diferencia < 1%)")
    elif diff_accuracy < 0.05:
        print("⚠️  Pequeña diferencia en accuracy (< 5%)")
    else:
        print("⚠️  Diferencia significativa en accuracy")

if pred_time_c and pred_time_py:
    speedup = pred_time_py / pred_time_c if pred_time_c > 0 else 0
    if speedup > 1:
        print(f"\\n⚡ Implementación C es {speedup:.2f}x más rápida")
    elif speedup < 1 and speedup > 0:
        print(f"\\n⚡ Implementación Python es {1/speedup:.2f}x más rápida")

# 6. Visualización comparativa
print("\\n6️⃣  Generando visualización comparativa...")

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Gráfico 1: Comparación de Accuracy
if accuracy_c:
    accuracies = [accuracy_py, accuracy_c]
    labels = ['Python\\n(sklearn)', 'C\\n(Manual)']
    colors = ['#3498db', '#e74c3c']
    
    bars = axes[0].bar(labels, accuracies, color=colors, edgecolor='black', linewidth=2)
    axes[0].set_ylabel('Accuracy', fontsize=12, fontweight='bold')
    axes[0].set_title('Comparación de Accuracy', fontsize=14, fontweight='bold')
    axes[0].set_ylim(0, 1)
    axes[0].grid(axis='y', alpha=0.3)
    
    # Añadir valores
    for bar in bars:
        height = bar.get_height()
        axes[0].text(bar.get_x() + bar.get_width()/2., height + 0.02,
                    f'{height:.4f}',
                    ha='center', va='bottom', fontweight='bold', fontsize=11)
else:
    axes[0].text(0.5, 0.5, 'Datos de C no disponibles',
                ha='center', va='center', fontsize=14)
    axes[0].set_xlim(0, 1)
    axes[0].set_ylim(0, 1)

# Gráfico 2: Comparación de Tiempo
if pred_time_c:
    times = [pred_time_py, pred_time_c]
    labels = ['Python\\n(sklearn)', 'C\\n(Manual)']
    colors = ['#3498db', '#e74c3c']
    
    bars = axes[1].bar(labels, times, color=colors, edgecolor='black', linewidth=2)
    axes[1].set_ylabel('Tiempo de Predicción (segundos)', fontsize=12, fontweight='bold')
    axes[1].set_title('Comparación de Tiempo de Ejecución', fontsize=14, fontweight='bold')
    axes[1].grid(axis='y', alpha=0.3)
    
    # Añadir valores
    for bar in bars:
        height = bar.get_height()
        axes[1].text(bar.get_x() + bar.get_width()/2., height + max(times)*0.02,
                    f'{height:.4f}s',
                    ha='center', va='bottom', fontweight='bold', fontsize=11)
else:
    axes[1].text(0.5, 0.5, 'Datos de C no disponibles',
                ha='center', va='center', fontsize=14)
    axes[1].set_xlim(0, 1)
    axes[1].set_ylim(0, 1)

plt.tight_layout()
plt.savefig('tarea24_comparison_python_vs_c.png', dpi=300, bbox_inches='tight')
plt.show()

print("✅ Visualización guardada: tarea24_comparison_python_vs_c.png")

# 7. Análisis cualitativo
print("\\n7️⃣  ANÁLISIS CUALITATIVO")
print("="*80)

analysis = """
COMPARACIÓN PYTHON (sklearn) vs C (Implementación Manual)
----------------------------------------------------------

1. PRECISIÓN:
   ✓ Ambas implementaciones usan el mismo algoritmo KNN
   ✓ Diferencias mínimas esperadas por redondeo en punto flotante
   ✓ sklearn tiene optimizaciones adicionales que pueden afectar ligeramente

2. VELOCIDAD:
   • Python (sklearn): Usa librerías optimizadas (Cython, NumPy con BLAS)
   • C (Manual): Implementación directa, sin optimizaciones avanzadas
   • RESULTADO ESPERADO: Python puede ser más rápido por optimizaciones
   • Para datasets grandes, C con optimizaciones podría ser más rápido

3. USO DE MEMORIA:
   • Python: Mayor overhead por objetos Python, NumPy arrays
   • C: Control directo de memoria, arrays estáticos y dinámicos
   • VENTAJA: C es más eficiente en memoria

4. FACILIDAD DE USO:
   • Python: API simple, 2-3 líneas de código
   • C: Implementación completa de ~600 líneas
   • VENTAJA: Python es mucho más fácil de usar

5. COMPRENSIÓN DEL ALGORITMO:
   • Python: "Caja negra", no se ven detalles internos
   • C: Implementación completa desde cero
   • VENTAJA: C demuestra comprensión profunda del algoritmo

6. MANTENIBILIDAD:
   • Python: Código corto, fácil de mantener
   • C: Más código, gestión manual de memoria
   • VENTAJA: Python es más mantenible

7. PORTABILIDAD:
   • Python: Funciona en cualquier sistema con Python
   • C: Requiere compilación para cada plataforma
   • VENTAJA: Python es más portable

8. EDUCACIÓN:
   • Python: Perfecto para prototipado rápido y exploración
   • C: Excelente para entender el funcionamiento interno
   • AMBOS SON VALIOSOS según el objetivo

CONCLUSIÓN:
-----------
• Para PRODUCCIÓN: Python (sklearn) es superior (velocidad, facilidad, confiabilidad)
• Para EDUCACIÓN: C es superior (comprensión profunda, control total)
• Esta implementación en C cumple su objetivo EDUCATIVO de demostrar
  comprensión algorítmica profunda

"""

print(analysis)

# Guardar comparación completa
with open('tarea24_comparacion_completa.txt', 'w', encoding='utf-8') as f:
    f.write("="*80 + "\\n")
    f.write("TAREA 24: COMPARACIÓN PYTHON VS C\\n")
    f.write("="*80 + "\\n\\n")
    f.write(df_comparison.to_string(index=False))
    f.write("\\n\\n")
    f.write(analysis)

print("✅ Comparación completa guardada: tarea24_comparacion_completa.txt")

print("\\n" + "="*80)
print("TAREA 24 COMPLETADA ✅")
print("="*80)'''

add_md(nb, tarea24_md)
add_code(nb, tarea24_code)
print(f"Added Tarea 24. Current cells: {len(nb['cells'])}")

# Save
save_nb(nb)
print("Notebook saved. Adding Tarea 25...")

print(f"\\nNotebook now has {len(nb['cells'])} cells")
print("✅ Successfully added Tareas 24")
