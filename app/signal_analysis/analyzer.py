import numpy as np

from .measure import waveform_to_array
from .frequency import estimate_frequency
from .amplitude import amplitude
from .rms import rms
from .duty_cycle import duty_cycle
from .statistics import signal_statistics


def analyze_signal(waveform):

    signal = waveform_to_array(waveform)

    if len(signal) == 0:

        return {

            "points": 0,

            "frequency": 0,

            "amplitude": 0,

            "vrms": 0,

            "duty_cycle": 0,

            "statistics": {}

        }

    return {

        "points": len(signal),

        "frequency": estimate_frequency(signal),

        "amplitude": amplitude(signal),

        "vrms": rms(signal),

        "duty_cycle": duty_cycle(signal),

        "statistics": signal_statistics(signal)

    }