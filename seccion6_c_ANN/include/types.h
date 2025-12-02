#ifndef TYPES_H
#define TYPES_H

typedef struct {
    double* features;
    int num_features;
    int label;
} DataPoint;

typedef struct {
    DataPoint* data;
    int num_samples;
    int num_features;
    int num_classes;
    double* feature_means;
    double* feature_stds;
} Dataset;

typedef struct {
    int num_neurons;
    int num_inputs;
    double** weights;
    double* biases;
    double* outputs;
    double* pre_activation;
    double* deltas;
    double** weight_grads;
    double* bias_grads;
    char activation[16];
} Layer;

typedef struct {
    Layer** layers;
    int num_layers;
    int input_size;
    int output_size;
    double learning_rate;
    double momentum;
    double weight_decay;
    double*** velocity_w;
    double** velocity_b;
} MLP;

typedef struct {
    int epochs;
    int batch_size;
    double learning_rate;
    double lr_decay;
    double momentum;
    double weight_decay;
    int early_stopping;
    double min_delta;
    int verbose;
    unsigned int seed;
} TrainConfig;

typedef struct {
    double accuracy;
    double balanced_acc;
    double f1_weighted;
    double precision;
    double recall;
    int** confusion_matrix;
    double* per_class_acc;
    double* per_class_f1;
    int num_classes;
} Metrics;

#endif
