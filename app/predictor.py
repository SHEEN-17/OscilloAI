import os
import cv2
import numpy as np
import tensorflow as tf

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "models",
    "oscilloAI.keras"
)

model = tf.keras.models.load_model(MODEL_PATH)

classes = [
    "pwm",
    "sawtooth",
    "sinus",
    "square",
    "triangle"
]


def predict_image(image_path):

    image = cv2.imread(image_path)

    image = cv2.resize(image,(224,224))

    image = image.astype(np.float32)

    image /= 255.0

    image = np.expand_dims(image, axis=0)

    prediction = model.predict(
        image,
        verbose=0
    )[0]

    index = np.argmax(prediction)

    return (
        classes[index],
        prediction[index] * 100,
        prediction
    )