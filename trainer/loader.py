import os
import cv2
import numpy as np

from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

IMAGE_SIZE = 224


def load_dataset(folder="../dataset"):

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

                image = image.astype("float32") / 255.0

                images.append(image)

                labels.append(label)

    images = np.array(images)

    labels = np.array(labels)

    labels = to_categorical(
        labels,
        num_classes=len(classes)
    )

    X_train, X_val, y_train, y_val = train_test_split(

        images,

        labels,

        test_size=0.2,

        random_state=42,

        shuffle=True

    )

    return (

        X_train,

        X_val,

        y_train,

        y_val,

        classes

    )