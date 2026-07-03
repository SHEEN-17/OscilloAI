import os

from loader import load_images

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

dataset = os.path.join(
    BASE_DIR,
    "dataset"
)

X, y, classes = load_images(dataset)

print("Jumlah gambar :", len(X))

print("Jumlah label :", len(y))

print(classes)