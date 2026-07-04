import json

from config import LABEL_PATH


def export_labels(class_names):

    with open(

        LABEL_PATH,

        "w",

        encoding="utf-8"

    ) as file:

        json.dump(

            class_names,

            file,

            indent=4

        )

    print()

    print("Labels exported")

    print(LABEL_PATH)