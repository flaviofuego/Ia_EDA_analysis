#!/usr/bin/env python3
"""
Visualizador de datos de entrenamiento del MLP en C
Lee el archivo training_history.csv y genera gráficas detalladas
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import sys

def load_training_history(csv_path):
    """Carga el historial de entrenamiento desde CSV"""
    if not Path(csv_path).exists():
        print(f"❌ Error: No se encontró el archivo {csv_path}")
        print("   Ejecuta primero el modelo en C para generar los datos.")
        return None, None
    
    # Leer datos de entrenamiento
    training_data = []
    with open(csv_path, 'r') as f:
        lines = f.readlines()
        
    # Encontrar donde terminan los datos de épocas
    data_end_idx = 0
    for i, line in enumerate(lines[1:], 1):  # Skip header
        if line.strip().startswith('#'):
            data_end_idx = i
            break
    
    if data_end_idx == 0:
        data_end_idx = len(lines)
    
    # Leer datos de épocas
    df_epochs = pd.read_csv(csv_path, nrows=data_end_idx-1)
    
    # Leer métricas finales si existen
    final_metrics = None
    for i, line in enumerate(lines):
        if line.strip().startswith('# accuracy,'):
            if i + 1 < len(lines):
                values = lines[i + 1].strip().split(',')
                if len(values) == 6:
                    final_metrics = {
                        'accuracy': float(values[0]),
                        'balanced_accuracy': float(values[1]),
                        'f1_score': float(values[2]),
                        'precision': float(values[3]),
                        'recall': float(values[4]),
                        'total_time': float(values[5])
                    }
            break
    
    return df_epochs, final_metrics

def plot_training_curves(df, output_dir):
    """Genera gráficas de curvas de entrenamiento"""
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Curvas de Entrenamiento del MLP en C', fontsize=16, fontweight='bold')
    
    # 1. Loss curves
    ax = axes[0, 0]
    ax.plot(df['epoch'], df['train_loss'], 'b-', label='Train Loss', linewidth=2)
    ax.plot(df['epoch'], df['val_loss'], 'r-', label='Validation Loss', linewidth=2)
    ax.set_xlabel('Epoch')
    ax.set_ylabel('Loss')
    ax.set_title('Pérdida durante el Entrenamiento')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # 2. Validation Accuracy
    ax = axes[0, 1]
    ax.plot(df['epoch'], df['val_accuracy'] * 100, 'g-', linewidth=2)
    ax.set_xlabel('Epoch')
    ax.set_ylabel('Accuracy (%)')
    ax.set_title('Accuracy de Validación')
    ax.grid(True, alpha=0.3)
    ax.axhline(y=df['val_accuracy'].max() * 100, color='r', linestyle='--', 
               alpha=0.5, label=f'Max: {df["val_accuracy"].max()*100:.2f}%')
    ax.legend()
    
    # 3. Learning Rate Decay
    ax = axes[1, 0]
    ax.plot(df['epoch'], df['learning_rate'], 'purple', linewidth=2)
    ax.set_xlabel('Epoch')
    ax.set_ylabel('Learning Rate')
    ax.set_title('Decaimiento del Learning Rate')
    ax.grid(True, alpha=0.3)
    ax.set_yscale('log')
    
    # 4. Tiempo acumulado
    ax = axes[1, 1]
    ax.plot(df['epoch'], df['elapsed_time'], 'orange', linewidth=2)
    ax.set_xlabel('Epoch')
    ax.set_ylabel('Tiempo (segundos)')
    ax.set_title('Tiempo de Entrenamiento Acumulado')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    output_path = output_dir / 'training_curves.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Gráfica guardada: {output_path}")

def plot_loss_comparison(df, output_dir):
    """Gráfica detallada de comparación de loss"""
    fig, ax = plt.subplots(figsize=(12, 7))
    
    ax.plot(df['epoch'], df['train_loss'], 'b-', label='Train Loss', 
            linewidth=2, marker='o', markersize=4, alpha=0.7)
    ax.plot(df['epoch'], df['val_loss'], 'r-', label='Validation Loss', 
            linewidth=2, marker='s', markersize=4, alpha=0.7)
    
    # Marcar el mejor epoch
    best_epoch = df['val_loss'].idxmin() + 1
    best_val_loss = df['val_loss'].min()
    ax.axvline(x=best_epoch, color='green', linestyle='--', alpha=0.5,
               label=f'Mejor epoch: {best_epoch}')
    ax.scatter([best_epoch], [best_val_loss], color='green', s=100, 
               zorder=5, marker='*')
    
    ax.set_xlabel('Epoch', fontweight='bold')
    ax.set_ylabel('Loss', fontweight='bold')
    ax.set_title('Comparación de Loss: Train vs Validation', 
                 fontweight='bold', fontsize=14)
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    output_path = output_dir / 'loss_comparison.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Gráfica guardada: {output_path}")

def plot_metrics_summary(df, final_metrics, output_dir):
    """Dashboard con métricas finales"""
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
    
    # 1. Loss evolution (grande)
    ax1 = fig.add_subplot(gs[0, :2])
    ax1.plot(df['epoch'], df['train_loss'], 'b-', label='Train', linewidth=2)
    ax1.plot(df['epoch'], df['val_loss'], 'r-', label='Validation', linewidth=2)
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Loss')
    ax1.set_title('Evolución del Loss', fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 2. Métricas finales (texto)
    ax2 = fig.add_subplot(gs[0, 2])
    ax2.axis('off')
    if final_metrics:
        metrics_text = f"""
        MÉTRICAS FINALES (TEST)
        {'='*25}
        
        Accuracy:        {final_metrics['accuracy']*100:.2f}%
        Balanced Acc:    {final_metrics['balanced_accuracy']*100:.2f}%
        F1-Score:        {final_metrics['f1_score']*100:.2f}%
        Precision:       {final_metrics['precision']*100:.2f}%
        Recall:          {final_metrics['recall']*100:.2f}%
        
        Tiempo Total:    {final_metrics['total_time']:.2f}s
        Epochs:          {len(df)}
        """
    else:
        metrics_text = "Métricas finales\nno disponibles"
    
    ax2.text(0.1, 0.5, metrics_text, fontsize=11, verticalalignment='center',
            family='monospace', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
    
    # 3. Validation Accuracy
    ax3 = fig.add_subplot(gs[1, :])
    ax3.plot(df['epoch'], df['val_accuracy'] * 100, 'g-', linewidth=2, marker='o', markersize=3)
    ax3.axhline(y=df['val_accuracy'].max() * 100, color='r', linestyle='--', alpha=0.5)
    ax3.fill_between(df['epoch'], 0, df['val_accuracy'] * 100, alpha=0.2, color='green')
    ax3.set_xlabel('Epoch')
    ax3.set_ylabel('Accuracy (%)')
    ax3.set_title('Accuracy de Validación', fontweight='bold')
    ax3.grid(True, alpha=0.3)
    ax3.set_ylim([df['val_accuracy'].min() * 100 - 1, df['val_accuracy'].max() * 100 + 1])
    
    # 4. Learning Rate
    ax4 = fig.add_subplot(gs[2, 0])
    ax4.plot(df['epoch'], df['learning_rate'], 'purple', linewidth=2)
    ax4.set_xlabel('Epoch')
    ax4.set_ylabel('Learning Rate')
    ax4.set_title('Learning Rate Decay', fontweight='bold')
    ax4.grid(True, alpha=0.3)
    ax4.set_yscale('log')
    
    # 5. Tiempo por epoch
    ax5 = fig.add_subplot(gs[2, 1])
    time_per_epoch = df['elapsed_time'].diff().fillna(df['elapsed_time'].iloc[0])
    ax5.bar(df['epoch'], time_per_epoch, color='orange', alpha=0.7)
    ax5.set_xlabel('Epoch')
    ax5.set_ylabel('Tiempo (s)')
    ax5.set_title('Tiempo por Epoch', fontweight='bold')
    ax5.grid(True, alpha=0.3, axis='y')
    
    # 6. Overfitting indicator
    ax6 = fig.add_subplot(gs[2, 2])
    gap = df['val_loss'] - df['train_loss']
    ax6.plot(df['epoch'], gap, 'red', linewidth=2)
    ax6.axhline(y=0, color='black', linestyle='-', alpha=0.3)
    ax6.fill_between(df['epoch'], 0, gap, where=(gap > 0), alpha=0.3, color='red', label='Overfitting')
    ax6.fill_between(df['epoch'], 0, gap, where=(gap <= 0), alpha=0.3, color='blue', label='Underfitting')
    ax6.set_xlabel('Epoch')
    ax6.set_ylabel('Val Loss - Train Loss')
    ax6.set_title('Gap Train/Validation', fontweight='bold')
    ax6.legend(fontsize=8)
    ax6.grid(True, alpha=0.3)
    
    fig.suptitle('Dashboard de Entrenamiento - MLP en C', fontsize=18, fontweight='bold', y=0.995)
    
    output_path = output_dir / 'training_dashboard.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Gráfica guardada: {output_path}")

def generate_summary_report(df, final_metrics, output_dir):
    """Genera reporte de texto con estadísticas"""
    output_path = output_dir / 'training_summary.txt'
    
    with open(output_path, 'w') as f:
        f.write("="*80 + "\n")
        f.write("RESUMEN DE ENTRENAMIENTO - MLP EN C\n")
        f.write("="*80 + "\n\n")
        
        f.write("DATOS DE ENTRENAMIENTO:\n")
        f.write(f"  Total de epochs: {len(df)}\n")
        f.write(f"  Tiempo total: {df['elapsed_time'].iloc[-1]:.2f} segundos\n")
        f.write(f"  Tiempo promedio por epoch: {df['elapsed_time'].diff().mean():.3f} segundos\n\n")
        
        f.write("PÉRDIDA (LOSS):\n")
        f.write(f"  Train Loss final: {df['train_loss'].iloc[-1]:.6f}\n")
        f.write(f"  Val Loss final: {df['val_loss'].iloc[-1]:.6f}\n")
        f.write(f"  Val Loss mínimo: {df['val_loss'].min():.6f} (epoch {df['val_loss'].idxmin()+1})\n")
        f.write(f"  Gap (Val-Train) final: {df['val_loss'].iloc[-1] - df['train_loss'].iloc[-1]:.6f}\n\n")
        
        f.write("ACCURACY DE VALIDACIÓN:\n")
        f.write(f"  Accuracy final: {df['val_accuracy'].iloc[-1]*100:.2f}%\n")
        f.write(f"  Accuracy máximo: {df['val_accuracy'].max()*100:.2f}% (epoch {df['val_accuracy'].idxmax()+1})\n")
        f.write(f"  Accuracy mínimo: {df['val_accuracy'].min()*100:.2f}%\n")
        f.write(f"  Mejora total: {(df['val_accuracy'].iloc[-1] - df['val_accuracy'].iloc[0])*100:.2f}%\n\n")
        
        f.write("LEARNING RATE:\n")
        f.write(f"  Inicial: {df['learning_rate'].iloc[0]:.6f}\n")
        f.write(f"  Final: {df['learning_rate'].iloc[-1]:.6f}\n")
        f.write(f"  Ratio de decay: {df['learning_rate'].iloc[-1] / df['learning_rate'].iloc[0]:.4f}\n\n")
        
        if final_metrics:
            f.write("="*80 + "\n")
            f.write("MÉTRICAS FINALES (TEST SET)\n")
            f.write("="*80 + "\n\n")
            f.write(f"  Accuracy:           {final_metrics['accuracy']*100:.2f}%\n")
            f.write(f"  Balanced Accuracy:  {final_metrics['balanced_accuracy']*100:.2f}%\n")
            f.write(f"  F1-Score:           {final_metrics['f1_score']*100:.2f}%\n")
            f.write(f"  Precision (Macro):  {final_metrics['precision']*100:.2f}%\n")
            f.write(f"  Recall (Macro):     {final_metrics['recall']*100:.2f}%\n")
            f.write(f"  Tiempo total:       {final_metrics['total_time']:.2f} segundos\n")
    
    print(f"✓ Reporte guardado: {output_path}")

def main():
    print("="*80)
    print("VISUALIZADOR DE ENTRENAMIENTO - MLP EN C")
    print("="*80)
    
    # Rutas
    script_dir = Path(__file__).parent
    parent_dir = script_dir.parent
    csv_path = parent_dir / 'tasks' / 'training_history.csv'
    output_dir = parent_dir / 'graficas'
    output_dir.mkdir(exist_ok=True)
    
    # Cargar datos
    print(f"\n📂 Leyendo datos desde: {csv_path}")
    df, final_metrics = load_training_history(csv_path)
    
    if df is None:
        return
    
    print(f"✓ Datos cargados: {len(df)} epochs")
    if final_metrics:
        print(f"✓ Métricas finales disponibles")
    
    # Generar visualizaciones
    print("\n🎨 Generando visualizaciones...")
    plot_training_curves(df, output_dir)
    plot_loss_comparison(df, output_dir)
    plot_metrics_summary(df, final_metrics, output_dir)
    generate_summary_report(df, final_metrics, output_dir)
    
    print("\n"+"="*80)
    print("✅ VISUALIZACIONES COMPLETADAS")
    print("="*80)
    print(f"Archivos generados en: {output_dir}/")
    print("  1. training_curves.png     - Curvas de entrenamiento (4 paneles)")
    print("  2. loss_comparison.png     - Comparación detallada de loss")
    print("  3. training_dashboard.png  - Dashboard completo")
    print("  4. training_summary.txt    - Reporte estadístico")
    print("="*80)

if __name__ == "__main__":
    main()
