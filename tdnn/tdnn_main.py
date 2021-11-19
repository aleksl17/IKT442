from dataScript import getData
from tdnn_model import TDNNModel
from numpy import load

def main():
    n_steps = 24
    # getData(topLen=n_steps,bottomLen=n_steps, topStation="Sloana")
    trainX = load('./tdnn/npybin/trainingX.npy')
    trainY = load('./tdnn/npybin/trainingY.npy')
    evalX = load('./tdnn/npybin/testingX.npy')
    evalY = load('./tdnn/npybin/testingY.npy')
    model = TDNNModel()
    model.create_model(n_steps)
    model.train_model(trainX, trainY, 100)
    model.evaluate_model(evalX, evalY)

if __name__ == "__main__":
    main()