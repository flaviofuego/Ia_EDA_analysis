#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include "../include/training.h"
#include "../include/training_logger.h"
#include "../include/forward.h"
#include "../include/backward.h"
#include "../include/optimizer.h"
#include "../include/prediction.h"

double compute_loss(MLP* mlp, Dataset* data) {
    double total_loss = 0.0;
    
    for (int i = 0; i < data->num_samples; i++) {
        forward_pass(mlp, data->data[i].features);
        Layer* output = mlp->layers[mlp->num_layers - 1];
        
        double prob = output->outputs[data->data[i].label];
        if (prob < 1e-10) prob = 1e-10;
        total_loss += -log(prob);
    }
    
    return total_loss / data->num_samples;
}

void train_mlp(MLP* mlp, Dataset* train_data, Dataset* val_data, TrainConfig* config) {
    double best_val_loss = 1e10;
    int patience_counter = 0;
    clock_t start_time = clock();
    
    // Crear logger para guardar datos de entrenamiento
    TrainingLogger* logger = create_training_logger("training_history.csv");
    write_logger_header(logger);
    
    printf("\n========== INICIANDO ENTRENAMIENTO ==========\n");
    printf("Epochs: %d, Batch size: %d, Learning rate: %.4f\n", 
           config->epochs, config->batch_size, config->learning_rate);
    printf("Momentum: %.2f, Weight decay: %.5f\n", 
           config->momentum, config->weight_decay);
    printf("============================================\n\n");
    
    mlp->momentum = config->momentum;
    mlp->weight_decay = config->weight_decay;
    
    for (int epoch = 0; epoch < config->epochs; epoch++) {
        shuffle_dataset(train_data, config->seed + epoch);
        
        double epoch_loss = 0.0;
        int num_batches = (train_data->num_samples + config->batch_size - 1) / config->batch_size;
        
        for (int batch_idx = 0; batch_idx < num_batches; batch_idx++) {
            zero_gradients(mlp);
            
            int start = batch_idx * config->batch_size;
            int end = start + config->batch_size;
            if (end > train_data->num_samples) {
                end = train_data->num_samples;
            }
            int batch_size = end - start;
            
            for (int i = start; i < end; i++) {
                forward_pass(mlp, train_data->data[i].features);
                
                Layer* output = mlp->layers[mlp->num_layers - 1];
                double prob = output->outputs[train_data->data[i].label];
                if (prob < 1e-10) prob = 1e-10;
                epoch_loss += -log(prob);
                
                backward_pass(mlp, train_data->data[i].features, train_data->data[i].label);
            }
            
            update_weights_momentum(mlp, batch_size);
        }
        
        double train_loss = epoch_loss / train_data->num_samples;
        double val_loss = compute_loss(mlp, val_data);
        
        int* val_preds = (int*)malloc(val_data->num_samples * sizeof(int));
        predict_batch(mlp, val_data, val_preds);
        int correct = 0;
        for (int i = 0; i < val_data->num_samples; i++) {
            if (val_preds[i] == val_data->data[i].label) {
                correct++;
            }
        }
        double val_acc = (double)correct / val_data->num_samples;
        free(val_preds);
        
        // Calcular tiempo transcurrido
        clock_t current_time = clock();
        double elapsed = (double)(current_time - start_time) / CLOCKS_PER_SEC;
        
        // Guardar datos en CSV
        log_epoch(logger, epoch + 1, config->epochs, train_loss, val_loss, 
                  val_acc, mlp->learning_rate, elapsed);
        
        if (config->verbose >= 1) {
            printf("Epoch %3d/%d | Train Loss: %.4f | Val Loss: %.4f | Val Acc: %.4f | LR: %.5f\n",
                   epoch + 1, config->epochs, train_loss, val_loss, val_acc, mlp->learning_rate);
        }
        
        mlp->learning_rate *= config->lr_decay;
        
        if (val_loss < best_val_loss - config->min_delta) {
            best_val_loss = val_loss;
            patience_counter = 0;
        } else {
            patience_counter++;
            if (patience_counter >= config->early_stopping) {
                printf("\nEarly stopping en epoch %d (mejor val_loss: %.4f)\n", epoch + 1, best_val_loss);
                break;
            }
        }
    }
    
    // Cerrar logger
    close_training_logger(logger);
    printf("\n✓ Datos de entrenamiento guardados en tasks/training_history.csv\n");
    printf("\n========== ENTRENAMIENTO COMPLETADO ==========\n");
}
