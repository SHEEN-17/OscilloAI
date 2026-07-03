import os
import cv2
import numpy as np
import tensorflow as tf

print("="*50)
print("OSCILLO AI PREDICTION TEST")
print("="*50)

MODEL_PATH = "../models/oscilloAI.keras"
IMAGE_PATH = "../test_images/test.png"

classes = [
    "pwm",
    "sawtooth",
    "sinus",
    "square",
    "triangle"
]

# ======================
# LOAD MODEL
# ======================

print("Loading model...")

model = tf.keras.models.load_model(MODEL_PATH)

print("Model loaded.")

# ======================
# LOAD IMAGE
# ======================

image = cv2.imread(IMAGE_PATH)

if image is None:

    raise FileNotFoundError(
        IMAGE_PATH
    )

image = cv2.resize(
    image,
    (224,224)
)

image = image.astype(np.float32)

image /= 255.0

image = np.expand_dims(
    image,
    axis=0
)

# ======================
# PREDICTION
# ======================

prediction = model.predict(
    image,
    verbose=0
)

index = np.argmax(
    prediction
)

confidence = prediction[0][index] * 100

print()

print("Prediction :")

print(classes[index])

print()

print(f"Confidence : {confidence:.2f}%")