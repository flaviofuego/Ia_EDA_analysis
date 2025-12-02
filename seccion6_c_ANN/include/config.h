#ifndef CONFIG_H
#define CONFIG_H

#include "types.h"

typedef struct {
    int epochs;
    int batch_size;
    double learning_rate;
    double lr_decay;
    double momentum;
    double weight_decay;
    int early_stopping_patience;
    double min_delta;
    int* hidden_layers;
    int num_hidden_layers;
    int seed;
    int verbose;
} MLPConfig;

/**
 * Carga configuración desde archivo
 */
MLPConfig* load_config(const char* config_file);

/**
 * Libera memoria de configuración
 */
void free_config(MLPConfig* config);

/**
 * Imprime configuración
 */
void print_config(const MLPConfig* config);

/**
 * Crea configuración por defecto
 */
MLPConfig* create_default_config(void);

#endif // CONFIG_H
