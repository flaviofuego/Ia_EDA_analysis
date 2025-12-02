#include <stdio.h>
#include <stdlib.h>
#include "../include/metrics.h"
#include "../include/prediction.h"

Metrics* compute_metrics(MLP* mlp, Dataset* data) {
    Metrics* metrics = (Metrics*)malloc(sizeof(Metrics));
    metrics->num_classes = data->num_classes;
    
    int* predictions = (int*)malloc(data->num_samples * sizeof(int));
    predict_batch(mlp, data, predictions);
    
    metrics->confusion_matrix = (int**)malloc(data->num_classes * sizeof(int*));
    for (int i = 0; i < data->num_classes; i++) {
        metrics->confusion_matrix[i] = (int*)calloc(data->num_classes, sizeof(int));
    }
    
    compute_confusion_matrix(predictions, data, metrics->confusion_matrix);
    
    metrics->per_class_acc = (double*)malloc(data->num_classes * sizeof(double));
    metrics->per_class_f1 = (double*)malloc(data->num_classes * sizeof(double));
    
    double* precision = (double*)malloc(data->num_classes * sizeof(double));
    double* recall = (double*)malloc(data->num_classes * sizeof(double));
    
    for (int c = 0; c < data->num_classes; c++) {
        int tp = metrics->confusion_matrix[c][c];
        int fn = 0, fp = 0;
        
        for (int i = 0; i < data->num_classes; i++) {
            if (i != c) {
                fn += metrics->confusion_matrix[c][i];
                fp += metrics->confusion_matrix[i][c];
            }
        }
        
        int total_class = tp + fn;
        metrics->per_class_acc[c] = total_class > 0 ? (double)tp / total_class : 0.0;
        
        precision[c] = (tp + fp) > 0 ? (double)tp / (tp + fp) : 0.0;
        recall[c] = (tp + fn) > 0 ? (double)tp / (tp + fn) : 0.0;
        
        if (precision[c] + recall[c] > 0) {
            metrics->per_class_f1[c] = 2.0 * precision[c] * recall[c] / (precision[c] + recall[c]);
        } else {
            metrics->per_class_f1[c] = 0.0;
        }
    }
    
    metrics->accuracy = compute_accuracy(predictions, data);
    metrics->balanced_acc = compute_balanced_accuracy(metrics);
    metrics->f1_weighted = compute_f1_weighted(metrics, data);
    
    double sum_prec = 0.0, sum_rec = 0.0;
    for (int c = 0; c < data->num_classes; c++) {
        sum_prec += precision[c];
        sum_rec += recall[c];
    }
    metrics->precision = sum_prec / data->num_classes;
    metrics->recall = sum_rec / data->num_classes;
    
    free(precision);
    free(recall);
    free(predictions);
    
    return metrics;
}

void compute_confusion_matrix(int* predictions, Dataset* data, int** conf_matrix) {
    for (int i = 0; i < data->num_samples; i++) {
        int true_label = data->data[i].label;
        int pred_label = predictions[i];
        conf_matrix[true_label][pred_label]++;
    }
}

double compute_accuracy(int* predictions, Dataset* data) {
    int correct = 0;
    for (int i = 0; i < data->num_samples; i++) {
        if (predictions[i] == data->data[i].label) {
            correct++;
        }
    }
    return (double)correct / data->num_samples;
}

double compute_balanced_accuracy(Metrics* metrics) {
    double sum = 0.0;
    for (int c = 0; c < metrics->num_classes; c++) {
        sum += metrics->per_class_acc[c];
    }
    return sum / metrics->num_classes;
}

double compute_f1_weighted(Metrics* metrics, Dataset* data) {
    int* class_counts = (int*)calloc(data->num_classes, sizeof(int));
    for (int i = 0; i < data->num_samples; i++) {
        class_counts[data->data[i].label]++;
    }
    
    double weighted_sum = 0.0;
    for (int c = 0; c < metrics->num_classes; c++) {
        double weight = (double)class_counts[c] / data->num_samples;
        weighted_sum += metrics->per_class_f1[c] * weight;
    }
    
    free(class_counts);
    return weighted_sum;
}

void print_metrics(Metrics* metrics, const char* dataset_name) {
    printf("\n========== MÉTRICAS DE EVALUACIÓN: %s ==========\n", dataset_name);
    printf("Accuracy Global:      %.4f\n", metrics->accuracy);
    printf("Balanced Accuracy:    %.4f\n", metrics->balanced_acc);
    printf("F1-Score (Weighted):  %.4f\n", metrics->f1_weighted);
    printf("Precision (Macro):    %.4f\n", metrics->precision);
    printf("Recall (Macro):       %.4f\n", metrics->recall);
    
    printf("\nMÉTRICAS POR CLASE:\n");
    printf("Clase | Accuracy | F1-Score\n");
    printf("------|----------|----------\n");
    for (int c = 0; c < metrics->num_classes; c++) {
        printf("  %d   |  %.4f   |  %.4f\n", c, metrics->per_class_acc[c], metrics->per_class_f1[c]);
    }
    
    printf("\nMATRIZ DE CONFUSIÓN:\n");
    printf("       ");
    for (int c = 0; c < metrics->num_classes; c++) {
        printf("Pred%d  ", c);
    }
    printf("\n");
    
    for (int i = 0; i < metrics->num_classes; i++) {
        printf("True%d  ", i);
        for (int j = 0; j < metrics->num_classes; j++) {
            printf("%6d ", metrics->confusion_matrix[i][j]);
        }
        printf("\n");
    }
    printf("=============================================\n\n");
}

void free_metrics(Metrics* metrics) {
    if (metrics) {
        if (metrics->confusion_matrix) {
            for (int i = 0; i < metrics->num_classes; i++) {
                free(metrics->confusion_matrix[i]);
            }
            free(metrics->confusion_matrix);
        }
        free(metrics->per_class_acc);
        free(metrics->per_class_f1);
        free(metrics);
    }
}
