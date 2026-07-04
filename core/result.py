from dataclasses import dataclass
from typing import Optional


@dataclass
class AnalysisResult:

    prediction: str = ""

    confidence: float = 0.0

    frequency: float = 0.0

    vrms: float = 0.0

    vpp: float = 0.0

    amplitude: float = 0.0

    duty_cycle: float = 0.0

    waveform_points: int = 0

    explanation: str = ""

    image = None

    processed = None

    warped = None

    waveform = None