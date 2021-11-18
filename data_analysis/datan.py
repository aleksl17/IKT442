import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import dates as mdates
from matplotlib.ticker import MaxNLocator
import datetime as dt
import os
import numpy
import time

x = []
y = []
allX = []
allY = []
currentTime = str(int(time.time()))
dataDirectory = os.path.dirname(os.path.dirname(__file__)) + "\\data"
outputDirectory = os.path.join("./.output/" + currentTime)
os.mkdir(outputDirectory)

for filename in os.listdir(dataDirectory):
    df = pd.read_csv(dataDirectory + "\\" + filename)
    pyli = df.values.tolist()
    for date in pyli:
        x.append(dt.datetime.strptime(date[0], "%Y-%m-%dT%H:00:00.000+00:00"))
        y.append(date[1])
        allX.append(dt.datetime.strptime(date[0], "%Y-%m-%dT%H:00:00.000+00:00"))
        allY.append(date[1])
    # Single 
    plt.plot(x, y)
    plt.xlabel("Datetime")
    plt.ylabel("Milliamp")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(outputDirectory + "/" + filename, dpi=600)
    plt.clf()
    x.clear()
    y.clear()

# All
# plt.plot(allX, allY)
# plt.xlabel("Datetime")
# plt.ylabel("Milliamp")
# plt.xticks(rotation=30)
# plt.tight_layout()
# plt.savefig(outputDirectory + "/all")