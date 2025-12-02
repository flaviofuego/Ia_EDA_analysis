#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "../include/data_utils.h"

Dataset* load_dataset(const char* filename, int num_features, int num_classes) {
    FILE* file = fopen(filename, "r");
    if (!file) {
        fprintf(stderr, "Error: Cannot open file %s\n", filename);
        return NULL;
    }
    
    int num_samples = 0;
    char buffer[4096];
    
    while (fgets(buffer, sizeof(buffer), file)) {
        num_samples++;
    }
    
    rewind(file);
    
    Dataset* dataset = (Dataset*)malloc(sizeof(Dataset));
    dataset->num_samples = num_samples;
    dataset->num_features = num_features;
    dataset->num_classes = num_classes;
    dataset->data = (DataPoint*)malloc(num_samples * sizeof(DataPoint));
    dataset->feature_means = (double*)calloc(num_features, sizeof(double));
    dataset->feature_stds = (double*)calloc(num_features, sizeof(double));
    
    for (int i = 0; i < num_samples; i++) {
        dataset->data[i].features = (double*)malloc(num_features * sizeof(double));
        dataset->data[i].num_features = num_features;
    }
    
    int idx = 0;
    while (fgets(buffer, sizeof(buffer), file) && idx < num_samples) {
        char* token = strtok(buffer, ",");
        int feat_idx = 0;
        
        while (token != NULL && feat_idx < num_features) {
            dataset->data[idx].features[feat_idx] = atof(token);
            feat_idx++;
            token = strtok(NULL, ",");
        }
        
        if (token != NULL) {
            dataset->data[idx].label = atoi(token);
        }
        idx++;
    }
    
    fclose(file);
    return dataset;
}

void normalize_dataset(Dataset* dataset) {
    for (int j = 0; j < dataset->num_features; j++) {
        double sum = 0.0;
        for (int i = 0; i < dataset->num_samples; i++) {
            sum += dataset->data[i].features[j];
        }
        dataset->feature_means[j] = sum / dataset->num_samples;
        
        double var_sum = 0.0;
        for (int i = 0; i < dataset->num_samples; i++) {
            double diff = dataset->data[i].features[j] - dataset->feature_means[j];
            var_sum += diff * diff;
        }
        dataset->feature_stds[j] = sqrt(var_sum / dataset->num_samples);
        
        if (dataset->feature_stds[j] < 1e-8) {
            dataset->feature_stds[j] = 1.0;
        }
        
        for (int i = 0; i < dataset->num_samples; i++) {
            dataset->data[i].features[j] = 
                (dataset->data[i].features[j] - dataset->feature_means[j]) / dataset->feature_stds[j];
        }
    }
}

void shuffle_dataset(Dataset* dataset, unsigned int seed) {
    srand(seed);
    for (int i = dataset->num_samples - 1; i > 0; i--) {
        int j = rand() % (i + 1);
        DataPoint temp = dataset->data[i];
        dataset->data[i] = dataset->data[j];
        dataset->data[j] = temp;
    }
}

void split_dataset(Dataset* source, Dataset** train, Dataset** test, double test_ratio, unsigned int seed) {
    shuffle_dataset(source, seed);
    
    int test_size = (int)(source->num_samples * test_ratio);
    int train_size = source->num_samples - test_size;
    
    *train = (Dataset*)malloc(sizeof(Dataset));
    *test = (Dataset*)malloc(sizeof(Dataset));
    
    (*train)->num_samples = train_size;
    (*train)->num_features = source->num_features;
    (*train)->num_classes = source->num_classes;
    (*train)->data = (DataPoint*)malloc(train_size * sizeof(DataPoint));
    (*train)->feature_means = source->feature_means;
    (*train)->feature_stds = source->feature_stds;
    
    (*test)->num_samples = test_size;
    (*test)->num_features = source->num_features;
    (*test)->num_classes = source->num_classes;
    (*test)->data = (DataPoint*)malloc(test_size * sizeof(DataPoint));
    (*test)->feature_means = source->feature_means;
    (*test)->feature_stds = source->feature_stds;
    
    for (int i = 0; i < train_size; i++) {
        (*train)->data[i] = source->data[i];
    }
    
    for (int i = 0; i < test_size; i++) {
        (*test)->data[i] = source->data[train_size + i];
    }
}

void free_dataset(Dataset* dataset) {
    if (dataset) {
        if (dataset->data) {
            for (int i = 0; i < dataset->num_samples; i++) {
                free(dataset->data[i].features);
            }
            free(dataset->data);
        }
        free(dataset->feature_means);
        free(dataset->feature_stds);
        free(dataset);
    }
}
