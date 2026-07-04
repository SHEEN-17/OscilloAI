import numpy as np


def trace_waveform(binary):

    height, width = binary.shape

    waveform = []

    for x in range(width):

        ys = np.where(binary[:, x] == 255)[0]

        if len(ys):

            y = int(np.mean(ys))

            waveform.append((x, y))

    return waveform