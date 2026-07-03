import os

def create_folder():

    folder = [
        "dataset/sinus",
        "dataset/square",
        "dataset/triangle",
        "dataset/sawtooth",
        "dataset/pwm"
    ]

    for f in folder:
        os.makedirs(
            f,
            exist_ok=True
        )

    print("Folder berhasil dibuat.")


if __name__ == "__main__":
    create_folder()