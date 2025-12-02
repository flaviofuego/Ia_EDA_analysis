#ifndef BACKWARD_H
#define BACKWARD_H

#include "types.h"

void backward_pass(MLP* mlp, double* input, int true_label);
void zero_gradients(MLP* mlp);

#endif
