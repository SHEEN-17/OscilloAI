from predictor import predict_image
from explain import get_explanation


def analyze(image_path):

    wave, confidence, probabilities = predict_image(image_path)

    explanation = get_explanation(wave)

    return {

        "wave": wave,

        "confidence": confidence,

        "probabilities": probabilities,

        "explanation": explanation

    }