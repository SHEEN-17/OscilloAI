import cv2
import random
import numpy as np


def random_brightness(image):

    alpha = random.uniform(0.8, 1.2)

    beta = random.randint(-20, 20)

    return cv2.convertScaleAbs(
        image,
        alpha=alpha,
        beta=beta
    )


def random_blur(image):

    if random.random() < 0.5:

        image = cv2.GaussianBlur(
            image,
            (3,3),
            0
        )

    return image


def random_noise(image):

    noise = np.random.normal(
        0,
        8,
        image.shape
    )

    image = image + noise

    image = np.clip(
        image,
        0,
        255
    )

    return image.astype(np.uint8)