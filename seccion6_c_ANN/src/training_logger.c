#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include "../include/training_logger.h"

TrainingLogger* create_training_logger(const char* filename) {
    TrainingLogger* logger = (TrainingLogger*)malloc(sizeof(TrainingLogger));
    
    // Crear directorio tasks/ si no existe
    #ifdef _WIN32
        mkdir("tasks");
    #else
        mkdir("tasks", 0755);
    #endif
    
    // Construir ruta completa
    char filepath[512];
    snprintf(filepath, sizeof(filepath), "tasks/%s", filename);
    
    logger->filename = strdup(filepath);
    logger->file = fopen(filepath, "w");
    logger->is_open = (logger->file != NULL);
    
    if (!logger->is_open) {
        fprintf(stderr, "Advertencia: No se pudo crear archivo de log: %s\n", filepath);
    } else {
        printf("📊 Guardando datos de entrenamiento en: %s\n", filepath);
    }
    
    return logger;
}

void write_logger_header(TrainingLogger* logger) {
    if (!logger || !logger->is_open) return;
    
    fprintf(logger->file, "epoch,total_epochs,train_loss,val_loss,val_accuracy,learning_rate,elapsed_time\n");
    fflush(logger->file);
}

void log_epoch(TrainingLogger* logger, int epoch, int total_epochs,
               double train_loss, double val_loss, double val_acc, 
               double learning_rate, double elapsed_time) {
    if (!logger || !logger->is_open) return;
    
    fprintf(logger->file, "%d,%d,%.6f,%.6f,%.6f,%.6f,%.2f\n",
            epoch, total_epochs, train_loss, val_loss, val_acc, learning_rate, elapsed_time);
    fflush(logger->file);
}

void log_final_metrics(TrainingLogger* logger, double accuracy, 
                       double balanced_acc, double f1_score,
                       double precision, double recall, double total_time) {
    if (!logger || !logger->is_open) return;
    
    // Agregar línea separadora
    fprintf(logger->file, "\n# Métricas Finales\n");
    fprintf(logger->file, "# accuracy,balanced_accuracy,f1_score,precision,recall,total_time\n");
    fprintf(logger->file, "%.6f,%.6f,%.6f,%.6f,%.6f,%.2f\n",
            accuracy, balanced_acc, f1_score, precision, recall, total_time);
    fflush(logger->file);
}

void close_training_logger(TrainingLogger* logger) {
    if (!logger) return;
    
    if (logger->is_open && logger->file) {
        fclose(logger->file);
        logger->is_open = 0;
    }
    
    if (logger->filename) {
        free(logger->filename);
    }
    
    free(logger);
}
