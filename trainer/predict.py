import os
import cv2
import numpy as np
import tensorflow as tf

# ===========================
# PATH
# ===========================

MODEL_PATH = os.path.join("..", "models", "oscilloAI.keras")
IMAGE_PATH = os.path.join("..", "test_images", "test.png")

# ===========================
# LOAD MODEL
# ===========================

print("Loading model...")

model = tf.keras.models.load_model(MODEL_PATH)

print("Model berhasil dimuat.")

# ===========================
# LOAD IMAGE
# ===========================

image = cv2.imread(IMAGE_PATH)

if image is None:
    raise FileNotFoundError(f"Tidak menemukan gambar: {IMAGE_PATH}")

image = cv2.resize(image, (224, 224))
image = image.astype(np.float32) / 255.0
image = np.expand_dims(image, axis=0)

# ===========================
# PREDICT
# ===========================

prediction = model.predict(image, verbose=0)

classes = [
    "pwm",
    "sawtooth",
    "sinus",
    "square",
    "triangle"
]

index = np.argmax(prediction)

confidence = prediction[0][index] * 100

print("\n========== HASIL ==========")
print(f"Jenis Gelombang : {classes[index]}")
print(f"Confidence      : {confidence:.2f}%")