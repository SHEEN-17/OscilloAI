import tensorflow as tf

from config import IMAGE_SIZE


def create_model(num_classes):

    base_model = tf.keras.applications.MobileNetV2(

        include_top=False,

        weights="imagenet",

        input_shape=(
            IMAGE_SIZE[0],
            IMAGE_SIZE[1],
            3
        )

    )

    base_model.trainable = False

    model = tf.keras.Sequential([

        base_model,

        tf.keras.layers.GlobalAveragePooling2D(),

        tf.keras.layers.Dropout(0.3),

        tf.keras.layers.Dense(

            num_classes,

            activation="softmax"

        )

    ])

    model.compile(

        optimizer=tf.keras.optimizers.Adam(

            learning_rate=0.0001

        ),

        loss="categorical_crossentropy",

        metrics=[

            "accuracy"

        ]

    )

    return model