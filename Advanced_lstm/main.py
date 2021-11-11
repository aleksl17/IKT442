#packages
from keras import models
from keras.engine import training
from keras.engine.data_adapter import pack_x_y_sample_weight
from model import getModel
from numpy import array
import matplotlib.pyplot as plt
# from confidence import confidence

#scripts
# from dataingest import ingest
from dataScript import getData

#params
n_features = 1
n_steps = 48
n_outputs = 24
epochs = 500
t_split = 0.9

trainingXtop, trainingXbottom, trainingY, testingXtop, testingXbottom, testingY = getData(topLen=n_steps,bottomLen=n_outputs)
trainingXtop = trainingXtop.reshape((trainingXtop.shape[0], trainingXtop.shape[1], n_features))
testingXtop = testingXtop.reshape((testingXtop.shape[0], testingXtop.shape[1], n_features))
trainingXbottom = trainingXbottom.reshape((trainingXbottom.shape[0], trainingXbottom.shape[1], n_features))
testingXbottom = testingXbottom.reshape((testingXbottom.shape[0], testingXbottom.shape[1], n_features))

print(testingXtop)


model = getModel()

history = model.fit([trainingXtop,trainingXbottom], trainingY, epochs=epochs, verbose=1, shuffle=True)

plt.plot(history.history['loss'])
plt.show()

pred = model.predict([testingXtop,testingXbottom])

print("PREDSSSSS")
print(pred)

totalError = []
conflist = [0]*n_outputs
for i in range(len(testingY)):
	error = 0
	for y, yHat, j in zip(testingY[i], pred[i], range(n_outputs)):
		error += abs((y - yHat)/y)	
		conflist[j] = conflist[j] + abs((y - yHat)/y)/len(testingY)
	totalError.append(error/n_outputs)

print("Training Completed")
print(sum(totalError)/len(totalError)*100)

x = range(n_outputs)

def confidence(predictions, conflist, y):
    upper = []
    lower =  []
    for p, conf, theta in zip(predictions, conflist, range(n_outputs)):
        upper.append(p + 0.05 + conf*10*(theta/n_outputs))
        lower.append(p - 0.05 - conf*10*(theta/n_outputs))

    # plt.plot(lower, upper) 
    plt.fill_between(x, y1=lower,y2=upper)
    plt.plot(y, "r")
    plt.axis([0,n_outputs,5,10])
    plt.show()

# confidence(pred[0], conflist, testingY[0])
# confidence(pred[-1], conflist, testingY[-1])

for i in range(len(pred)):
    print(pred[i*10])
    confidence(pred[i*10], conflist, testingY[i*10])