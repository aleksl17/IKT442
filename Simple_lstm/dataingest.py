import pandas as pd
from numpy import array
import os

# TODO:
# Add more tests. Easy to break with wrong parameters.

def ingest(startStations, endStations, startDate, endDate, xTime=48, yTime=24, dataDirectory='data'):
    x= []
    y = []
    dataDictionary = {}
    tmpStartDates = []
    tmpEndDates = []
    startStationsSequences = []
    endStationsSequences = []
    # Makes sure that the stations variables are a list, even if single element is fed.
    if type(startStations) is not list: startStations = [ startStations ]
    if type(endStations) is not list: endStations = [ endStations ]

    # Read data
    for filename in os.listdir(os.path.dirname(os.path.dirname(__file__)) + "\\" + dataDirectory):
        dataDictionary[filename] = pd.read_csv(os.path.join(dataDirectory, filename))

    # Sort data
    for startStation in startStations:
        if startDate < dataDictionary[startStation].loc[0].to_numpy()[0]:
            tmpStartDates.append(dataDictionary[startStation].loc[0].to_numpy()[0])
        if endDate > dataDictionary[startStation].iloc[-1].to_numpy()[0]:
            tmpEndDates.append(dataDictionary[startStation].iloc[-1].to_numpy()[0])
    for endStation in endStations:
        if startDate < dataDictionary[endStation].loc[0].to_numpy()[0]:
            tmpStartDates.append(dataDictionary[endStation].loc[0].to_numpy()[0])
        if endDate > dataDictionary[endStation].iloc[-1].to_numpy()[0]:
            tmpEndDates.append(dataDictionary[endStation].iloc[-1].to_numpy()[0]) 
    if tmpStartDates:
        startDate = min(tmpStartDates)
        print('Invalid startDate given. New startDate set to: ', startDate)
    if tmpEndDates:
        endDate = max(tmpEndDates)
        print('Invalid endDate given. New endDate set to: ', endDate)

    # Sequence
    for startStation in startStations:
        startRangeStart = int(dataDictionary[startStation][dataDictionary[startStation]['time']==startDate].index.to_numpy())
        startRangeEnd = int(dataDictionary[startStation][dataDictionary[startStation]['time']==endDate].index.to_numpy())+1
        startStationsSequences.append(dataDictionary[startStation][startRangeStart:startRangeEnd])
    for endStation in endStations:
        endRangeStart = int(dataDictionary[endStation][dataDictionary[endStation]['time']==startDate].index.to_numpy())
        endRangeEnd = int(dataDictionary[endStation][dataDictionary[endStation]['time']==endDate].index.to_numpy())+1
        endStationsSequences.append(dataDictionary[endStation][endRangeStart:endRangeEnd])

    # Assign x and y
    for i in range(len(startStationsSequences[0])+len(endStationsSequences[0])):
        sssEnd_i = i + xTime
        essEnd_i = sssEnd_i + yTime
        # if sssEnd_i > len(startStationsSequences[0])+len(endStationsSequences[0]) - 1:
        #     break
        if (i % 24 == 0):
            seq_x = startStationsSequences[0]['milliamp'][i:sssEnd_i]
            seq_y = endStationsSequences[0]['milliamp'][sssEnd_i:essEnd_i]
            x.append(seq_x)
            y.append(seq_y)
    return array(x), array(y)

# Testing
print(ingest('Netlandsnes_no_NaN', 'Åmot_Bru_no_NaN', '2021-05-26T00:00:00.000+00:00', '2021-05-28T23:00:00.000+00:00'))
# print(ingest('Netlandsnes_no_NaN', 'Åmot_Bru_no_NaN', '2021-05-25T14:00:00.000+00:00', '2021-06-02T22:00:00.000+00:00'))
# print(ingest('Netlandsnes_no_NaN', 'Åmot_Bru_no_NaN', '2021-05-25T00:00:00.000+00:00', '2021-09-29T08:00:00.000+00:00'))
