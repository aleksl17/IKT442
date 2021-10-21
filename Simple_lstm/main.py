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

#     # split a univariate sequence into samples
# def split_sequence(sequence, n_steps):
# 	X, y = list(), list()
# 	for i in range(len(sequence)):
# 		# find the end of this pattern
# 		end_ix = i + n_steps
# 		# check if we are beyond the sequence
# 		if end_ix > len(sequence)-1:
# 			break
# 		# gather input and output parts of the pattern
# 		seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
# 		X.append(seq_x)
# 		y.append(seq_y)
# 	return array(X)#, array(y)
 
# # choose a number of time steps
# # split into samples
# X = split_sequence(dataX, n_steps)
# # summarize the data
# y = split_sequence(dataY, n_outputs)

# X = X[:len(y)]
 
# X = X.reshape((X.shape[0], X.shape[1], n_features))

# print(X)

# X, y = ingest()
# X = X.reshape((X.shape[0], X.shape[1], n_features))

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