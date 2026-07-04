import cv2
import numpy as np


def extract_waveform(image):

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    blur = cv2.GaussianBlur(
        gray,
        (5, 5),
        0
    )

    _, thresh = cv2.threshold(

        blur,

        180,

        255,

        cv2.THRESH_BINARY

    )

    return thresh