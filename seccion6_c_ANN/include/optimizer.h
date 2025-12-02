#ifndef OPTIMIZER_H
#define OPTIMIZER_H

#include "types.h"

void update_weights_sgd(MLP* mlp, int batch_size);
void update_weights_momentum(MLP* mlp, int batch_size);

#endif
