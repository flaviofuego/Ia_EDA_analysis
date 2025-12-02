#include "../include/optimizer.h"

void update_weights_sgd(MLP* mlp, int batch_size) {
    for (int l = 0; l < mlp->num_layers; l++) {
        Layer* layer = mlp->layers[l];
        
        for (int i = 0; i < layer->num_neurons; i++) {
            layer->biases[i] -= mlp->learning_rate * (layer->bias_grads[i] / batch_size);
            
            for (int j = 0; j < layer->num_inputs; j++) {
                double grad = layer->weight_grads[i][j] / batch_size;
                double reg = mlp->weight_decay * layer->weights[i][j];
                layer->weights[i][j] -= mlp->learning_rate * (grad + reg);
            }
        }
    }
}

void update_weights_momentum(MLP* mlp, int batch_size) {
    for (int l = 0; l < mlp->num_layers; l++) {
        Layer* layer = mlp->layers[l];
        
        for (int i = 0; i < layer->num_neurons; i++) {
            double grad_b = layer->bias_grads[i] / batch_size;
            mlp->velocity_b[l][i] = mlp->momentum * mlp->velocity_b[l][i] + mlp->learning_rate * grad_b;
            layer->biases[i] -= mlp->velocity_b[l][i];
            
            for (int j = 0; j < layer->num_inputs; j++) {
                double grad = layer->weight_grads[i][j] / batch_size;
                double reg = mlp->weight_decay * layer->weights[i][j];
                mlp->velocity_w[l][i][j] = mlp->momentum * mlp->velocity_w[l][i][j] + 
                                           mlp->learning_rate * (grad + reg);
                layer->weights[i][j] -= mlp->velocity_w[l][i][j];
            }
        }
    }
}
