import matplotlib.pyplot as plt

def confidence(predictions):
    upper = []
    lower =  []
    conf = 0.1
    for pred in predictions:
        upper.append(pred + conf)
        lower.append(pred - conf)
        conf += 0.05

    plt.plot(upper) 
    plt.plot(lower)
    plt.show()