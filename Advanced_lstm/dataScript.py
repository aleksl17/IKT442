from random import random
from typing import Sequence
from numpy import array
from datetime import datetime
from sklearn.linear_model import LinearRegression
from augment import augment

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

def getData(topLen=48, bottomLen=24, topStation="Netlandsnes", bottomStation="faret", t_split=0.8):
    print("Loading data from "+topStation+" to "+bottomStation)
    topX, bottomX, y = list(), list(), list()
    tops = open("dataset/"+topStation+"_no_NaN").readlines()
    tops.pop(0)
    tops = tops[len(tops)-2000:]

    bottoms = open("dataset/"+bottomStation+"_no_NaN").readlines()
    bottoms.pop(0)

    # tops = tops[len(tops)-2000:]
    # bottoms = bottoms[len(bottoms)-2000:]

    top = split_sequence(tops, topLen)
    bottom = split_sequence(bottoms, topLen + bottomLen)

    for t in top:
        for b in bottom:
            if datetime.strptime(t[0].split(":")[0],"%Y-%m-%dT%H") == datetime.strptime(b[0].split(":")[0],"%Y-%m-%dT%H"):
                #check if weird behavior and add muiltiple instances, augmentation?
                topMeasurements = removeDateTime(t)
                bottomMeasurements = removeDateTime(b)
                if max(bottomMeasurements) - min(bottomMeasurements) > 0.5:
                    topX.append(augment(topMeasurements))
                    bottomX.append(bottomMeasurements[:topLen])
                    y.append(bottomMeasurements[topLen:])
                    topX.append(topMeasurements)
                    bottomX.append(augment(bottomMeasurements[:topLen]))
                    y.append(bottomMeasurements[topLen:])
                    topX.append(augment(topMeasurements))
                    bottomX.append(augment(bottomMeasurements[:topLen]))
                    y.append(bottomMeasurements[topLen:])
                    topX.append(augment(topMeasurements))
                    bottomX.append(augment(bottomMeasurements[:topLen]))
                    y.append(augment(bottomMeasurements[topLen:]))
                    topX.append(augment(topMeasurements))
                    bottomX.append(augment(bottomMeasurements[:topLen]))
                    y.append(bottomMeasurements[topLen:])
                    topX.append(augment(topMeasurements))
                    bottomX.append(augment(bottomMeasurements[:topLen]))
                    y.append(augment(bottomMeasurements[topLen:]))
                    topX.append(augment(topMeasurements))
                    bottomX.append(augment(bottomMeasurements[:topLen]))
                    y.append(bottomMeasurements[topLen:])
                    topX.append(augment(topMeasurements))
                    bottomX.append(augment(bottomMeasurements[:topLen]))
                    y.append(augment(bottomMeasurements[topLen:]))
                    topX.append(augment(topMeasurements))
                    bottomX.append(bottomMeasurements[:topLen])
                    y.append(bottomMeasurements[topLen:])
                    topX.append(topMeasurements)
                    bottomX.append(augment(bottomMeasurements[:topLen]))
                    y.append(bottomMeasurements[topLen:])
                    topX.append(augment(topMeasurements))
                    bottomX.append(augment(bottomMeasurements[:topLen]))
                    y.append(bottomMeasurements[topLen:])
                    topX.append(augment(topMeasurements))
                    bottomX.append(augment(bottomMeasurements[:topLen]))
                    y.append(augment(bottomMeasurements[topLen:]))
                    topX.append(augment(topMeasurements))
                    bottomX.append(augment(bottomMeasurements[:topLen]))
                    y.append(bottomMeasurements[topLen:])
                    topX.append(augment(topMeasurements))
                    bottomX.append(augment(bottomMeasurements[:topLen]))
                    y.append(augment(bottomMeasurements[topLen:]))
                    topX.append(augment(topMeasurements))
                    bottomX.append(augment(bottomMeasurements[:topLen]))
                    y.append(bottomMeasurements[topLen:])
                    topX.append(augment(topMeasurements))
                    bottomX.append(augment(bottomMeasurements[:topLen]))
                    y.append(augment(bottomMeasurements[topLen:]))

                topX.append(topMeasurements)
                bottomX.append(bottomMeasurements[:topLen])
                y.append(bottomMeasurements[topLen:])
                
        if len(y)%100 == 0:
            print("Loaded data: " + str(len(y)))
    
    print("Loading completed")
    print("making training and testing")
    trainingXtop = list()
    trainingXbottom = list()
    trainingY = list()
    testingXtop = list()
    testingXbottom = list()
    testingY = list()
    for x1, x2, b in zip(topX, bottomX, y):
        if random() > t_split:
            testingXtop.append(x1)
            testingXbottom.append(x2)
            testingY.append(b)
        else:
            trainingXtop.append(x1)
            trainingXbottom.append(x2)
            trainingY.append(b)

    return array(trainingXtop), array(trainingXbottom), array(trainingY), array(testingXtop), array(testingXbottom), array(testingY)