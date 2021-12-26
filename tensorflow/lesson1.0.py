# Example: turning strings into sequences of one-hot encoded bigrams



import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import TextVectorization

# Example training data, of dtype `string`.
