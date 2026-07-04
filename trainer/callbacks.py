import tensorflow as tf

from config import MODEL_PATH


def get_callbacks():

    return [

        tf.keras.callbacks.EarlyStopping(

            monitor="val_loss",

            patience=5,

            restore_best_weights=True

        ),

        tf.keras.callbacks.ModelCheckpoint(

            filepath=MODEL_PATH,

            monitor="val_accuracy",

            save_best_only=True

        ),

        tf.keras.callbacks.ReduceLROnPlateau(

            factor=0.5,

            patience=2

        )

    ]