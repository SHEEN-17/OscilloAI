import numpy as np


def estimate_frequency(signal):

    if len(signal) < 2:

        return 0

    centered = signal - np.mean(signal)

    crossings = []

    for i in range(1, len(centered)):

        if centered[i - 1] < 0 <= centered[i]:

            crossings.append(i)

    if len(crossings) < 2:

        return 0

    periods = np.diff(crossings)

    return float(

        np.mean(periods)

    )