#ifndef MLP_CORE_H
#define MLP_CORE_H

#include "types.h"

MLP* create_mlp(int input_size, int* layer_sizes, int num_layers, const char** activations, double learning_rate);
Layer* create_layer(int num_neurons, int num_inputs, const char* activation);
void initialize_weights(Layer* layer, const char* method);
void free_mlp(MLP* mlp);
void free_layer(Layer* layer);

#endif
