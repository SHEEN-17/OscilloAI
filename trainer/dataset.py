import tensorflow as tf

from config import (
    DATASET_DIR,
    IMAGE_SIZE,
    BATCH_SIZE,
    VALIDATION_SPLIT,
    SEED
)


def load_dataset():

    train_dataset = tf.keras.utils.image_dataset_from_directory(

        DATASET_DIR,

        validation_split=VALIDATION_SPLIT,

        subset="training",

        seed=SEED,

        image_size=IMAGE_SIZE,

        batch_size=BATCH_SIZE,

        label_mode="categorical"

    )

    validation_dataset = tf.keras.utils.image_dataset_from_directory(

        DATASET_DIR,

        validation_split=VALIDATION_SPLIT,

        subset="validation",

        seed=SEED,

        image_size=IMAGE_SIZE,

        batch_size=BATCH_SIZE,

        label_mode="categorical"

    )

    class_names = train_dataset.class_names

    AUTOTUNE = tf.data.AUTOTUNE

    train_dataset = train_dataset.prefetch(AUTOTUNE)

    validation_dataset = validation_dataset.prefetch(AUTOTUNE)

    return (

        train_dataset,

        validation_dataset,

        class_names

    )