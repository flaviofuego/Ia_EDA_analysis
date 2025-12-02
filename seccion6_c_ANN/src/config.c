#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "../include/config.h"

#define MAX_LINE_LENGTH 256

static char* trim(char* str) {
    char* end;
    while(isspace((unsigned char)*str)) str++;
    if(*str == 0) return str;
    end = str + strlen(str) - 1;
    while(end > str && isspace((unsigned char)*end)) end--;
    end[1] = '\0';
    return str;
}

static void parse_hidden_layers(const char* value, MLPConfig* config) {
    char* value_copy = strdup(value);
    char* token;
    int count = 1;
    
    // Contar número de capas
    for (const char* p = value; *p; p++) {
        if (*p == ',') count++;
    }
    
    config->hidden_layers = (int*)malloc(count * sizeof(int));
    config->num_hidden_layers = count;
    
    // Parsear valores
    int i = 0;
    token = strtok(value_copy, ",");
    while (token != NULL && i < count) {
        config->hidden_layers[i++] = atoi(trim(token));
        token = strtok(NULL, ",");
    }
    
    free(value_copy);
}

MLPConfig* create_default_config(void) {
    MLPConfig* config = (MLPConfig*)malloc(sizeof(MLPConfig));
    
    config->epochs = 100;
    config->batch_size = 64;
    config->learning_rate = 0.01;
    config->lr_decay = 0.98;
    config->momentum = 0.9;
    config->weight_decay = 0.0001;
    config->early_stopping_patience = 15;
    config->min_delta = 0.001;
    config->seed = 42;
    config->verbose = 1;
    
    // Arquitectura por defecto: 20,10
    config->num_hidden_layers = 2;
    config->hidden_layers = (int*)malloc(2 * sizeof(int));
    config->hidden_layers[0] = 20;
    config->hidden_layers[1] = 10;
    
    return config;
}

MLPConfig* load_config(const char* config_file) {
    FILE* file = fopen(config_file, "r");
    if (!file) {
        fprintf(stderr, "Advertencia: No se pudo abrir archivo de configuración '%s'\n", config_file);
        fprintf(stderr, "Usando configuración por defecto...\n");
        return create_default_config();
    }
    
    MLPConfig* config = create_default_config();
    char line[MAX_LINE_LENGTH];
    
    while (fgets(line, sizeof(line), file)) {
        // Ignorar comentarios y líneas vacías
        char* trimmed = trim(line);
        if (trimmed[0] == '#' || trimmed[0] == '\0') {
            continue;
        }
        
        // Buscar '='
        char* equals = strchr(trimmed, '=');
        if (!equals) continue;
        
        *equals = '\0';
        char* key = trim(trimmed);
        char* value = trim(equals + 1);
        
        // Parsear valores
        if (strcmp(key, "epochs") == 0) {
            config->epochs = atoi(value);
        } else if (strcmp(key, "batch_size") == 0) {
            config->batch_size = atoi(value);
        } else if (strcmp(key, "learning_rate") == 0) {
            config->learning_rate = atof(value);
        } else if (strcmp(key, "lr_decay") == 0) {
            config->lr_decay = atof(value);
        } else if (strcmp(key, "momentum") == 0) {
            config->momentum = atof(value);
        } else if (strcmp(key, "weight_decay") == 0) {
            config->weight_decay = atof(value);
        } else if (strcmp(key, "early_stopping_patience") == 0) {
            config->early_stopping_patience = atoi(value);
        } else if (strcmp(key, "min_delta") == 0) {
            config->min_delta = atof(value);
        } else if (strcmp(key, "seed") == 0) {
            config->seed = atoi(value);
        } else if (strcmp(key, "verbose") == 0) {
            config->verbose = atoi(value);
        } else if (strcmp(key, "hidden_layers") == 0) {
            free(config->hidden_layers);
            parse_hidden_layers(value, config);
        }
    }
    
    fclose(file);
    return config;
}

void free_config(MLPConfig* config) {
    if (config) {
        if (config->hidden_layers) {
            free(config->hidden_layers);
        }
        free(config);
    }
}

void print_config(const MLPConfig* config) {
    printf("\n========================================\n");
    printf("CONFIGURACIÓN DEL MODELO\n");
    printf("========================================\n");
    printf("Epochs:                  %d\n", config->epochs);
    printf("Batch size:              %d\n", config->batch_size);
    printf("Learning rate inicial:   %.4f\n", config->learning_rate);
    printf("Learning rate decay:     %.4f\n", config->lr_decay);
    printf("Momentum:                %.4f\n", config->momentum);
    printf("Weight decay (L2):       %.6f\n", config->weight_decay);
    printf("Early stopping patience: %d\n", config->early_stopping_patience);
    printf("Min delta:               %.6f\n", config->min_delta);
    printf("Seed:                    %d\n", config->seed);
    printf("Verbose:                 %d\n", config->verbose);
    printf("Capas ocultas:           ");
    for (int i = 0; i < config->num_hidden_layers; i++) {
        printf("%d", config->hidden_layers[i]);
        if (i < config->num_hidden_layers - 1) printf(",");
    }
    printf("\n========================================\n\n");
}
