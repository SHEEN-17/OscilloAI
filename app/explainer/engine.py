from .waveform import explain_waveform
from .recommendation import recommendation


def explain(result):

    info = explain_waveform(
        result.prediction
    )

    result.explanation = {

        "title": info["name"],

        "description": info["description"],

        "application": info["application"],

        "recommendation": recommendation(
            result.confidence
        )
    }

    return result