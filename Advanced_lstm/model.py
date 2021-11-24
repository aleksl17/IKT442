#tensorflow
from keras import models
from keras.backend import dropout
from keras.models import Sequential, Model
from keras.layers import LSTM, Dense, Dropout, Flatten, Concatenate

def inputLstm(n_steps = 48):
    model = Sequential()
    model.add(LSTM(n_steps, activation='relu', input_shape=(n_steps, 1)))
    model.add(Dense(24, activation="sigmoid"))

    return model


def getModel(n_steps=48,n_outputs=24):
    input1 = inputLstm()
    input2 = inputLstm()
    output = Concatenate()([input1.output, input2.output])
    output = Dense(n_steps, activation="sigmoid")(output)
    output = Dropout(0.1)(output)
    output = Dense(n_outputs, activation="relu")(output)

    model = Model([input1.input,input2.input],output)
    model.compile(optimizer='adam', loss='mse')



    return model


    #add noise