<!--------------------------------------------------------------------------------- Description -->
# Tensorflow
    AI : Develop : Package



<!--------------------------------------------------------------------------------- Networks -->
<br><br>

## Networks
<!-------------------------- Sequential -->
### Sequential
```
```
<!-------------------------- Functional API -->
### Functional API
```
Multiple input and multiple output structures
Parallel structures like Inception and ResNet
```
```
Network input definition
Defining parameters and their connections
Model making
```
```
Fast RCNN
Multi Label Classification
```
<!-------------------------- Model Subclassing -->
### Model Subclassing
```
The best way for GAN Networks
```



<!--------------------------------------------------------------------------------- Leyer -->
<br><br>

## Leyer

<!-------------------------- Type -->
### Type
```
Lambda
Trainable
```
<!-------------------------- Structure -->
### Structure
```
Parameter (State) : Weights 
Computing (Forward Pass)
```
<!-------------------------- Dense -->
### Dense
```
State     : W | Bias
Computing : Y=X*W+b
Input     : Vector 
```



<!--------------------------------------------------------------------------------- Mode -->
<br><br>

## Mode
<!-------------------------- Graph -->
### Graph
Used for
```

```

<!-------------------------- Eager -->
### Eager
Features
```
Evaluate Values immediately
Broadcast Support
Operator Overloading
Numpy Compatibility
```


<!--------------------------------------------------------------------------------- Decorators -->
<br><br>

## Decorators

### @tf.function
```
Convert Eager to Graph
```



<!--------------------------------------------------------------------------------- Automatic differentiation -->
<br><br>

## Automatic differentiation
```
Automatic Differentiation (AD)
Derivative | Gradient | backpropagation
is a technique that lets computers automatically calculate derivatives (gradients) of functions
It’s the method TensorFlow use to compute how your loss changes with respect to your model’s parameters
These gradients tell the optimizer how to adjust weights to make predictions better — it’s the core of backpropagation
```

```
Forward Mode
Reverse Mode
```

tf.GradientTape
```
```



<!--------------------------------------------------------------------------------- CallBack -->
<br><br>

## CallBack 
```
A callback is a function that TensorFlow/Keras automatically calls at specific points during training :
    before or after each epoch,
    before or after each batch,
    or at the beginning or end of training.

Callbacks let you monitor, control, and modify the training process while it’s running
```
```
BaseLogger
CSVLogger
EarlyStopping
LambdaCallback
LearningRateScheduler
ModelCheckpoint
ProgbarLogger
ReduceLROnPlateau
RemoteMonitor
TensorBoard
TerminateOnNaN
BackupAndRestore
History
TimeStopping
```