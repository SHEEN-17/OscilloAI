import numpy as np


def signal_statistics(signal):

    if len(signal) == 0:

        return {}

    return {

        "min": float(np.min(signal)),

        "max": float(np.max(signal)),

        "mean": float(np.mean(signal)),

        "std": float(np.std(signal))

    }