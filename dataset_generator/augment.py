import cv2
import numpy as np

def add_noise(image):

    noise = np.random.normal(
        0,
        8,
        image.shape
    ).astype(np.uint8)

    return cv2.add(image, noise)


def blur(image):

    return cv2.GaussianBlur(
        image,
        (3,3),
        0
    )


def brightness(image):

    alpha = np.random.uniform(
        0.8,
        1.2
    )

    beta = np.random.randint(
        -15,
        15
    )

    return cv2.convertScaleAbs(
        image,
        alpha=alpha,
        beta=beta
    )