#include <math.h>
#include <string.h>
#include <stdio.h>
#include "../include/activation.h"

void relu(double* input, double* output, int size) {
    for (int i = 0; i < size; i++) {
        output[i] = input[i] > 0 ? input[i] : 0;
    }
}

void relu_derivative(double* input, double* output, int size) {
    for (int i = 0; i < size; i++) {
        output[i] = input[i] > 0 ? 1.0 : 0.0;
    }
}

void sigmoid_func(double* input, double* output, int size) {
    for (int i = 0; i < size; i++) {
        output[i] = 1.0 / (1.0 + exp(-input[i]));
    }
}

void sigmoid_derivative(double* input, double* output, int size) {
    for (int i = 0; i < size; i++) {
        double s = 1.0 / (1.0 + exp(-input[i]));
        output[i] = s * (1.0 - s);
    }
}

void tanh_func(double* input, double* output, int size) {
    for (int i = 0; i < size; i++) {
        output[i] = tanh(input[i]);
    }
}

void tanh_derivative(double* input, double* output, int size) {
    for (int i = 0; i < size; i++) {
        double t = tanh(input[i]);
        output[i] = 1.0 - t * t;
    }
}

void softmax(double* input, double* output, int size) {
    double max_val = input[0];
    for (int i = 1; i < size; i++) {
        if (input[i] > max_val) {
            max_val = input[i];
        }
    }
    
    double sum = 0.0;
    for (int i = 0; i < size; i++) {
        output[i] = exp(input[i] - max_val);
        sum += output[i];
    }
    
    for (int i = 0; i < size; i++) {
        output[i] /= sum;
    }
}
