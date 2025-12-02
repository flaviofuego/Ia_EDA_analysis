#ifndef METRICS_H
#define METRICS_H

#include "types.h"

Metrics* compute_metrics(MLP* mlp, Dataset* data);
void compute_confusion_matrix(int* predictions, Dataset* data, int** conf_matrix);
double compute_accuracy(int* predictions, Dataset* data);
double compute_balanced_accuracy(Metrics* metrics);
double compute_f1_weighted(Metrics* metrics, Dataset* data);
void print_metrics(Metrics* metrics, const char* dataset_name);
void free_metrics(Metrics* metrics);

#endif
