import os
import cv2

from pipeline import process

CURRENT_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

PROJECT_ROOT = os.path.abspath(
    os.path.join(
        CURRENT_DIR,
        "..",
        ".."
    )
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

print()

print("=" * 40)

print("Waveform Points :", len(waveform))

print("=" * 40)

cv2.imshow("Original", image)

cv2.imshow("Edges", edges)

cv2.imshow("Detected Screen", detected)

if warped is not None:

    cv2.imshow("Warped", warped)

if waveform_image is not None:

    cv2.imshow("Waveform", waveform_image)

cv2.waitKey(0)

cv2.destroyAllWindows()