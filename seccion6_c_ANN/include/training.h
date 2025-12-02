#ifndef TRAINING_H
#define TRAINING_H

#include "types.h"

void train_mlp(MLP* mlp, Dataset* train_data, Dataset* val_data, TrainConfig* config);
double compute_loss(MLP* mlp, Dataset* data);

#endif
