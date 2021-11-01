#tensorflow
from keras.backend import dropout
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout

def getModel(n_steps=48,n_outputs=24):
    model = Sequential()
    model.add(LSTM(n_steps, activation='relu', input_shape=(n_steps, 1)))
    model.add(Dense(n_outputs))
    model.add(Dropout(0.1))
    model.add(Dense(n_outputs))
    model.compile(optimizer='adam', loss='mse')
    return model


    #add noise