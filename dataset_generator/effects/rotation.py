import cv2
import random

def apply_rotation(image):

    angle = random.uniform(
        -5,
        5
    )

    h, w = image.shape[:2]

    M = cv2.getRotationMatrix2D(
        (w//2, h//2),
        angle,
        1
    )

    rotated = cv2.warpAffine(
        image,
        M,
        (w,h)
    )

    return rotated