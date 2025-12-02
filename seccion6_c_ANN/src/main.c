#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <sys/stat.h>
#include <sys/types.h>
#include "../include/types.h"
#include "../include/config.h"
#include "../include/data_utils.h"
#include "../include/mlp_core.h"
#include "../include/training.h"
#include "../include/training_logger.h"
#include "../include/metrics.h"

int main(int argc, char** argv) {
    if (argc < 2) {
        printf("Uso: %s <archivo_dataset.csv> [opciones]\n", argv[0]);
        printf("Opciones:\n");
        printf("  --config <archivo>  Archivo de configuración (default: mlp_config.txt)\n");
        printf("  --epochs <n>        Número de épocas (override config)\n");
        printf("  --batch <n>         Tamaño de batch (override config)\n");
        printf("  --lr <f>            Learning rate (override config)\n");
        printf("  --hidden <n,n,...>  Neuronas por capa oculta (override config)\n");
        return 1;
    }
    
    const char* filename = argv[1];
    const char* config_file = "mlp_config.txt";
    
    // Buscar archivo de configuración en argumentos
    for (int i = 2; i < argc; i++) {
        if (strcmp(argv[i], "--config") == 0 && i + 1 < argc) {
            config_file = argv[++i];
            break;
        }
    }
    
    // Cargar configuración desde archivo
    MLPConfig* mlp_config = load_config(config_file);
    
    // Permitir overrides desde línea de comandos
    for (int i = 2; i < argc; i++) {
        if (strcmp(argv[i], "--epochs") == 0 && i + 1 < argc) {
            mlp_config->epochs = atoi(argv[++i]);
        } else if (strcmp(argv[i], "--batch") == 0 && i + 1 < argc) {
            mlp_config->batch_size = atoi(argv[++i]);
        } else if (strcmp(argv[i], "--lr") == 0 && i + 1 < argc) {
            mlp_config->learning_rate = atof(argv[++i]);
        } else if (strcmp(argv[i], "--config") == 0 && i + 1 < argc) {
            i++; // Ya procesado
        }
    }
    
    printf("\n============================================\n");
    printf("   PERCEPTRÓN MULTICAPA - CLASIFICACIÓN\n");
    printf("   Dataset: Pruebas Saber 11 - DESEMP_INGLES\n");
    printf("============================================\n\n");
    
    // Mostrar configuración
    print_config(mlp_config);
    
    clock_t start_time = clock();
    
    int num_features = 10;
    int num_classes = 5;
    
    printf("Cargando dataset desde %s...\n", filename);
    Dataset* dataset = load_dataset(filename, num_features, num_classes);
    if (!dataset) {
        fprintf(stderr, "Error al cargar dataset\n");
        return 1;
    }
    printf("Dataset cargado: %d muestras, %d features, %d clases\n", 
           dataset->num_samples, dataset->num_features, dataset->num_classes);
    
    printf("\nNormalizando datos (z-score)...\n");
    normalize_dataset(dataset);
    
    printf("Dividiendo dataset (80%% train, 20%% test)...\n");
    Dataset *train_data, *test_data;
    split_dataset(dataset, &train_data, &test_data, 0.2, 42);
    printf("Train: %d muestras | Test: %d muestras\n", 
           train_data->num_samples, test_data->num_samples);
    
    Dataset *train_subset, *val_data;
    split_dataset(train_data, &train_subset, &val_data, 0.15, mlp_config->seed);
    printf("Train: %d muestras | Validation: %d muestras\n", 
           train_subset->num_samples, val_data->num_samples);
    
    int total_layers = mlp_config->num_hidden_layers + 1;
    int* layer_sizes = (int*)malloc(total_layers * sizeof(int));
    for (int i = 0; i < mlp_config->num_hidden_layers; i++) {
        layer_sizes[i] = mlp_config->hidden_layers[i];
    }
    layer_sizes[mlp_config->num_hidden_layers] = num_classes;
    
    const char** activations = (const char**)malloc(total_layers * sizeof(char*));
    for (int i = 0; i < mlp_config->num_hidden_layers; i++) {
        activations[i] = "relu";
    }
    activations[mlp_config->num_hidden_layers] = "softmax";
    
    printf("\nCreando MLP: %d", num_features);
    for (int i = 0; i < total_layers; i++) {
        printf(" -> %d(%s)", layer_sizes[i], activations[i]);
    }
    printf("\n");
    
    MLP* mlp = create_mlp(num_features, layer_sizes, total_layers, activations, mlp_config->learning_rate);
    
    TrainConfig config;
    config.epochs = mlp_config->epochs;
    config.batch_size = mlp_config->batch_size;
    config.learning_rate = mlp_config->learning_rate;
    config.lr_decay = mlp_config->lr_decay;
    config.momentum = mlp_config->momentum;
    config.weight_decay = mlp_config->weight_decay;
    config.early_stopping = mlp_config->early_stopping_patience;
    config.min_delta = mlp_config->min_delta;
    config.verbose = mlp_config->verbose;
    config.seed = mlp_config->seed;
    
    train_mlp(mlp, train_subset, val_data, &config);
    
    printf("\nEvaluando modelo en conjunto de test...\n");
    Metrics* test_metrics = compute_metrics(mlp, test_data);
    print_metrics(test_metrics, "TEST");
    
    clock_t end_time = clock();
    double elapsed = (double)(end_time - start_time) / CLOCKS_PER_SEC;
    
    printf("TIEMPO TOTAL DE EJECUCIÓN: %.2f segundos\n", elapsed);
    
    // Guardar métricas finales en el CSV de training history
    FILE* metrics_file = fopen("tasks/training_history.csv", "a");
    if (metrics_file) {
        fprintf(metrics_file, "\n# Métricas Finales\n");
        fprintf(metrics_file, "# accuracy,balanced_accuracy,f1_score,precision,recall,total_time\n");
        fprintf(metrics_file, "%.6f,%.6f,%.6f,%.6f,%.6f,%.2f\n",
                test_metrics->accuracy, test_metrics->balanced_acc, 
                test_metrics->f1_weighted, test_metrics->precision, 
                test_metrics->recall, elapsed);
        fclose(metrics_file);
    }
    
    printf("\nGUARDANDO RESULTADOS...\n");
    
    // Crear directorio tasks/ si no existe
    #ifdef _WIN32
        mkdir("tasks");
    #else
        mkdir("tasks", 0755);
    #endif
    
    FILE* report = fopen("tasks/tarea23_resultados_entrenamiento.txt", "w");
    if (report) {
        fprintf(report, "================================================================================\n");
        fprintf(report, "TAREA 23: RESULTADOS DE ENTRENAMIENTO Y PREDICCIÓN\n");
        fprintf(report, "================================================================================\n\n");
        fprintf(report, "CONFIGURACIÓN DEL MODELO:\n");
        fprintf(report, "Archivo de configuración: %s\n", config_file);
        fprintf(report, "Arquitectura: %d", num_features);
        for (int i = 0; i < total_layers; i++) {
            fprintf(report, " -> %d(%s)", layer_sizes[i], activations[i]);
        }
        fprintf(report, "\n");
        fprintf(report, "Learning rate inicial: %.4f (decay: %.2f)\n", mlp_config->learning_rate, config.lr_decay);
        fprintf(report, "Batch size: %d\n", config.batch_size);
        fprintf(report, "Momentum: %.2f\n", config.momentum);
        fprintf(report, "Weight decay (L2): %.5f\n", config.weight_decay);
        fprintf(report, "Epochs máximo: %d\n", config.epochs);
        fprintf(report, "Early stopping patience: %d\n", config.early_stopping);
        fprintf(report, "Seed: %d\n\n", config.seed);
        
        fprintf(report, "DATASET:\n");
        fprintf(report, "Total: %d muestras\n", dataset->num_samples);
        fprintf(report, "Train: %d (%.1f%%)\n", train_subset->num_samples, 
                100.0 * train_subset->num_samples / dataset->num_samples);
        fprintf(report, "Validation: %d (%.1f%%)\n", val_data->num_samples,
                100.0 * val_data->num_samples / dataset->num_samples);
        fprintf(report, "Test: %d (%.1f%%)\n\n", test_data->num_samples,
                100.0 * test_data->num_samples / dataset->num_samples);
        
        fprintf(report, "MÉTRICAS FINALES (TEST SET):\n");
        fprintf(report, "Accuracy:           %.4f\n", test_metrics->accuracy);
        fprintf(report, "Balanced Accuracy:  %.4f\n", test_metrics->balanced_acc);
        fprintf(report, "F1-Score Weighted:  %.4f\n", test_metrics->f1_weighted);
        fprintf(report, "Precision (Macro):  %.4f\n", test_metrics->precision);
        fprintf(report, "Recall (Macro):     %.4f\n\n", test_metrics->recall);
        
        fprintf(report, "TIEMPO DE EJECUCIÓN: %.2f segundos\n\n", elapsed);
        
        fprintf(report, "FRAGMENTOS DE CÓDIGO CLAVE:\n\n");
        fprintf(report, "1. INICIALIZACIÓN DE PESOS (He para ReLU):\n");
        fprintf(report, "   scale = sqrt(2.0 / layer->num_inputs);\n");
        fprintf(report, "   for (i = 0; i < num_neurons; i++)\n");
        fprintf(report, "       for (j = 0; j < num_inputs; j++)\n");
        fprintf(report, "           weights[i][j] = random(-1,1) * scale;\n\n");
        
        fprintf(report, "2. FORWARD PASS CON RELU:\n");
        fprintf(report, "   for (i = 0; i < num_neurons; i++) {\n");
        fprintf(report, "       z[i] = bias[i];\n");
        fprintf(report, "       for (j = 0; j < num_inputs; j++)\n");
        fprintf(report, "           z[i] += weights[i][j] * input[j];\n");
        fprintf(report, "       output[i] = z[i] > 0 ? z[i] : 0;  // ReLU\n");
        fprintf(report, "   }\n\n");
        
        fprintf(report, "3. SOFTMAX PARA OUTPUT LAYER:\n");
        fprintf(report, "   max_val = max(z);\n");
        fprintf(report, "   sum = 0;\n");
        fprintf(report, "   for (i = 0; i < num_classes; i++) {\n");
        fprintf(report, "       output[i] = exp(z[i] - max_val);\n");
        fprintf(report, "       sum += output[i];\n");
        fprintf(report, "   }\n");
        fprintf(report, "   for (i = 0; i < num_classes; i++)\n");
        fprintf(report, "       output[i] /= sum;\n\n");
        
        fprintf(report, "4. BACKPROPAGATION - DELTA OUTPUT:\n");
        fprintf(report, "   for (i = 0; i < num_classes; i++)\n");
        fprintf(report, "       delta[i] = (i == true_label) ? output[i] - 1.0 : output[i];\n\n");
        
        fprintf(report, "5. BACKPROPAGATION - CAPAS OCULTAS:\n");
        fprintf(report, "   for (i = 0; i < num_neurons; i++) {\n");
        fprintf(report, "       sum = 0;\n");
        fprintf(report, "       for (j = 0; j < next_layer_size; j++)\n");
        fprintf(report, "           sum += next_weights[j][i] * next_delta[j];\n");
        fprintf(report, "       derivative = (output[i] > 0) ? 1.0 : 0.0;  // ReLU'\n");
        fprintf(report, "       delta[i] = sum * derivative;\n");
        fprintf(report, "   }\n\n");
        
        fprintf(report, "6. ACTUALIZACIÓN DE PESOS CON MOMENTUM:\n");
        fprintf(report, "   for (i = 0; i < num_neurons; i++)\n");
        fprintf(report, "       for (j = 0; j < num_inputs; j++) {\n");
        fprintf(report, "           grad = weight_grad[i][j] / batch_size;\n");
        fprintf(report, "           reg = weight_decay * weights[i][j];\n");
        fprintf(report, "           velocity[i][j] = momentum * velocity[i][j] + lr * (grad + reg);\n");
        fprintf(report, "           weights[i][j] -= velocity[i][j];\n");
        fprintf(report, "       }\n\n");
        
        fprintf(report, "================================================================================\n");
        fclose(report);
        printf("Resultados guardados en tasks/tarea23_resultados_entrenamiento.txt\n");
    } else {
        fprintf(stderr, "Advertencia: No se pudo guardar el archivo de resultados en tasks/\n");
    }
    
    free_metrics(test_metrics);
    free_mlp(mlp);
    free(layer_sizes);
    free(activations);
    free_config(mlp_config);
    free(train_subset->data);
    free(train_subset);
    free(val_data->data);
    free(val_data);
    free(train_data->data);
    free(train_data);
    free(test_data->data);
    free(test_data);
    free_dataset(dataset);
    
    printf("\nPROGRAMA FINALIZADO EXITOSAMENTE\n");
    printf("============================================\n\n");
    
    return 0;
}
