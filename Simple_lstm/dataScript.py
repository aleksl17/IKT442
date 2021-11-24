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
    X, y = list(), list()
    tops = open("dataset/"+topStation+"_no_NaN").readlines()
    tops.pop(0)
    tops = tops[len(tops)-2000:]

    bottoms = open("dataset/"+bottomStation+"_no_NaN").readlines()
    bottoms.pop(0)

    tops = tops[len(tops)-2000:]
    bottoms = bottoms[len(bottoms)-2000:]

    top = split_sequence(tops, topLen)
    bottom = split_sequence(bottoms, bottomLen)

    for t in top:
        for b in bottom:
            if datetime.strptime(t[-1].split(":")[0],"%Y-%m-%dT%H") == datetime.strptime(b[0].split(":")[0],"%Y-%m-%dT%H"):
                #check if weird behavior and add muiltiple instances, augmentation?
                topMeasurements = removeDateTime(t)
                bottomMeasurements = removeDateTime(b)
                if max(bottomMeasurements) - min(bottomMeasurements) > 0.5:
                    print("Larger")
                    X.append(topMeasurements)
                    y.append(bottomMeasurements)
                    X.append(augment(topMeasurements))
                    y.append(bottomMeasurements)
                    X.append(augment(topMeasurements))
                    y.append(augment(bottomMeasurements))
                    X.append(topMeasurements)
                    y.append(bottomMeasurements)
                    X.append(augment(topMeasurements))
                    y.append(bottomMeasurements)
                    X.append(augment(topMeasurements))
                    y.append(augment(bottomMeasurements))
                    X.append(topMeasurements)
                    y.append(bottomMeasurements)
                    X.append(augment(topMeasurements))
                    y.append(bottomMeasurements)
                    X.append(augment(topMeasurements))
                    y.append(augment(bottomMeasurements))
                    X.append(topMeasurements)
                    y.append(bottomMeasurements)
                    X.append(augment(topMeasurements))
                    y.append(bottomMeasurements)
                    X.append(augment(topMeasurements))
                    y.append(augment(bottomMeasurements))
                    X.append(topMeasurements)
                    y.append(bottomMeasurements)
                    X.append(augment(topMeasurements))
                    y.append(bottomMeasurements)
                    X.append(augment(topMeasurements))
                    y.append(augment(bottomMeasurements))
                    X.append(topMeasurements)
                    y.append(bottomMeasurements)
                    X.append(augment(topMeasurements))
                    y.append(bottomMeasurements)
                    X.append(augment(topMeasurements))
                    y.append(augment(bottomMeasurements))
                    X.append(topMeasurements)
                    y.append(bottomMeasurements)
                    X.append(augment(topMeasurements))
                    y.append(bottomMeasurements)
                    X.append(augment(topMeasurements))
                    y.append(augment(bottomMeasurements))
                    X.append(topMeasurements)
                    y.append(bottomMeasurements)
                    X.append(augment(topMeasurements))
                    y.append(bottomMeasurements)
                    X.append(augment(topMeasurements))
                    y.append(augment(bottomMeasurements))
                    X.append(topMeasurements)
                    y.append(bottomMeasurements)
                    X.append(augment(topMeasurements))
                    y.append(bottomMeasurements)
                    X.append(augment(topMeasurements))
                    y.append(augment(bottomMeasurements))
                    X.append(topMeasurements)
                    y.append(bottomMeasurements)
                    X.append(augment(topMeasurements))
                    y.append(bottomMeasurements)
                    X.append(augment(topMeasurements))
                    y.append(augment(bottomMeasurements))
                    X.append(topMeasurements)
                    y.append(bottomMeasurements)
                    X.append(augment(topMeasurements))
                    y.append(bottomMeasurements)
                    X.append(augment(topMeasurements))
                    y.append(augment(bottomMeasurements))
                    X.append(topMeasurements)
                    y.append(bottomMeasurements)
                    X.append(augment(topMeasurements))
                    y.append(bottomMeasurements)
                    X.append(augment(topMeasurements))
                    y.append(augment(bottomMeasurements))
                if max(bottomMeasurements) - min(bottomMeasurements) > 0.3:
                    X.append(topMeasurements)
                    y.append(bottomMeasurements)
                    X.append(topMeasurements)
                    y.append(bottomMeasurements)
                X.append(topMeasurements)
                y.append(bottomMeasurements)
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

    return array(trainingX), array(trainingY), array(testingX), array(testingY)