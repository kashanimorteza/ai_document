<!--------------------------------------------------------------------------------- Overfitting -->
# Overfitting
    AI : Subject



<!--------------------------------------------------------------------------------- Description -->
<br><br>

## Description
```
اختلاف خطای داده‌های تست و ترین زیاد باشد
داده ها Generalization ندارند
```



<!--------------------------------------------------------------------------------- Data-Level Techniques -->
<br><br>

## Data-Level Techniques
    Data Augmentation
    Data Normalization
    Data Cleaning
    Feature Engineering
    Feature Selection
    Synthetic Data Generation
    Cross-Validation
    Shuffling Data
    Balancing Classes (e.g., SMOTE)
    More Training Data
    Noise Injection (label noise or input noise)



<!--------------------------------------------------------------------------------- Model-Level Techniques -->
<br><br>

## Model-Level Techniques
    Simplify Model Architecture
    Reduce Number of Layers
    Reduce Number of Neurons
    Weight Regularization (L1, L2, ElasticNet)
    Dropout
    Batch Normalization
    Early Stopping
    Weight Sharing
    Parameter Tying
    Skip Connections (ResNet-style)



<!--------------------------------------------------------------------------------- Training-Level Techniques -->
<br><br>

## Training-Level Techniques
    Early Stopping
    Learning Rate Scheduling
    Gradient Clipping
    Mini-Batch Training
    Loss Function Regularization
    Optimizer Tuning (Adam, RMSProp, SGD with momentum)
    Ensembling (Bagging, Boosting, Stacking)
    Cross-Validation during training
    Hyperparameter Optimization
    Transfer Learning (using pretrained models)



<!--------------------------------------------------------------------------------- Regularization Methods -->
<br><br>

## Regularization Methods
    L1 Regularization (Lasso)
    L2 Regularization (Ridge)
    ElasticNet Regularization
    Dropout
    Label Smoothing
    Activity Regularization
    Weight Decay
    Noise Regularization
    Data Augmentation Regularization



<!--------------------------------------------------------------------------------- Evaluation / Validation Strategies -->
<br><br>

## Evaluation / Validation Strategies
    Use Separate Validation Set
    Use K-Fold Cross-Validation
    Monitor Validation Loss
    Use Early Stopping on Validation Loss
    Avoid Data Leakage
    Use Proper Train/Test Split



<!--------------------------------------------------------------------------------- Ensemble & Averaging Methods -->
<br><br>

## Ensemble & Averaging Methods
    Bagging (Bootstrap Aggregating)
    Boosting (AdaBoost, XGBoost)
    Stacking
    Voting Classifier
    Model Averaging
    Snapshot Ensembling



<!--------------------------------------------------------------------------------- Advanced / Modern Approaches -->
<br><br>

## Advanced / Modern Approaches
    Transfer Learning
    Fine-Tuning Pretrained Models
    Knowledge Distillation
    Regularized Pretraining
    Contrastive Learning
    Mixup / CutMix
    DropConnect
    Stochastic Depth
    Monte Carlo Dropout (Bayesian approximation)



<!--------------------------------------------------------------------------------- Other Practical Techniques -->
<br><br>

## Other Practical Techniques
    Reduce Training Time
    Reduce Learning Rate
    Use Proper Batch Size
    Use Weight Initialization (He, Xavier)
    Use Noise in Inputs or Layers
    Use Proper Activation Functions
    Monitor Metrics (Accuracy vs Loss)