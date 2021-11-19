from dataScript import getData
from tdnn_model import TDNNModel
import matplotlib.pyplot as plt
from numpy import load

def main():
    n_steps = 48
    n_outputs = 24
    # getData()
    trainX = load('./tdnn/npybin/trainingX.npy')
    trainY = load('./tdnn/npybin/trainingY.npy')
    evalX = load('./tdnn/npybin/testingX.npy')
    evalY = load('./tdnn/npybin/testingY.npy')
    # trainX = trainX.reshape((trainX.shape[0], trainX.shape[1], 1))
    # evalX = evalX.reshape((evalX.shape[0], evalX.shape[1], 1))
    model = TDNNModel()
    model.create_model(n_steps, n_outputs)
    history = model.train_model(trainX, trainY, 100)
    plt.plot(history.history['loss'])
    plt.show()
    model.evaluate_model(evalX, evalY)

if __name__ == "__main__":
    main()