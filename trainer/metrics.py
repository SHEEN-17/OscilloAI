import matplotlib.pyplot as plt


def plot_history(history):

    plt.figure(figsize=(10,5))

    plt.plot(history.history["accuracy"])

    plt.plot(history.history["val_accuracy"])

    plt.title("Training Accuracy")

    plt.xlabel("Epoch")

    plt.ylabel("Accuracy")

    plt.legend([
        "Train",
        "Validation"
    ])

    plt.grid()

    plt.show()