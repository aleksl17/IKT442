#packages
from keras import models
from keras.engine.data_adapter import pack_x_y_sample_weight
from model import getModel
from numpy import array
import matplotlib.pyplot as plt
import random
# from confidence import confidence

#scripts
# from dataingest import ingest
from dataScript import getData

#params
n_features = 1
n_steps = 48
n_outputs = 24
epochs = 100
t_split = 0.9

trainingX, trainingY, testingX, testingY = getData(topLen=n_steps,bottomLen=n_outputs, topStation="Sløåna")
trainingX = trainingX.reshape((trainingX.shape[0], trainingX.shape[1], n_features))
testingX = testingX.reshape((testingX.shape[0], testingX.shape[1], n_features))

model = getModel()

history = model.fit(trainingX, trainingY, epochs=epochs, verbose=1, shuffle=True)

plt.plot(history.history['loss'])
plt.show()

pred = model.predict(testingX)

totalError = []
conflist = [0]*n_outputs
for i in range(len(testingY)):
	error = 0
	for y, yHat, j in zip(testingY[i], pred[i], range(n_outputs)):
		error += abs((y - yHat)/y)	
		conflist[j] = conflist[j] + abs((y - yHat)/y)/len(testingY)
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
    confidence(pred[i], conflist, testingY[i])