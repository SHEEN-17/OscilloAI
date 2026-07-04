import numpy as np


def rms(signal):

    if len(signal) == 0:

        return 0

    centered = signal - np.mean(signal)

    return float(

        np.sqrt(

            np.mean(

                centered ** 2

            )

        )

    )