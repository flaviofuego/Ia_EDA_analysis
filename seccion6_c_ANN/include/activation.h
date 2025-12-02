#ifndef ACTIVATION_H
#define ACTIVATION_H

void relu(double* input, double* output, int size);
void relu_derivative(double* input, double* output, int size);
void sigmoid_func(double* input, double* output, int size);
void sigmoid_derivative(double* input, double* output, int size);
void tanh_func(double* input, double* output, int size);
void tanh_derivative(double* input, double* output, int size);
void softmax(double* input, double* output, int size);

#endif
