from dataScript import getData
from tdnn_model import TDNNModel


def main():
    n_steps = 48
    n_outputs = 24
    trainX, trainY, evalX, evalY = getData(topLen=n_steps,bottomLen=n_outputs, topStation="Sloana")
    print("getData done!")
    model = TDNNModel
    model.create_model(n_steps, n_outputs)
    print("Create model done!")
    model.train_model(trainX, trainY, 2)
    print("Train model done!")
    model.evaluate_model(evalX, evalY)
    print("All done!")

if __name__ == "__main__":
    main()