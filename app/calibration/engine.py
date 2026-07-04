from .converter import *


class CalibrationEngine:

    def __init__(self, waveform, image_shape):

        self.waveform = waveform

        self.height = image_shape[0]

        self.width = image_shape[1]

    def amplitude(self):

        if len(self.waveform) == 0:

            return 0.0

        ys = [p[1] for p in self.waveform]

        pixel = (max(ys) - min(ys)) / 2

        div = pixel_to_vertical_div(
            pixel,
            self.height
        )

        return div_to_voltage(div)

    def vpp(self):

        return self.amplitude() * 2

    def period(self):

        if len(self.waveform) < 2:

            return 0.0

        pixel = self.width

        div = pixel_to_horizontal_div(
            pixel,
            self.width
        )

        return div_to_time(div)

    def frequency(self):

        period = self.period()

        if period == 0:

            return 0.0

        return 1 / period