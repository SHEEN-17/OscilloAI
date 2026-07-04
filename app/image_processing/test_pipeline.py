import os

from .pipeline import process


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_ROOT = os.path.abspath(
    os.path.join(CURRENT_DIR, "..", "..")
)

IMAGE_PATH = os.path.join(
    PROJECT_ROOT,
    "test_images",
    "test.png"
)

(
    image,
    edges,
    detected,
    warped,
    waveform_image,
    waveform,
    processed
) = process(IMAGE_PATH)

print("=" * 50)
print("Pipeline Test Success")
print("=" * 50)
print("Waveform Points :", len(waveform))
print("=" * 50)