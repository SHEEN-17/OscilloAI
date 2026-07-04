import numpy as np

from measure import waveform_to_array
from amplitude import amplitude
from rms import rms
from duty_cycle import duty_cycle
from frequency import estimate_frequency
from statistics import signal_statistics

waveform = []

for x in range(500):

    y = 100 + 50 * np.sin(x / 25)

    waveform.append((x, y))

signal = waveform_to_array(waveform)

print("=" * 50)

print("Amplitude :", amplitude(signal))

print("RMS :", rms(signal))

print("Duty :", duty_cycle(signal))

print("Frequency :", estimate_frequency(signal))

print("Statistics")

print(signal_statistics(signal))

print("=" * 50)