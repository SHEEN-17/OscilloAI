import cv2

def apply_blur(image):

    blurred = cv2.GaussianBlur(
        image,
        (5,5),
        0
    )

    return blurred