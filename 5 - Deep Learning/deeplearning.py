import tensorflow as tf

def mean_absolute_error():
    return tf.keras.metrics.mean_absolute_error(y_true, y_pred)

def mean_squared_error():
    return tf.keras.metrics.mean_squared_error(y_true, y_pred)