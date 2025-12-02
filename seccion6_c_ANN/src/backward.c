#include <string.h>
#include <stdlib.h>
#include "../include/backward.h"
#include "../include/activation.h"

void zero_gradients(MLP* mlp) {
    for (int l = 0; l < mlp->num_layers; l++) {
        Layer* layer = mlp->layers[l];
        for (int i = 0; i < layer->num_neurons; i++) {
            layer->bias_grads[i] = 0.0;
            for (int j = 0; j < layer->num_inputs; j++) {
                layer->weight_grads[i][j] = 0.0;
            }
        }
    }
}

void backward_pass(MLP* mlp, double* input, int true_label) {
    Layer* output_layer = mlp->layers[mlp->num_layers - 1];
    
    for (int i = 0; i < output_layer->num_neurons; i++) {
        if (i == true_label) {
            output_layer->deltas[i] = output_layer->outputs[i] - 1.0;
        } else {
            output_layer->deltas[i] = output_layer->outputs[i];
        }
    }
    
    for (int l = mlp->num_layers - 2; l >= 0; l--) {
        Layer* current = mlp->layers[l];
        Layer* next = mlp->layers[l + 1];
        
        for (int i = 0; i < current->num_neurons; i++) {
            double sum = 0.0;
            for (int j = 0; j < next->num_neurons; j++) {
                sum += next->weights[j][i] * next->deltas[j];
            }
            
            double derivative;
            if (strcmp(current->activation, "relu") == 0) {
                derivative = current->outputs[i] > 0 ? 1.0 : 0.0;
            } else if (strcmp(current->activation, "sigmoid") == 0) {
                derivative = current->outputs[i] * (1.0 - current->outputs[i]);
            } else if (strcmp(current->activation, "tanh") == 0) {
                derivative = 1.0 - current->outputs[i] * current->outputs[i];
            } else {
                derivative = 1.0;
            }
            
            current->deltas[i] = sum * derivative;
        }
    }
    
    for (int l = 0; l < mlp->num_layers; l++) {
        Layer* layer = mlp->layers[l];
        double* prev_outputs;
        
        if (l == 0) {
            prev_outputs = input;
        } else {
            prev_outputs = mlp->layers[l-1]->outputs;
        }
        
        for (int i = 0; i < layer->num_neurons; i++) {
            layer->bias_grads[i] += layer->deltas[i];
            for (int j = 0; j < layer->num_inputs; j++) {
                layer->weight_grads[i][j] += layer->deltas[i] * prev_outputs[j];
            }
        }
    }
}
