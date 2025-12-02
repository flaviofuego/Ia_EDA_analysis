#ifndef FORWARD_H
#define FORWARD_H

#include "types.h"

void forward_pass(MLP* mlp, double* input);
void forward_layer(Layer* layer, double* input);

#endif
