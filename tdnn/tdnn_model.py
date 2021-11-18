from keras.models import Sequential
from TDNN_layer import TDNNLayer
import numpy as np

class TDNNModel:
    def __init__(self):
        self.model = None
        self.epochs = 5
        self.n_steps = 48
        self.n_outputs = 24
        self.trainX = []
        self.trainY = []
        self.evalX = []
        self.evalY = []

    def create_model(self, n_steps, n_outputs):
        self.n_steps = n_steps
        self.n_outputs = n_outputs
        self.model = Sequential()
        self.model.add(TDNNLayer([-2, 2], sub_sampling=False, input_shape=(n_steps, 1)))
        self.model.add(TDNNLayer([-1, 2], sub_sampling=True))
        self.model.add(TDNNLayer([-3, 2], sub_sampling=True))
        self.model.add(TDNNLayer([-7, 2], sub_sampling=True, activation="softmax"))
        self.model.compile(optimizer='Adam', loss="categorical_crossentropy", metrics=['accuracy'])
        self.model.summary()

    def train_model(self, trainX, trainY, epochs):
        self.trainX = trainX
        self.trainY = trainY
        self.epochs = epochs
        self.model(trainX, trainY, epochs=epochs)
        # data = np.random.random((3200, self.input_dim, 1))
        # truth = np.round(np.random.random((3200, self.input_dim - 21)))
        # self.model.fit(data, truth, epochs=20)

    def evaluate_model(self, evalX, evalY):
        self.evalX = evalX
        self.evalY = evalY
        return self.model.evaluate(evalX, evalY)
        # data = np.random.random((3200, self.input_dim, 1))
        # truth = np.round(np.random.random((3200, self.input_dim - 21)))
        # return self.model.evaluate(data, truth)
