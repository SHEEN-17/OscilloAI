import numpy as np
from scipy import signal


# ==========================================
# SINUS
# ==========================================

def generate_sine(frequency, amplitude, duration, sample_rate):

    t = np.linspace(
        0,
        duration,
        int(sample_rate * duration),
        endpoint=False
    )

    y = amplitude * np.sin(
        2 * np.pi * frequency * t
    )

    return t, y


# ==========================================
# SQUARE
# ==========================================

def generate_square(frequency, amplitude, duration, sample_rate):

    t = np.linspace(
        0,
        duration,
        int(sample_rate * duration),
        endpoint=False
    )

    y = amplitude * signal.square(
        2 * np.pi * frequency * t
    )

    y = amplitude * y

    return t, y


# ==========================================
# TRIANGLE
# ==========================================

def generate_triangle(frequency, amplitude, duration, sample_rate):

    t = np.linspace(
        0,
        duration,
        int(sample_rate * duration),
        endpoint=False
    )

    y = signal.sawtooth(
        2*np.pi*frequency*t,
        width=0.5
    )

    y = amplitude * y

    return t, y


# ==========================================
# SAWTOOTH
# ==========================================

def generate_sawtooth(frequency, amplitude, duration, sample_rate):

    t = np.linspace(
        0,
        duration,
        int(sample_rate * duration),
        endpoint=False
    )

    y = signal.sawtooth(
        2*np.pi*frequency*t
    )

    y = amplitude * y

    return t, y


# ==========================================
# PWM
# ==========================================

def generate_pwm(frequency, amplitude, duration, sample_rate, duty):

    t = np.linspace(
        0,
        duration,
        int(sample_rate * duration),
        endpoint=False
    )

    y = signal.square(
        2*np.pi*frequency*t,
        duty=duty
    )

    y = amplitude * y

    return t, y