import numpy as np


def waveform_to_array(waveform):

    if len(waveform) == 0:

        return np.array([])

    y = [point[1] for point in waveform]

    return np.array(y, dtype=np.float32)