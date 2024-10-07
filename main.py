import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

# load in dataset CIFAR-10 to train image detection
(x_train, y_train), (x_test, y_test) = datasets.cifar10.load_data()

print(x_train)