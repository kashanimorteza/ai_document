#--------------------------------------------------------------Import
import numpy as np
import tensorflow as tf
import keras as ks

#--------------------------------------------------------------SimpleDense
class SimpleDense(ks.layers.Layer):

    def __init__(self, units):
        super().__init__()
        self.units = units

    def build(self, input_shape):
        w_init = tf.random_uniform_initializer()
        self.w = tf.Variable(
            initial_value=w_init(shape=(input_shape[-1], self.units), dtype="float32"), 
            trainable=True, 
            name="kernel"
        )

        b_init = tf.zeros_initializer()
        self.b = tf.Variable(
            initial_value=b_init(shape=(1, self.units), dtype="float32"), 
            trainable=True, 
            name="bias"
        )

    def call(self, inputs):
        return tf.matmul(inputs, self.w) + self.b
    
#--------------------------------------------------------------Action
#---X
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=np.float32).reshape(-1, 1)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=np.float32).reshape(-1, 1)

#---Model
model = ks.Sequential(
    [
        SimpleDense(1)
    ]
)
model.compile(optimizer="sgd", loss = "mean_squared_error")

#---Train
model.fit(xs, ys, epochs = 3, verbose=0)

#---Predict
xp = np.array([10], dtype=np.float32).reshape(-1, 1)
yp = model.predict(xp)

#---Log
print("Variables (w)", model.variables)
print("Predict   (10)", yp)