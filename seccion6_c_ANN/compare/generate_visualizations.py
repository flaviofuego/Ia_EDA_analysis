#!/usr/bin/env python3
"""
Generador de visualizaciones para comparación MLP C vs Python
Crea gráficas comparativas de rendimiento, accuracy, y tiempos
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import json

# Configuración de estilo
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 11
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12

def create_output_dir():
    """Crea directorio para guardar gráficas"""
    script_dir = Path(__file__).parent
    parent_dir = script_dir.parent
    output_dir = parent_dir / 'graficas'
    output_dir.mkdir(exist_ok=True)
    return output_dir

def load_results():
    """Carga resultados desde archivo de comparación"""
    script_dir = Path(__file__).parent
    comparison_file = script_dir / 'comparacion_completa.txt'
    
    if not comparison_file.exists():
        print(f"⚠ Archivo de comparación no encontrado: {comparison_file}")
        print("  Ejecuta primero: python3 compare_mlp_implementations.py")
        return None
    
    results = {}
    current_framework = None
    
    print(f"📂 Leyendo resultados desde: {comparison_file}")
    
    with open(comparison_file, 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        line = line.strip()
        
        # Detectar frameworks
        if line.startswith('C (custom):'):
            current_framework = 'C (custom)'
            results[current_framework] = {}
        elif line.startswith('Scikit-learn:'):
            current_framework = 'Scikit-learn'
            results[current_framework] = {}
        elif line.startswith('TensorFlow'):
            current_framework = 'TensorFlow'
            results[current_framework] = {}
        elif line.startswith('PyTorch:'):
            current_framework = 'PyTorch'
            results[current_framework] = {}
        
        # Extraer métricas
        if current_framework and line.startswith('Accuracy:'):
            value = float(line.split(':')[1].strip().rstrip('%'))
            results[current_framework]['accuracy'] = value
        elif current_framework and line.startswith('Balanced Accuracy:'):
            value = float(line.split(':')[1].strip().rstrip('%'))
            results[current_framework]['balanced_accuracy'] = value
        elif current_framework and line.startswith('F1-Score'):
            value = float(line.split(':')[1].strip().rstrip('%'))
            results[current_framework]['f1_macro'] = value
        elif current_framework and 'Tiempo entrenamiento:' in line:
            value = float(line.split(':')[1].strip().rstrip('s'))
            results[current_framework]['time'] = value
        elif current_framework and 'Epochs ejecutados:' in line:
            value = int(line.split(':')[1].strip())
            results[current_framework]['epochs'] = value
    
    # Validar que se cargaron todos los datos
    for fw, data in results.items():
        required_keys = ['accuracy', 'balanced_accuracy', 'f1_macro', 'time', 'epochs']
        missing = [k for k in required_keys if k not in data]
        if missing:
            print(f"⚠ Advertencia: Faltan datos para {fw}: {missing}")
    
    print(f"✓ Resultados cargados para {len(results)} frameworks")
    return results

def plot_accuracy_comparison(results, output_dir):
    """Gráfica de barras comparando métricas de accuracy"""
    frameworks = list(results.keys())
    accuracy = [results[f]['accuracy'] for f in frameworks]
    balanced_acc = [results[f]['balanced_accuracy'] for f in frameworks]
    f1_score = [results[f]['f1_macro'] for f in frameworks]
    
    x = np.arange(len(frameworks))
    width = 0.25
    
    fig, ax = plt.subplots(figsize=(12, 7))
    
    bars1 = ax.bar(x - width, accuracy, width, label='Accuracy', color='#2ecc71', alpha=0.8)
    bars2 = ax.bar(x, balanced_acc, width, label='Balanced Accuracy', color='#3498db', alpha=0.8)
    bars3 = ax.bar(x + width, f1_score, width, label='F1-Score', color='#e74c3c', alpha=0.8)
    
    ax.set_xlabel('Framework', fontweight='bold')
    ax.set_ylabel('Porcentaje (%)', fontweight='bold')
    ax.set_title('Comparación de Métricas de Accuracy\nMLP: C vs Python Frameworks', 
                 fontweight='bold', fontsize=16)
    ax.set_xticks(x)
    ax.set_xticklabels(frameworks)
    ax.legend(loc='lower right', fontsize=11)
    ax.grid(axis='y', alpha=0.3)
    ax.set_ylim([80, 95])
    
    # Agregar valores en las barras
    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height:.1f}%',
                       xy=(bar.get_x() + bar.get_width() / 2, height),
                       xytext=(0, 3),
                       textcoords="offset points",
                       ha='center', va='bottom',
                       fontsize=9)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'accuracy_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Gráfica guardada: accuracy_comparison.png")

def plot_time_comparison(results, output_dir):
    """Gráfica de barras comparando tiempos de ejecución"""
    frameworks = list(results.keys())
    times = [results[f]['time'] for f in frameworks]
    colors = ['#27ae60', '#f39c12', '#e74c3c']
    
    fig, ax = plt.subplots(figsize=(10, 7))
    
    bars = ax.barh(frameworks, times, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    
    ax.set_xlabel('Tiempo de Entrenamiento (segundos)', fontweight='bold')
    ax.set_title('Comparación de Tiempo de Entrenamiento\nMLP: C vs Python Frameworks',
                 fontweight='bold', fontsize=16)
    ax.grid(axis='x', alpha=0.3)
    
    # Agregar valores en las barras
    for i, (bar, time) in enumerate(zip(bars, times)):
        ax.text(time + 0.5, i, f'{time:.2f}s', va='center', fontweight='bold', fontsize=11)
    
    # Agregar línea de referencia
    ax.axvline(x=times[0], color='green', linestyle='--', linewidth=2, alpha=0.5, 
               label=f'Baseline C: {times[0]:.2f}s')
    ax.legend(loc='lower right')
    
    plt.tight_layout()
    plt.savefig(output_dir / 'time_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Gráfica guardada: time_comparison.png")

def plot_speedup_comparison(results, output_dir):
    """Gráfica de speedup relativo a C"""
    frameworks = list(results.keys())
    c_time = results['C (custom)']['time']
    speedups = [c_time / results[f]['time'] for f in frameworks]
    
    fig, ax = plt.subplots(figsize=(10, 7))
    
    colors = ['#27ae60', '#f39c12', '#e74c3c']
    bars = ax.bar(frameworks, speedups, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    
    ax.set_ylabel('Speedup (relativo a C)', fontweight='bold')
    ax.set_title('Speedup de C vs Python Frameworks\n(valores > 1 = C es más rápido)',
                 fontweight='bold', fontsize=16)
    ax.axhline(y=1.0, color='red', linestyle='--', linewidth=2, alpha=0.7, 
               label='Baseline (C = 1.0x)')
    ax.grid(axis='y', alpha=0.3)
    ax.legend()
    
    # Agregar valores en las barras
    for bar, speedup in zip(bars, speedups):
        height = bar.get_height()
        label = f'{speedup:.2f}x' if speedup >= 1 else f'{speedup:.2f}x\n(más lento)'
        ax.annotate(label,
                   xy=(bar.get_x() + bar.get_width() / 2, height),
                   xytext=(0, 5),
                   textcoords="offset points",
                   ha='center', va='bottom',
                   fontweight='bold', fontsize=11)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'speedup_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Gráfica guardada: speedup_comparison.png")

def plot_epochs_comparison(results, output_dir):
    """Gráfica comparando número de epochs ejecutados"""
    frameworks = list(results.keys())
    epochs = [results[f]['epochs'] for f in frameworks]
    
    fig, ax = plt.subplots(figsize=(10, 7))
    
    colors = ['#3498db', '#9b59b6', '#e67e22']
    bars = ax.bar(frameworks, epochs, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    
    ax.set_ylabel('Número de Epochs', fontweight='bold')
    ax.set_title('Epochs Ejecutados Antes de Early Stopping\nMLP: C vs Python Frameworks',
                 fontweight='bold', fontsize=16)
    ax.grid(axis='y', alpha=0.3)
    
    # Agregar valores en las barras
    for bar, epoch in zip(bars, epochs):
        height = bar.get_height()
        ax.annotate(f'{epoch}',
                   xy=(bar.get_x() + bar.get_width() / 2, height),
                   xytext=(0, 5),
                   textcoords="offset points",
                   ha='center', va='bottom',
                   fontweight='bold', fontsize=12)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'epochs_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Gráfica guardada: epochs_comparison.png")

def plot_efficiency_scatter(results, output_dir):
    """Gráfica de dispersión: Accuracy vs Tiempo (eficiencia)"""
    frameworks = list(results.keys())
    times = [results[f]['time'] for f in frameworks]
    accuracies = [results[f]['accuracy'] for f in frameworks]
    colors = ['#27ae60', '#f39c12', '#e74c3c']
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    for i, (fw, time, acc) in enumerate(zip(frameworks, times, accuracies)):
        ax.scatter(time, acc, s=500, alpha=0.6, color=colors[i], 
                  edgecolors='black', linewidth=2, label=fw)
        ax.annotate(fw, (time, acc), xytext=(10, 10), 
                   textcoords='offset points', fontsize=11, fontweight='bold',
                   bbox=dict(boxstyle='round,pad=0.5', facecolor=colors[i], alpha=0.3))
    
    ax.set_xlabel('Tiempo de Entrenamiento (segundos)', fontweight='bold')
    ax.set_ylabel('Accuracy (%)', fontweight='bold')
    ax.set_title('Eficiencia: Accuracy vs Tiempo de Entrenamiento\n(Esquina superior izquierda = Mejor)',
                 fontweight='bold', fontsize=16)
    ax.grid(True, alpha=0.3)
    ax.set_xlim([0, max(times) * 1.1])
    ax.set_ylim([min(accuracies) - 0.5, max(accuracies) + 0.5])
    
    # Líneas de referencia
    ax.axvline(x=results['C (custom)']['time'], color='green', 
              linestyle='--', alpha=0.5, label='Tiempo C')
    ax.axhline(y=results['C (custom)']['accuracy'], color='green', 
              linestyle='--', alpha=0.5, label='Accuracy C')
    
    plt.tight_layout()
    plt.savefig(output_dir / 'efficiency_scatter.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Gráfica guardada: efficiency_scatter.png")

def plot_radar_chart(results, output_dir):
    """Gráfica de radar comparando múltiples métricas normalizadas"""
    frameworks = list(results.keys())
    
    # Métricas a comparar (invertir tiempo para que más bajo sea mejor)
    categories = ['Accuracy', 'Balanced\nAccuracy', 'F1-Score', 'Velocidad\n(inv)']
    
    # Normalizar valores (0-100)
    data = []
    for fw in frameworks:
        acc = results[fw]['accuracy']
        bal_acc = results[fw]['balanced_accuracy']
        f1 = results[fw]['f1_macro']
        # Invertir tiempo: convertir a velocidad relativa
        speed = 100 * (1 / results[fw]['time']) / max([1 / results[f]['time'] for f in frameworks])
        data.append([acc, bal_acc, f1, speed])
    
    # Configurar radar
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    data = [d + [d[0]] for d in data]  # Cerrar el polígono
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))
    
    colors = ['#27ae60', '#f39c12', '#e74c3c']
    for i, (fw, values) in enumerate(zip(frameworks, data)):
        ax.plot(angles, values, 'o-', linewidth=2, label=fw, color=colors[i])
        ax.fill(angles, values, alpha=0.25, color=colors[i])
    
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=11, fontweight='bold')
    ax.set_ylim(0, 100)
    ax.set_title('Comparación Multi-Métrica\nMLP: C vs Python Frameworks',
                 fontweight='bold', fontsize=16, pad=20)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=11)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'radar_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Gráfica guardada: radar_comparison.png")

def plot_combined_dashboard(results, output_dir):
    """Dashboard combinado con múltiples gráficas"""
    frameworks = list(results.keys())
    
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(2, 3, hspace=0.3, wspace=0.3)
    
    # 1. Accuracy
    ax1 = fig.add_subplot(gs[0, 0])
    accuracies = [results[f]['accuracy'] for f in frameworks]
    colors1 = ['#27ae60', '#f39c12', '#e74c3c']
    bars1 = ax1.bar(frameworks, accuracies, color=colors1, alpha=0.8)
    ax1.set_ylabel('Accuracy (%)', fontweight='bold')
    ax1.set_title('Accuracy', fontweight='bold')
    ax1.grid(axis='y', alpha=0.3)
    ax1.set_ylim([90, 95])
    for bar, acc in zip(bars1, accuracies):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                f'{acc:.2f}%', ha='center', fontsize=9, fontweight='bold')
    
    # 2. Tiempo
    ax2 = fig.add_subplot(gs[0, 1])
    times = [results[f]['time'] for f in frameworks]
    bars2 = ax2.barh(frameworks, times, color=colors1, alpha=0.8)
    ax2.set_xlabel('Tiempo (s)', fontweight='bold')
    ax2.set_title('Tiempo de Entrenamiento', fontweight='bold')
    ax2.grid(axis='x', alpha=0.3)
    for i, (bar, time) in enumerate(zip(bars2, times)):
        ax2.text(time + 0.5, i, f'{time:.2f}s', va='center', fontsize=9, fontweight='bold')
    
    # 3. F1-Score
    ax3 = fig.add_subplot(gs[0, 2])
    f1_scores = [results[f]['f1_macro'] for f in frameworks]
    bars3 = ax3.bar(frameworks, f1_scores, color=colors1, alpha=0.8)
    ax3.set_ylabel('F1-Score (%)', fontweight='bold')
    ax3.set_title('F1-Score', fontweight='bold')
    ax3.grid(axis='y', alpha=0.3)
    ax3.set_ylim([85, 95])
    for bar, f1 in zip(bars3, f1_scores):
        ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                f'{f1:.2f}%', ha='center', fontsize=9, fontweight='bold')
    
    # 4. Speedup
    ax4 = fig.add_subplot(gs[1, 0])
    c_time = results['C (custom)']['time']
    speedups = [c_time / results[f]['time'] for f in frameworks]
    bars4 = ax4.bar(frameworks, speedups, color=colors1, alpha=0.8)
    ax4.set_ylabel('Speedup (vs C)', fontweight='bold')
    ax4.set_title('Speedup Relativo', fontweight='bold')
    ax4.axhline(y=1.0, color='red', linestyle='--', alpha=0.7)
    ax4.grid(axis='y', alpha=0.3)
    for bar, speedup in zip(bars4, speedups):
        ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                f'{speedup:.2f}x', ha='center', fontsize=9, fontweight='bold')
    
    # 5. Epochs
    ax5 = fig.add_subplot(gs[1, 1])
    epochs = [results[f]['epochs'] for f in frameworks]
    bars5 = ax5.bar(frameworks, epochs, color=colors1, alpha=0.8)
    ax5.set_ylabel('Epochs', fontweight='bold')
    ax5.set_title('Epochs Ejecutados', fontweight='bold')
    ax5.grid(axis='y', alpha=0.3)
    for bar, epoch in zip(bars5, epochs):
        ax5.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f'{epoch}', ha='center', fontsize=9, fontweight='bold')
    
    # 6. Resumen textual
    ax6 = fig.add_subplot(gs[1, 2])
    ax6.axis('off')
    summary_text = f"""
    RESUMEN COMPARATIVO
    {'='*30}
    
    Mejor Accuracy:
      → {max(frameworks, key=lambda f: results[f]['accuracy'])}
      → {max(accuracies):.2f}%
    
    Más Rápido:
      → C (custom)
      → {min(times):.2f}s
    
    Speedups:
      → C vs Sklearn: {speedups[1]:.2f}x
      → C vs PyTorch: {speedups[2]:.2f}x
    
    Conclusión:
      → C ofrece el mejor
        balance entre velocidad
        y precisión
    """
    ax6.text(0.1, 0.5, summary_text, fontsize=10, verticalalignment='center',
            family='monospace', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    fig.suptitle('Dashboard Comparativo: MLP C vs Python Frameworks', 
                fontsize=18, fontweight='bold', y=0.98)
    
    plt.savefig(output_dir / 'dashboard_completo.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Gráfica guardada: dashboard_completo.png")

def main():
    """Función principal"""
    print("="*80)
    print("GENERACIÓN DE VISUALIZACIONES")
    print("="*80)
    
    # Crear directorio de salida
    output_dir = create_output_dir()
    print(f"\n📁 Directorio de salida: {output_dir}")
    
    # Cargar resultados
    print("\n📊 Cargando resultados de comparación...")
    results = load_results()
    
    if results is None or len(results) == 0:
        print("\n❌ ERROR: No se pudieron cargar los resultados")
        print("   Ejecuta primero: python3 compare_mlp_implementations.py")
        return
    
    # Generar gráficas
    print("\n🎨 Generando visualizaciones...\n")
    
    plot_accuracy_comparison(results, output_dir)
    plot_time_comparison(results, output_dir)
    plot_speedup_comparison(results, output_dir)
    plot_epochs_comparison(results, output_dir)
    plot_efficiency_scatter(results, output_dir)
    plot_radar_chart(results, output_dir)
    plot_combined_dashboard(results, output_dir)
    
    print("\n" + "="*80)
    print("✅ VISUALIZACIONES COMPLETADAS")
    print("="*80)
    print(f"\nArchivos generados en: {output_dir}/")
    print("\nGráficas creadas:")
    print("  1. accuracy_comparison.png    - Comparación de métricas")
    print("  2. time_comparison.png        - Tiempos de entrenamiento")
    print("  3. speedup_comparison.png     - Speedups relativos")
    print("  4. epochs_comparison.png      - Epochs ejecutados")
    print("  5. efficiency_scatter.png     - Eficiencia (accuracy vs tiempo)")
    print("  6. radar_comparison.png       - Comparación multi-métrica")
    print("  7. dashboard_completo.png     - Dashboard combinado")
    print("\n" + "="*80)

if __name__ == "__main__":
    main()
