#ifndef DATA_UTILS_H
#define DATA_UTILS_H

#include "types.h"

Dataset* load_dataset(const char* filename, int num_features, int num_classes);
void normalize_dataset(Dataset* dataset);
void split_dataset(Dataset* source, Dataset** train, Dataset** test, double test_ratio, unsigned int seed);
void shuffle_dataset(Dataset* dataset, unsigned int seed);
void free_dataset(Dataset* dataset);

#endif
