import pandas as pd
import numpy
import os

# TODO:
# Les data fra fil(er)
# Sorter data så alle tidspunkt liner opp
# Når to stasjoner etterspørres, sorter slik at data liner opp. Om range ikke er oppgitt, sorter fra begynnelsen av minste datasett til slutt av minste datasett.
# 
# GOAL:
# x[i] med data fra siste 48h(var) fra gitt stasjon(var)
# y[i] med data fra 24h(var) fra gitt stasjon(var)
# Fjern timestamps siden alle målinger er visst tid (må sorteres)
# x bør kunne gies i "fra-til" format
# TODO:
# Drit i multi-stations support
# x er xTime(48) timer fra topstation, y er de sekvensielle neste yTime(24) fra endstation.


def ingest(startStations, endStations, startDate, endDate, xTime=48, yTime=24, dataDirectory='data'):
    x= 0
    y = 0
    dataDictionary = {}
    tmpStartDates = []
    tmpEndDates = []
    startStationsSequences = []
    endStationsSequences = []
    # Makes sure that the stations variables are a list, even if single element is fed.
    if type(startStations) is not list: startStations = [ startStations ]
    if type(endStations) is not list: endStations = [ endStations ]

    # Read data
    for filename in os.listdir(dataDirectory):
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

    print(startDate)
    print(endDate)

    # Sequence
    for startStation in startStations:
        startRangeStart = int(dataDictionary[startStation][dataDictionary[startStation]['time']==startDate].index.to_numpy())
        startRangeEnd = int(dataDictionary[startStation][dataDictionary[startStation]['time']==endDate].index.to_numpy())+1
        print(startRangeStart)
        print(startRangeEnd)
        startStationsSequences.append(dataDictionary[startStation][startRangeStart:startRangeEnd])
    for endStation in endStations:
        endRangeStart = int(dataDictionary[endStation][dataDictionary[endStation]['time']==startDate].index.to_numpy())
        endRangeEnd = int(dataDictionary[endStation][dataDictionary[endStation]['time']==endDate].index.to_numpy())+1
        print(endRangeStart)
        print(endRangeEnd)
        endStationsSequences.append(dataDictionary[endStation][endRangeStart:endRangeEnd])

    print(startStationsSequences)
    print(endStationsSequences)

    return x, y


def split_sequence(sequence, n_steps):
    x, y = list(), list()
    for i in range(len(sequence)):
        end_i = i + n_steps
        if end_i > len(sequence) - 1:
            break
        seq_x, seq_y = sequence[i:end_i], sequence[end_i]
        x.append(seq_x)
        y.append(seq_y)
    return array(x), array(y)

# print(ingest('Netlandsnes_no_NaN', 'Åmot_Bru_no_NaN', '2021-05-25T14:00:00.000+00:00', '2021-05-25T22:00:00.000+00:00'))
print(ingest('Netlandsnes_no_NaN', 'Åmot_Bru_no_NaN', '2021-05-25T00:00:00.000+00:00', '2021-09-29T08:00:00.000+00:00'))



# Get index fucked
# startStations.index(stations)

# def getData(dataDirectory):
#     dataDictionary = {}
#     for filename in os.listdir(dataDirectory):
#         dataDictionary[filename] = pd.read_csv(os.path.join(dataDirectory, filename))
#     return dataDictionary

# def sortData(dataDictionary, startStations, endStations, startDate, endDate):
#     if startDate < dataDictionary['']
#     sortedData = []

#     return sortedData

# dataDictionary['Stakkeland_no_NaN'].loc[101].to_numpy()[1]