import cv2
import numpy as np


TARGET_SIZE = (224, 224)


def preprocess_image(image_path):

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Image cannot be loaded.")

    image = cv2.resize(image, TARGET_SIZE)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    image = image.astype(np.float32)

    image /= 255.0

    return image