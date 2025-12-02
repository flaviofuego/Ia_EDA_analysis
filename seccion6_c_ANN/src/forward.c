#include <string.h>
#include "../include/forward.h"
#include "../include/activation.h"

void forward_layer(Layer* layer, double* input) {
    for (int i = 0; i < layer->num_neurons; i++) {
        layer->pre_activation[i] = layer->biases[i];
        for (int j = 0; j < layer->num_inputs; j++) {
            layer->pre_activation[i] += layer->weights[i][j] * input[j];
        }
    }
    
    if (strcmp(layer->activation, "relu") == 0) {
        relu(layer->pre_activation, layer->outputs, layer->num_neurons);
    } else if (strcmp(layer->activation, "sigmoid") == 0) {
        sigmoid_func(layer->pre_activation, layer->outputs, layer->num_neurons);
    } else if (strcmp(layer->activation, "tanh") == 0) {
        tanh_func(layer->pre_activation, layer->outputs, layer->num_neurons);
    } else if (strcmp(layer->activation, "softmax") == 0) {
        softmax(layer->pre_activation, layer->outputs, layer->num_neurons);
    }
}

void forward_pass(MLP* mlp, double* input) {
    forward_layer(mlp->layers[0], input);
    
    for (int i = 1; i < mlp->num_layers; i++) {
        forward_layer(mlp->layers[i], mlp->layers[i-1]->outputs);
    }
}
