import os
import random
import cv2
import matplotlib.pyplot as plt

from waveform import (
    generate_sine,
    generate_square,
    generate_triangle,
    generate_sawtooth,
    generate_pwm
)

from oscilloscope import create_scope
from augment import add_noise, brightness, blur
from metadata import create_metadata, append_metadata
from config import *

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATASET_DIR = os.path.join(
    BASE_DIR,
    "dataset"
)

metadata_path = create_metadata()

waveforms = {

    "sinus": generate_sine,

    "square": generate_square,

    "triangle": generate_triangle,

    "sawtooth": generate_sawtooth,

    "pwm": generate_pwm

}

for waveform_name, generator in waveforms.items():

    folder = os.path.join(
        DATASET_DIR,
        waveform_name
    )

    os.makedirs(
        folder,
        exist_ok=True
    )

    print(f"\nGenerating {waveform_name}...")

    for i in range(IMAGE_PER_CLASS):

        frequency = random.randint(
            FREQUENCY_MIN,
            FREQUENCY_MAX
        )

        amplitude = random.randint(
            AMPLITUDE_MIN,
            AMPLITUDE_MAX
        )

        if waveform_name == "pwm":

            duty = random.uniform(
                PWM_MIN,
                PWM_MAX
            )

            t, y = generator(
                frequency,
                amplitude,
                DURATION,
                SAMPLE_RATE,
                duty
            )

        else:

            t, y = generator(
                frequency,
                amplitude,
                DURATION,
                SAMPLE_RATE
            )

        fig, ax = create_scope()

        ax.plot(
            t,
            y,
            color="#00FF66",
            linewidth=2
        )

        filename = os.path.join(
            folder,
            f"{waveform_name}_{i+1:04d}.png"
        )

        plt.savefig(
            filename,
            dpi=150,
            bbox_inches="tight"
        )

        plt.close(fig)

        image = cv2.imread(filename)

        image = add_noise(image)
        image = brightness(image)
        image = blur(image)

        cv2.imwrite(
            filename,
            image
        )

        append_metadata(
            metadata_path,
            os.path.basename(filename),
            waveform_name,
            frequency,
            amplitude
        )

print("\n=======================================")
print("Dataset berhasil dibuat!")
print("=======================================")