#ifndef PREDICTION_H
#define PREDICTION_H

#include "types.h"

int predict(MLP* mlp, double* input);
void predict_proba(MLP* mlp, double* input, double* probabilities);
void predict_batch(MLP* mlp, Dataset* data, int* predictions);

#endif
