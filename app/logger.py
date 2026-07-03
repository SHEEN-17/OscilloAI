import csv
import os
from datetime import datetime


LOG_PATH = os.path.join(
    "..",
    "logs",
    "prediction_log.csv"
)


def save_log(filename, wave, confidence):

    file_exists = os.path.isfile(LOG_PATH)

    with open(
        LOG_PATH,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow([
                "Datetime",
                "Filename",
                "Waveform",
                "Confidence"
            ])

        writer.writerow([

            datetime.now(),

            filename,

            wave,

            f"{confidence:.2f}"

        ])