from pathlib import Path

SUPPORTED_IMAGE = [
    ".png",
    ".jpg",
    ".jpeg",
    ".bmp"
]


def is_image(path):

    return Path(path).suffix.lower() in SUPPORTED_IMAGE