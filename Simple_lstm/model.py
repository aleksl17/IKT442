#tensorflow
from keras.models import Sequential
from keras.layers import LSTM, Dense

def getModel(n_steps=48,n_outputs=24):
    model = Sequential()
    model.add(LSTM(n_steps, activation='relu', input_shape=(n_steps, 1)))
    model.add(Dense(n_outputs))
    model.compile(optimizer='adam', loss='mse')
    return model