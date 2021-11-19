from random import random
from typing import Sequence
from numpy import array
from numpy import save
from datetime import datetime
import numpy

def split_sequence(data, n_steps):
    X = list()
    for i in range(len(data) - n_steps):
        X.append(data[:i + n_steps][i:])

    return X

def removeDateTime(data):
    X = []
    for d in data:
        measurement = d.split(",")[1]
        measurement = float(measurement)
        X.append(measurement)

    return X

def getData(topLen=24, bottomLen=24, topStation="Netlandsnes", bottomStation="Faret", t_split=0.5):
    print("Loading data from "+topStation+" to "+bottomStation)
    X, y = list(), list()
    tops = open("./data/"+topStation).readlines()
    tops.pop(0)
    tops = tops[len(tops)-2000:]

    bottoms = open("./data/"+bottomStation).readlines()
    bottoms.pop(0)

    # tops = tops[len(tops)-2000:]
    # bottoms = bottoms[len(bottoms)-2000:]

    top = split_sequence(tops, topLen)
    bottom = split_sequence(bottoms, bottomLen)

    for t in top:
        for b in bottom:
            if datetime.strptime(t[-1].split(":")[0],"%Y-%m-%dT%H") == datetime.strptime(b[0].split(":")[0],"%Y-%m-%dT%H"):
                #check if weird behavior and add muiltiple instances, augmentation?
                X.append(removeDateTime(t))
                y.append(removeDateTime(b))
        if len(y)%100 == 0:
            print("Loaded data: " + str(len(y)))
    
    print("Loading completed")
    print("making training and testing")
    trainingX = list()
    trainingY = list()
    testingX = list()
    testingY = list()
    for a, b in zip(X,y):
        if random() > t_split:
            testingX.append(a)
            testingY.append(b)
        else:
            trainingX.append(a)
            trainingY.append(b)

    array(trainingX)
    array(trainingY)
    array(testingX)
    array(testingY)

    trainingX = trainingX[:900]
    trainingY = trainingY[:900]
    testingX = testingX[:900]
    testingY = testingY[:900]

    # trainingX = trainingX.reshape((trainingX.shape[0], trainingX.shape[1], 1))
    # testingX = testingX.reshape((testingX.shape[0], testingX.shape[1], 1))

    # Save Xs and Ys as numpy binary files.
    save('trainingX.npy', trainingX)
    save('trainingY.npy', trainingY)
    save('testingX.npy', testingX)
    save('testingY.npy', testingY)

    return trainingX, trainingY, testingX, testingY