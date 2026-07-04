from tensorflow.keras.models import load_model

from dataset import load_dataset

from config import MODEL_PATH


def evaluate():

    model = load_model(

        MODEL_PATH

    )

    train_dataset, validation_dataset, _ = load_dataset()

    loss, accuracy = model.evaluate(

        validation_dataset

    )

    print()

    print("------------------------")

    print(f"Loss      : {loss:.4f}")

    print(f"Accuracy  : {accuracy:.4f}")

    print("------------------------")


if __name__ == "__main__":

    evaluate()