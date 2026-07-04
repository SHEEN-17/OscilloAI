from dataset import load_dataset
from model import create_model
from callbacks import get_callbacks
from export import export_labels
from config import EPOCHS


def train():

    print("=" * 50)
    print("Loading Dataset...")
    print("=" * 50)

    train_dataset, validation_dataset, class_names = load_dataset()

    print()
    print("Classes :", class_names)

    model = create_model(
        len(class_names)
    )

    model.summary()

    print()
    print("=" * 50)
    print("Training Started")
    print("=" * 50)

    history = model.fit(

        train_dataset,

        validation_data=validation_dataset,

        epochs=EPOCHS,

        callbacks=get_callbacks()

    )

    export_labels(class_names)

    print()
    print("=" * 50)
    print("Training Finished")
    print("=" * 50)

    return history


if __name__ == "__main__":

    train()