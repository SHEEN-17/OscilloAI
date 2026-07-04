import numpy as np


def duty_cycle(signal):

    if len(signal) == 0:

        return 0

    mean = np.mean(signal)

    high = np.sum(signal > mean)

    return float(

        high / len(signal) * 100

    )