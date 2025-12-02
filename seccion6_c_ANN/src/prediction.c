#include "../include/prediction.h"
#include "../include/forward.h"

int predict(MLP* mlp, double* input) {
    forward_pass(mlp, input);
    
    Layer* output_layer = mlp->layers[mlp->num_layers - 1];
    int max_idx = 0;
    double max_val = output_layer->outputs[0];
    
    for (int i = 1; i < output_layer->num_neurons; i++) {
        if (output_layer->outputs[i] > max_val) {
            max_val = output_layer->outputs[i];
            max_idx = i;
        }
    }
    
    return max_idx;
}

void predict_proba(MLP* mlp, double* input, double* probabilities) {
    forward_pass(mlp, input);
    
    Layer* output_layer = mlp->layers[mlp->num_layers - 1];
    for (int i = 0; i < output_layer->num_neurons; i++) {
        probabilities[i] = output_layer->outputs[i];
    }
}

void predict_batch(MLP* mlp, Dataset* data, int* predictions) {
    for (int i = 0; i < data->num_samples; i++) {
        predictions[i] = predict(mlp, data->data[i].features);
    }
}
