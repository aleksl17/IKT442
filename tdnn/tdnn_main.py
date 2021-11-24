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
    predModel = model.create_model(n_steps, n_outputs)
    history = model.train_model(trainX, trainY, 200)
    plt.plot(history.history['loss'])
    plt.show()
    # model.evaluate_model(evalX, evalY)

    pred = predModel.predict(evalX)

    totalError = []
    conflist = [0]*n_outputs
    for i in range(len(evalY)):
        error = 0
        for y, yHat, j in zip(evalY[i], pred[i], range(n_outputs)):
            error += abs((y - yHat)/y)	
            conflist[j] = conflist[j] + abs((y - yHat)/y)/len(evalY)
        totalError.append(error/n_outputs)
        print(error/n_outputs)

    print("Training Completed")
    print(sum(totalError)/len(totalError)*100)
    print(pred[0])

    x = range(n_outputs)

    def confidence(predictions, conflist, y):
        upper = []
        lower =  []
        for pred, conf, theta in zip(predictions, conflist, range(n_outputs)):
            upper.append(pred + conf + conf*10*(theta/n_outputs))
            lower.append(pred - conf - conf*10*(theta/n_outputs))

        # plt.plot(lower, upper) 
        plt.fill_between(x, y1=lower,y2=upper)
        plt.plot(y, "r")
        plt.axis([0,n_outputs,5,10])
        plt.show()

    # confidence(pred[0], conflist, testingY[0])
    # confidence(pred[-1], conflist, testingY[-1])

    for i in range(len(pred)):
        confidence(pred[i], conflist, evalY[i])

if __name__ == "__main__":
    main()