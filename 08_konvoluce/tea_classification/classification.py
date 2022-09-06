import os
import random
import tensorflow as tf
import numpy as np

from keras.preprocessing.image import load_img, img_to_array, ImageDataGenerator
from keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from keras.layers import InputLayer, Conv2D, MaxPool2D, Flatten, Dense, Activation
from keras.activations import linear, relu, softmax


cwd = os.getcwd()
print("-----loading model")
model = VGG16()

print("------processing-input")
# Image.open(os.path.join(cwd, "dataset_resized/pu-erh", "3.jpg"))
image = load_img(os.path.join(cwd, "dataset_resized/pu-erh", "3.jpg"), target_size=(224, 224))
image = img_to_array(image)
image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
image = preprocess_input(image)


print("-----prediction")
yhat = model.predict(image)
labels = decode_predictions(yhat)
label = labels[0][0]
print('%s (%.2f%%)' % (label[1], label[2]*100))
print(labels)


# nb_classes = 5
# input_shape = (128, 128, 1)

# (x_train, y_train), (x_test, y_test) = mnist.load_data()
# x_train = x_train.astype('float32')
# x_test = x_test.astype('float32')
# mnist_class_labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# model = tf.keras.models.Sequential([])
# model.add(InputLayer(input_shape = input_shape))
# model.add(Conv2D(filters=32, kernel_size=(5, 5)))
# model.add(MaxPool2D(strides=2, pool_size=(2, 2)))
# model.add(Conv2D(filters=64, kernel_size=5, activation=relu))
# model.add(MaxPool2D(strides=2, pool_size=(2, 2)))
# model.add(Flatten(name='Flatten'))
# model.add(Dense(units=30, activation=relu))
# model.add(Dense(units=nb_classes, activation=linear, name='logits'))
# model.add(Activation(activation=softmax))

# model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# model.fit(x_train, y_train, batch_size=128, epochs=2)
# x_test = x_test.reshape((-1,) + input_shape)
# model.evaluate(x_test/255, y_test)
