import numpy as np


def amplitude(signal):

    if len(signal) == 0:

        return 0

    return float(

        (np.max(signal) - np.min(signal))

        / 2

    )