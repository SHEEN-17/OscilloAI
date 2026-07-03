import os
import cv2
import numpy as np


IMAGE_SIZE = 224


def load_images(folder):

    images = []

    labels = []

    classes = sorted(os.listdir(folder))

    for label, class_name in enumerate(classes):

        class_folder = os.path.join(folder, class_name)

        if not os.path.isdir(class_folder):
            continue

        for file in os.listdir(class_folder):

            if file.endswith(".png"):

                path = os.path.join(class_folder, file)

                image = cv2.imread(path)

                image = cv2.resize(
                    image,
                    (IMAGE_SIZE, IMAGE_SIZE)
                )

                image = image / 255.0

                images.append(image)

                labels.append(label)

    return (
        np.array(images),
        np.array(labels),
        classes
    )