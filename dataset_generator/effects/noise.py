import cv2
import numpy as np

def apply_noise(image):

    noise = np.random.normal(
        0,
        15,
        image.shape
    ).astype(np.uint8)

    noisy = cv2.add(
        image,
        noise
    )

    return noisy