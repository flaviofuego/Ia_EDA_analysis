/*
 * ============================================================================
 * K-NEAREST NEIGHBORS (KNN) CLASSIFIER - IMPLEMENTATION IN C
 * ============================================================================
 * 
 * Proyecto: Análisis y Predicción de Desempeño en Inglés - Pruebas Saber 11
 * Universidad del Norte - Inteligencia Artificial (ELP 8012)
 * Estudiantes: Flavio Arregoces, Cristian Gonzales
 * Fecha: Noviembre 2025
 * 
 * Este archivo implementa un clasificador KNN desde cero en C para demostrar
 * comprensión profunda del algoritmo.
 * 
 * Características:
 * - K-Nearest Neighbors con k=5
 * - Distancia Euclidiana (L2)
 * - Votación por mayoría simple
 * - Soporte para clasificación multiclase
 * 
 * ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <time.h>

/* ========================================================================
 * DEFINICIONES Y CONSTANTES
 * ======================================================================== */

#define MAX_FEATURES 20        // Máximo número de features
#define MAX_LINE_LENGTH 2048   // Longitud máxima de línea en CSV
#define MAX_CLASSES 10         // Máximo número de clases

/* ========================================================================
 * ESTRUCTURAS DE DATOS
 * ======================================================================== */

/**
 * DataPoint: Representa un punto de datos con sus características y etiqueta
 */
typedef struct {
    double features[MAX_FEATURES];  // Vector de características
    int label;                       // Etiqueta de clase
} DataPoint;

/**
 * Dataset: Contenedor para múltiples puntos de datos
 */
typedef struct {
    DataPoint* data;       // Array de puntos
    int n_samples;         // Número de muestras
    int n_features;        // Número de características
    int n_classes;         // Número de clases
} Dataset;

/**
 * Neighbor: Información de un vecino cercano
 */
typedef struct {
    int index;            // Índice del vecino en el dataset
    double distance;      // Distancia al punto de consulta
    int label;            // Etiqueta del vecino
} Neighbor;

/**
 * KNNModel: Modelo completo de KNN
 */
typedef struct {
    Dataset* training_data;  // Datos de entrenamiento
    int k;                   // Número de vecinos
} KNNModel;

/* ========================================================================
 * FUNCIONES DE UTILIDAD
 * ======================================================================== */

/**
 * Calcular distancia euclidiana entre dos puntos
 * 
 * @param point1 Primer punto
 * @param point2 Segundo punto
 * @param n_features Número de características
 * @return Distancia euclidiana
 */
double euclidean_distance(const double* point1, const double* point2, int n_features) {
    double sum = 0.0;
    
    for (int i = 0; i < n_features; i++) {
        double diff = point1[i] - point2[i];
        sum += diff * diff;
    }
    
    return sqrt(sum);
}

/**
 * Comparar dos vecinos por distancia (para qsort)
 */
int compare_neighbors(const void* a, const void* b) {
    Neighbor* na = (Neighbor*)a;
    Neighbor* nb = (Neighbor*)b;
    
    if (na->distance < nb->distance) return -1;
    if (na->distance > nb->distance) return 1;
    return 0;
}

/**
 * Votar por la clase mayoritaria entre los vecinos
 * 
 * @param neighbors Array de vecinos
 * @param k Número de vecinos
 * @param n_classes Número de clases
 * @return Clase ganadora
 */
int majority_vote(Neighbor* neighbors, int k, int n_classes) {
    // Inicializar contadores de votos
    int* votes = (int*)calloc(n_classes, sizeof(int));
    if (votes == NULL) {
        fprintf(stderr, "Error: No se pudo asignar memoria para votos\n");
        return -1;
    }
    
    // Contar votos
    for (int i = 0; i < k; i++) {
        if (neighbors[i].label >= 0 && neighbors[i].label < n_classes) {
            votes[neighbors[i].label]++;
        }
    }
    
    // Encontrar clase con más votos
    int winning_class = 0;
    int max_votes = votes[0];
    
    for (int i = 1; i < n_classes; i++) {
        if (votes[i] > max_votes) {
            max_votes = votes[i];
            winning_class = i;
        }
    }
    
    free(votes);
    return winning_class;
}

/* ========================================================================
 * FUNCIONES DE CARGA DE DATOS
 * ======================================================================== */

/**
 * Cargar dataset desde archivo CSV
 * 
 * @param filename Nombre del archivo CSV
 * @param n_features Número de características (output)
 * @param n_classes Número de clases (output)
 * @return Puntero al dataset cargado o NULL si hay error
 */
Dataset* load_dataset(const char* filename, int* n_features, int* n_classes) {
    FILE* file = fopen(filename, "r");
    if (file == NULL) {
        fprintf(stderr, "Error: No se pudo abrir el archivo %s\n", filename);
        return NULL;
    }
    
    // Contar líneas para saber cuántas muestras hay
    int n_samples = 0;
    char line[MAX_LINE_LENGTH];
    
    // Leer primera línea (header)
    if (fgets(line, MAX_LINE_LENGTH, file) == NULL) {
        fprintf(stderr, "Error: Archivo vacío\n");
        fclose(file);
        return NULL;
    }
    
    // Contar número de features desde el header
    int feature_count = 0;
    char* token = strtok(line, ",");
    while (token != NULL) {
        feature_count++;
        token = strtok(NULL, ",");
    }
    feature_count--;  // Última columna es la etiqueta
    *n_features = feature_count;
    
    // Contar muestras
    while (fgets(line, MAX_LINE_LENGTH, file) != NULL) {
        if (strlen(line) > 1) {  // Ignorar líneas vacías
            n_samples++;
        }
    }
    
    if (n_samples == 0) {
        fprintf(stderr, "Error: No hay datos en el archivo\n");
        fclose(file);
        return NULL;
    }
    
    // Crear dataset
    Dataset* dataset = (Dataset*)malloc(sizeof(Dataset));
    if (dataset == NULL) {
        fprintf(stderr, "Error: No se pudo asignar memoria para dataset\n");
        fclose(file);
        return NULL;
    }
    
    dataset->data = (DataPoint*)malloc(n_samples * sizeof(DataPoint));
    if (dataset->data == NULL) {
        fprintf(stderr, "Error: No se pudo asignar memoria para datos\n");
        free(dataset);
        fclose(file);
        return NULL;
    }
    
    dataset->n_samples = n_samples;
    dataset->n_features = *n_features;
    
    // Volver al inicio del archivo (después del header)
    rewind(file);
    fgets(line, MAX_LINE_LENGTH, file);  // Skip header
    
    // Leer datos
    int max_label = 0;
    for (int i = 0; i < n_samples; i++) {
        if (fgets(line, MAX_LINE_LENGTH, file) == NULL) {
            break;
        }
        
        // Parsear features
        char* token = strtok(line, ",");
        for (int j = 0; j < *n_features && token != NULL; j++) {
            dataset->data[i].features[j] = atof(token);
            token = strtok(NULL, ",");
        }
        
        // Parsear label (última columna)
        if (token != NULL) {
            dataset->data[i].label = atoi(token);
            if (dataset->data[i].label > max_label) {
                max_label = dataset->data[i].label;
            }
        }
    }
    
    dataset->n_classes = max_label + 1;
    *n_classes = dataset->n_classes;
    
    fclose(file);
    return dataset;
}

/**
 * Liberar memoria del dataset
 */
void free_dataset(Dataset* dataset) {
    if (dataset != NULL) {
        if (dataset->data != NULL) {
            free(dataset->data);
        }
        free(dataset);
    }
}

/**
 * Imprimir información del dataset
 */
void print_dataset_info(Dataset* dataset) {
    if (dataset == NULL) {
        printf("Dataset es NULL\n");
        return;
    }
    
    printf("\n╔════════════════════════════════════════╗\n");
    printf("║      INFORMACIÓN DEL DATASET           ║\n");
    printf("╚════════════════════════════════════════╝\n");
    printf("  Muestras:        %d\n", dataset->n_samples);
    printf("  Features:        %d\n", dataset->n_features);
    printf("  Clases:          %d\n", dataset->n_classes);
    printf("\n");
}

/* ========================================================================
 * FUNCIONES DEL MODELO KNN
 * ======================================================================== */

/**
 * Crear modelo KNN
 * 
 * @param k Número de vecinos
 * @return Puntero al modelo creado
 */
KNNModel* create_knn_model(int k) {
    KNNModel* model = (KNNModel*)malloc(sizeof(KNNModel));
    if (model == NULL) {
        fprintf(stderr, "Error: No se pudo asignar memoria para modelo\n");
        return NULL;
    }
    
    model->k = k;
    model->training_data = NULL;
    
    return model;
}

/**
 * Entrenar modelo KNN (almacenar datos de entrenamiento)
 * 
 * @param model Modelo KNN
 * @param training_data Datos de entrenamiento
 */
void knn_fit(KNNModel* model, Dataset* training_data) {
    model->training_data = training_data;
}

/**
 * Predecir clase de un único punto
 * 
 * @param model Modelo KNN entrenado
 * @param test_point Punto a clasificar
 * @return Clase predicha
 */
int knn_predict_single(KNNModel* model, const double* test_point) {
    if (model->training_data == NULL) {
        fprintf(stderr, "Error: Modelo no entrenado\n");
        return -1;
    }
    
    Dataset* train = model->training_data;
    int k = model->k;
    
    // Crear array de vecinos
    Neighbor* all_neighbors = (Neighbor*)malloc(train->n_samples * sizeof(Neighbor));
    if (all_neighbors == NULL) {
        fprintf(stderr, "Error: No se pudo asignar memoria para vecinos\n");
        return -1;
    }
    
    // Calcular distancias a todos los puntos de entrenamiento
    for (int i = 0; i < train->n_samples; i++) {
        all_neighbors[i].index = i;
        all_neighbors[i].distance = euclidean_distance(
            test_point, 
            train->data[i].features, 
            train->n_features
        );
        all_neighbors[i].label = train->data[i].label;
    }
    
    // Ordenar por distancia
    qsort(all_neighbors, train->n_samples, sizeof(Neighbor), compare_neighbors);
    
    // Tomar los k más cercanos
    Neighbor* k_neighbors = (Neighbor*)malloc(k * sizeof(Neighbor));
    if (k_neighbors == NULL) {
        fprintf(stderr, "Error: No se pudo asignar memoria para k vecinos\n");
        free(all_neighbors);
        return -1;
    }
    
    for (int i = 0; i < k; i++) {
        k_neighbors[i] = all_neighbors[i];
    }
    
    // Votar por la clase mayoritaria
    int predicted_class = majority_vote(k_neighbors, k, train->n_classes);
    
    free(all_neighbors);
    free(k_neighbors);
    
    return predicted_class;
}

/**
 * Predecir clases de múltiples puntos
 * 
 * @param model Modelo KNN entrenado
 * @param test_data Dataset de prueba
 * @param predictions Array para almacenar predicciones (output)
 */
void knn_predict(KNNModel* model, Dataset* test_data, int* predictions) {
    printf("\nRealizando predicciones...\n");
    printf("[");
    
    int progress_step = test_data->n_samples / 50;
    if (progress_step == 0) progress_step = 1;
    
    for (int i = 0; i < test_data->n_samples; i++) {
        predictions[i] = knn_predict_single(model, test_data->data[i].features);
        
        // Mostrar progreso
        if (i % progress_step == 0) {
            printf("=");
            fflush(stdout);
        }
    }
    
    printf("] 100%%\n");
}

/**
 * Liberar memoria del modelo
 */
void free_knn_model(KNNModel* model) {
    if (model != NULL) {
        // No liberamos training_data aquí porque se libera externamente
        free(model);
    }
}

/* ========================================================================
 * FUNCIONES DE EVALUACIÓN
 * ======================================================================== */

/**
 * Calcular accuracy
 * 
 * @param y_true Etiquetas verdaderas
 * @param y_pred Etiquetas predichas
 * @param n_samples Número de muestras
 * @return Accuracy (0.0 a 1.0)
 */
double calculate_accuracy(const int* y_true, const int* y_pred, int n_samples) {
    int correct = 0;
    
    for (int i = 0; i < n_samples; i++) {
        if (y_true[i] == y_pred[i]) {
            correct++;
        }
    }
    
    return (double)correct / n_samples;
}

/**
 * Calcular y mostrar matriz de confusión
 * 
 * @param y_true Etiquetas verdaderas
 * @param y_pred Etiquetas predichas
 * @param n_samples Número de muestras
 * @param n_classes Número de clases
 */
void print_confusion_matrix(const int* y_true, const int* y_pred, 
                           int n_samples, int n_classes) {
    // Crear matriz de confusión
    int** matrix = (int**)malloc(n_classes * sizeof(int*));
    for (int i = 0; i < n_classes; i++) {
        matrix[i] = (int*)calloc(n_classes, sizeof(int));
    }
    
    // Llenar matriz
    for (int i = 0; i < n_samples; i++) {
        if (y_true[i] >= 0 && y_true[i] < n_classes &&
            y_pred[i] >= 0 && y_pred[i] < n_classes) {
            matrix[y_true[i]][y_pred[i]]++;
        }
    }
    
    // Imprimir matriz
    printf("\n╔════════════════════════════════════════╗\n");
    printf("║      MATRIZ DE CONFUSIÓN               ║\n");
    printf("╚════════════════════════════════════════╝\n\n");
    printf("         ");
    for (int i = 0; i < n_classes; i++) {
        printf("C%-2d  ", i);
    }
    printf("\n");
    printf("      ");
    for (int i = 0; i < n_classes; i++) {
        printf("-----");
    }
    printf("\n");
    
    for (int i = 0; i < n_classes; i++) {
        printf("C%-2d |  ", i);
        for (int j = 0; j < n_classes; j++) {
            printf("%4d ", matrix[i][j]);
        }
        printf("\n");
    }
    printf("\n");
    
    // Liberar matriz
    for (int i = 0; i < n_classes; i++) {
        free(matrix[i]);
    }
    free(matrix);
}

/**
 * Calcular métricas por clase
 * 
 * @param y_true Etiquetas verdaderas
 * @param y_pred Etiquetas predichas
 * @param n_samples Número de muestras
 * @param n_classes Número de clases
 */
void print_per_class_metrics(const int* y_true, const int* y_pred,
                             int n_samples, int n_classes) {
    printf("\n╔════════════════════════════════════════╗\n");
    printf("║      MÉTRICAS POR CLASE                ║\n");
    printf("╚════════════════════════════════════════╝\n\n");
    printf("Clase  Precisión  Recall    F1-Score\n");
    printf("─────────────────────────────────────────\n");
    
    for (int c = 0; c < n_classes; c++) {
        int tp = 0, fp = 0, fn = 0;
        
        for (int i = 0; i < n_samples; i++) {
            if (y_true[i] == c && y_pred[i] == c) tp++;
            if (y_true[i] != c && y_pred[i] == c) fp++;
            if (y_true[i] == c && y_pred[i] != c) fn++;
        }
        
        double precision = (tp + fp > 0) ? (double)tp / (tp + fp) : 0.0;
        double recall = (tp + fn > 0) ? (double)tp / (tp + fn) : 0.0;
        double f1 = (precision + recall > 0) ? 
                    2 * precision * recall / (precision + recall) : 0.0;
        
        printf("  %d     %.4f    %.4f    %.4f\n", c, precision, recall, f1);
    }
    printf("\n");
}

/* ========================================================================
 * FUNCIÓN PRINCIPAL
 * ======================================================================== */

int main(int argc, char* argv[]) {
    printf("\n");
    printf("╔═══════════════════════════════════════════════════════════════════╗\n");
    printf("║    K-NEAREST NEIGHBORS (KNN) CLASSIFIER - IMPLEMENTACIÓN EN C     ║\n");
    printf("║                                                                    ║\n");
    printf("║    Universidad del Norte - Inteligencia Artificial (ELP 8012)     ║\n");
    printf("║    Proyecto: Predicción de Desempeño en Inglés - Saber 11         ║\n");
    printf("╚═══════════════════════════════════════════════════════════════════╝\n");
    printf("\n");
    
    // Verificar argumentos
    if (argc < 4) {
        printf("Uso: %s <train.csv> <test.csv> <k>\n", argv[0]);
        printf("Ejemplo: %s train_data_c.csv test_data_c.csv 5\n", argv[0]);
        return 1;
    }
    
    const char* train_file = argv[1];
    const char* test_file = argv[2];
    int k = atoi(argv[3]);
    
    if (k <= 0) {
        fprintf(stderr, "Error: k debe ser un número positivo\n");
        return 1;
    }
    
    printf("Parámetros:\n");
    printf("  Archivo de entrenamiento: %s\n", train_file);
    printf("  Archivo de prueba: %s\n", test_file);
    printf("  K (vecinos): %d\n", k);
    printf("\n");
    
    // Medir tiempo de inicio
    clock_t start_time = clock();
    
    // Cargar datos de entrenamiento
    printf("📂 Cargando datos de entrenamiento...\n");
    int n_features, n_classes;
    Dataset* train_data = load_dataset(train_file, &n_features, &n_classes);
    
    if (train_data == NULL) {
        fprintf(stderr, "Error al cargar datos de entrenamiento\n");
        return 1;
    }
    
    printf("✅ Datos de entrenamiento cargados:\n");
    print_dataset_info(train_data);
    
    // Cargar datos de prueba
    printf("📂 Cargando datos de prueba...\n");
    int test_n_features, test_n_classes;
    Dataset* test_data = load_dataset(test_file, &test_n_features, &test_n_classes);
    
    if (test_data == NULL) {
        fprintf(stderr, "Error al cargar datos de prueba\n");
        free_dataset(train_data);
        return 1;
    }
    
    printf("✅ Datos de prueba cargados:\n");
    print_dataset_info(test_data);
    
    // Verificar compatibilidad
    if (n_features != test_n_features) {
        fprintf(stderr, "Error: Número de features no coincide\n");
        free_dataset(train_data);
        free_dataset(test_data);
        return 1;
    }
    
    // Crear y entrenar modelo
    printf("🔧 Creando modelo KNN con k=%d...\n", k);
    KNNModel* model = create_knn_model(k);
    
    if (model == NULL) {
        free_dataset(train_data);
        free_dataset(test_data);
        return 1;
    }
    
    printf("🎯 Entrenando modelo...\n");
    knn_fit(model, train_data);
    printf("✅ Modelo entrenado\n");
    
    // Realizar predicciones
    clock_t pred_start = clock();
    int* predictions = (int*)malloc(test_data->n_samples * sizeof(int));
    
    if (predictions == NULL) {
        fprintf(stderr, "Error al asignar memoria para predicciones\n");
        free_knn_model(model);
        free_dataset(train_data);
        free_dataset(test_data);
        return 1;
    }
    
    knn_predict(model, test_data, predictions);
    clock_t pred_end = clock();
    
    double pred_time = (double)(pred_end - pred_start) / CLOCKS_PER_SEC;
    printf("✅ Predicciones completadas en %.2f segundos\n", pred_time);
    
    // Evaluar resultados
    printf("\n📊 EVALUANDO RESULTADOS\n");
    printf("════════════════════════════════════════\n");
    
    // Extraer etiquetas verdaderas
    int* y_true = (int*)malloc(test_data->n_samples * sizeof(int));
    for (int i = 0; i < test_data->n_samples; i++) {
        y_true[i] = test_data->data[i].label;
    }
    
    // Calcular accuracy
    double accuracy = calculate_accuracy(y_true, predictions, test_data->n_samples);
    
    printf("\n╔════════════════════════════════════════╗\n");
    printf("║      RESULTADOS GENERALES              ║\n");
    printf("╚════════════════════════════════════════╝\n");
    printf("  Accuracy:              %.2f%%\n", accuracy * 100);
    printf("  Total de muestras:     %d\n", test_data->n_samples);
    printf("  Predicciones correctas: %d\n", (int)(accuracy * test_data->n_samples));
    printf("  Predicciones incorrectas: %d\n", 
           test_data->n_samples - (int)(accuracy * test_data->n_samples));
    printf("\n");
    
    // Mostrar matriz de confusión
    print_confusion_matrix(y_true, predictions, test_data->n_samples, n_classes);
    
    // Mostrar métricas por clase
    print_per_class_metrics(y_true, predictions, test_data->n_samples, n_classes);
    
    // Tiempo total
    clock_t end_time = clock();
    double total_time = (double)(end_time - start_time) / CLOCKS_PER_SEC;
    
    printf("╔════════════════════════════════════════╗\n");
    printf("║      TIEMPO DE EJECUCIÓN               ║\n");
    printf("╚════════════════════════════════════════╝\n");
    printf("  Tiempo total:      %.2f segundos\n", total_time);
    printf("  Tiempo predicción: %.2f segundos\n", pred_time);
    printf("  Tiempo por muestra: %.4f segundos\n", pred_time / test_data->n_samples);
    printf("\n");
    
    // Guardar resultados en directorio results/
    FILE* results_file = fopen("results/resultados_knn_c.txt", "w");
    if (results_file != NULL) {
        fprintf(results_file, "RESULTADOS KNN EN C\n");
        fprintf(results_file, "==================\n\n");
        fprintf(results_file, "K: %d\n", k);
        fprintf(results_file, "Muestras de entrenamiento: %d\n", train_data->n_samples);
        fprintf(results_file, "Muestras de prueba: %d\n", test_data->n_samples);
        fprintf(results_file, "Features: %d\n", n_features);
        fprintf(results_file, "Clases: %d\n\n", n_classes);
        fprintf(results_file, "Accuracy: %.4f\n", accuracy);
        fprintf(results_file, "Tiempo de predicción: %.2f segundos\n", pred_time);
        fprintf(results_file, "Tiempo total: %.2f segundos\n", total_time);
        fclose(results_file);
        printf("✅ Resultados guardados en: results/resultados_knn_c.txt\n");
    } else {
        fprintf(stderr, "⚠️  No se pudo crear archivo de resultados\n");
    }
    
    // Liberar memoria
    free(predictions);
    free(y_true);
    free_knn_model(model);
    free_dataset(train_data);
    free_dataset(test_data);
    
    printf("\n✅ Programa finalizado exitosamente\n\n");
    
    return 0;
}
