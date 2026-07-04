def recommendation(confidence):

    if confidence > 0.95:

        return "Prediksi sangat meyakinkan."

    if confidence > 0.80:

        return "Prediksi cukup baik."

    return "Disarankan mengambil foto ulang."