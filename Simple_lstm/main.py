#packages
from keras import models
from model import getModel
from numpy import array
import matplotlib.pyplot as plt
import random

#scripts
# from dataingest import ingest
from dataScript import getData

#params
n_features = 1
n_steps = 48
n_outputs = 24
epochs = 100
t_split = 0.8

trainingX, trainingY, testingX, testingY = getData(topLen=n_steps,bottomLen=n_outputs)
trainingX = trainingX.reshape((trainingX.shape[0], trainingX.shape[1], n_features))
testingX = testingX.reshape((testingX.shape[0], testingX.shape[1], n_features))

model = getModel()

history = model.fit(trainingX, trainingY, epochs=epochs, verbose=1)

plt.plot(history.history['loss'])
plt.show()

pred = model.predict(testingX)

totalError = []
for i in range(len(testingY)):
	error = 0
	for y, yHat in zip(testingY[i], pred[i]):
		error += abs((y - yHat)/y)
	
	totalError.append(error/24)
	print(error/n_outputs)

print("Training Completed")
print(sum(totalError)/len(totalError)*100)