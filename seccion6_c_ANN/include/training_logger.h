#ifndef TRAINING_LOGGER_H
#define TRAINING_LOGGER_H

#include <stdio.h>

typedef struct {
    FILE* file;
    char* filename;
    int is_open;
} TrainingLogger;

/**
 * Crea y abre un logger para guardar datos de entrenamiento
 */
TrainingLogger* create_training_logger(const char* filename);

/**
 * Escribe el header del CSV
 */
void write_logger_header(TrainingLogger* logger);

/**
 * Registra datos de una época
 */
void log_epoch(TrainingLogger* logger, int epoch, int total_epochs,
               double train_loss, double val_loss, double val_acc, 
               double learning_rate, double elapsed_time);

/**
 * Registra métricas finales de test
 */
void log_final_metrics(TrainingLogger* logger, double accuracy, 
                       double balanced_acc, double f1_score,
                       double precision, double recall, double total_time);

/**
 * Cierra el logger
 */
void close_training_logger(TrainingLogger* logger);

#endif // TRAINING_LOGGER_H
