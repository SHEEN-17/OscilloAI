EXPLANATION = {

    "sinus": {

        "description":
        "Gelombang sinus memiliki perubahan tegangan yang halus dan periodik.",

        "applications": [
            "PLN",
            "Generator",
            "Audio",
            "Inverter"
        ],

        "tips":
        "Jika bentuk sinus terpotong (clipping), kemungkinan terdapat masalah pada penguat atau sumber daya."
    },

    "square": {

        "description":
        "Gelombang kotak memiliki dua level tegangan yang berubah secara cepat.",

        "applications": [
            "Digital Logic",
            "Clock",
            "Microcontroller"
        ],

        "tips":
        "Periksa duty cycle apabila lebar pulsa terlihat tidak simetris."
    },

    "triangle": {

        "description":
        "Gelombang segitiga berubah secara linear antara nilai minimum dan maksimum.",

        "applications": [
            "Function Generator",
            "PWM Control",
            "Analog Synthesizer"
        ],

        "tips":
        "Perhatikan apakah kemiringan naik dan turun tetap linear."
    },

    "sawtooth": {

        "description":
        "Gelombang gigi gergaji naik secara perlahan lalu turun dengan cepat.",

        "applications": [
            "CRT",
            "Sweep Generator",
            "Signal Generator"
        ],

        "tips":
        "Pastikan bagian reset terjadi secara cepat tanpa noise."
    },

    "pwm": {

        "description":
        "PWM merupakan sinyal digital dengan duty cycle yang dapat berubah.",

        "applications": [
            "Motor Driver",
            "Buck Converter",
            "LED Dimmer"
        ],

        "tips":
        "Analisis duty cycle sangat penting untuk mengetahui besar daya keluaran."
    }

}


def get_explanation(wave):

    return EXPLANATION.get(
        wave.lower(),
        None
    )