#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include "../include/mlp_core.h"

Layer* create_layer(int num_neurons, int num_inputs, const char* activation) {
    Layer* layer = (Layer*)malloc(sizeof(Layer));
    layer->num_neurons = num_neurons;
    layer->num_inputs = num_inputs;
    strcpy(layer->activation, activation);
    
    layer->weights = (double**)malloc(num_neurons * sizeof(double*));
    layer->weight_grads = (double**)malloc(num_neurons * sizeof(double*));
    for (int i = 0; i < num_neurons; i++) {
        layer->weights[i] = (double*)malloc(num_inputs * sizeof(double));
        layer->weight_grads[i] = (double*)calloc(num_inputs, sizeof(double));
    }
    
    layer->biases = (double*)calloc(num_neurons, sizeof(double));
    layer->bias_grads = (double*)calloc(num_neurons, sizeof(double));
    layer->outputs = (double*)malloc(num_neurons * sizeof(double));
    layer->pre_activation = (double*)malloc(num_neurons * sizeof(double));
    layer->deltas = (double*)malloc(num_neurons * sizeof(double));
    
    return layer;
}

void initialize_weights(Layer* layer, const char* method) {
    srand(time(NULL));
    double scale;
    
    if (strcmp(method, "xavier") == 0) {
        scale = sqrt(6.0 / (layer->num_inputs + layer->num_neurons));
    } else if (strcmp(method, "he") == 0) {
        scale = sqrt(2.0 / layer->num_inputs);
    } else {
        scale = 0.1;
    }
    
    for (int i = 0; i < layer->num_neurons; i++) {
        for (int j = 0; j < layer->num_inputs; j++) {
            double r = ((double)rand() / RAND_MAX) * 2.0 - 1.0;
            layer->weights[i][j] = r * scale;
        }
    }
}

MLP* create_mlp(int input_size, int* layer_sizes, int num_layers, const char** activations, double learning_rate) {
    MLP* mlp = (MLP*)malloc(sizeof(MLP));
    mlp->num_layers = num_layers;
    mlp->input_size = input_size;
    mlp->output_size = layer_sizes[num_layers - 1];
    mlp->learning_rate = learning_rate;
    mlp->momentum = 0.9;
    mlp->weight_decay = 0.0001;
    
    mlp->layers = (Layer**)malloc(num_layers * sizeof(Layer*));
    
    int prev_size = input_size;
    for (int i = 0; i < num_layers; i++) {
        mlp->layers[i] = create_layer(layer_sizes[i], prev_size, activations[i]);
        
        if (strcmp(activations[i], "relu") == 0) {
            initialize_weights(mlp->layers[i], "he");
        } else {
            initialize_weights(mlp->layers[i], "xavier");
        }
        
        prev_size = layer_sizes[i];
    }
    
    mlp->velocity_w = (double***)malloc(num_layers * sizeof(double**));
    mlp->velocity_b = (double**)malloc(num_layers * sizeof(double*));
    
    for (int i = 0; i < num_layers; i++) {
        mlp->velocity_w[i] = (double**)malloc(mlp->layers[i]->num_neurons * sizeof(double*));
        for (int j = 0; j < mlp->layers[i]->num_neurons; j++) {
            mlp->velocity_w[i][j] = (double*)calloc(mlp->layers[i]->num_inputs, sizeof(double));
        }
        mlp->velocity_b[i] = (double*)calloc(mlp->layers[i]->num_neurons, sizeof(double));
    }
    
    return mlp;
}

void free_layer(Layer* layer) {
    if (layer) {
        for (int i = 0; i < layer->num_neurons; i++) {
            free(layer->weights[i]);
            free(layer->weight_grads[i]);
        }
        free(layer->weights);
        free(layer->weight_grads);
        free(layer->biases);
        free(layer->bias_grads);
        free(layer->outputs);
        free(layer->pre_activation);
        free(layer->deltas);
        free(layer);
    }
}

void free_mlp(MLP* mlp) {
    if (mlp) {
        for (int i = 0; i < mlp->num_layers; i++) {
            free_layer(mlp->layers[i]);
            for (int j = 0; j < mlp->layers[i]->num_neurons; j++) {
                free(mlp->velocity_w[i][j]);
            }
            free(mlp->velocity_w[i]);
            free(mlp->velocity_b[i]);
        }
        free(mlp->layers);
        free(mlp->velocity_w);
        free(mlp->velocity_b);
        free(mlp);
    }
}
