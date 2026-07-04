import os

from app.image_processing.pipeline import process

from app.signal_analysis.measure import waveform_to_array
from app.signal_analysis.amplitude import amplitude
from app.signal_analysis.rms import rms
from app.signal_analysis.frequency import estimate_frequency
from app.signal_analysis.duty_cycle import duty_cycle
from app.signal_analysis.statistics import signal_statistics


class OscilloEngine:

    def analyze(self, image_path):

        (
            image,
            edges,
            detected,
            warped,
            waveform_image,
            waveform,
            processed
        ) = process(image_path)

        signal = waveform_to_array(waveform)

        result = {

            "waveform_points": len(waveform),

            "amplitude": amplitude(signal),

            "rms": rms(signal),

            "frequency": estimate_frequency(signal),

            "duty_cycle": duty_cycle(signal),

            "statistics": signal_statistics(signal)

        }

        return result