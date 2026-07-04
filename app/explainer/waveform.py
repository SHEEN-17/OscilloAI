from .glossary import EXPLANATION


def explain_waveform(label):

    label = label.lower()

    if label in EXPLANATION:

        return EXPLANATION[label]

    return {

        "name": label,

        "description": "Belum tersedia.",

        "application": "-"
    }