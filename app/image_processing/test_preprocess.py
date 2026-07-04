import os
import cv2

from .preprocess import preprocess_image
from .detect_screen import detect_screen


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_ROOT = os.path.abspath(
    os.path.join(CURRENT_DIR, "..", "..")
)

IMAGE_PATH = os.path.join(
    PROJECT_ROOT,
    "test_images",
    "test.png"
)

processed = preprocess_image(IMAGE_PATH)

edges = detect_screen(
    cv2.imread(IMAGE_PATH)
)

print("=" * 50)
print("Preprocess Test Success")
print("=" * 50)
print(processed.shape)
print(edges.shape)
print("=" * 50)