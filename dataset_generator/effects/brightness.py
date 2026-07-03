import cv2
import random

def apply_brightness(image):

    alpha = random.uniform(
        0.8,
        1.2
    )

    beta = random.randint(
        -20,
        20
    )

    result = cv2.convertScaleAbs(
        image,
        alpha=alpha,
        beta=beta
    )

    return result