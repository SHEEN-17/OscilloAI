from pathlib import Path

from core.result import AnalysisResult

from app.image_processing.pipeline import process
from app.signal_analysis.analyzer import analyze_signal
from app.predictor_engine import Predictor
from app.explainer.engine import explain


class OscilloEngine:

    def __init__(self):

        print("=" * 60)
        print("              OSCILLO AI ENGINE")
        print("=" * 60)

        self.predictor = Predictor()

    def analyze(self, image_path):

        image_path = str(
            Path(image_path)
        )

        result = AnalysisResult()

        (
            image,
            edges,
            detected,
            warped,
            waveform_image,
            waveform,
            processed

        ) = process(image_path)

        # ==========================
        # IMAGE
        # ==========================

        result.image = image

        result.edges = edges

        result.detected = detected

        result.warped = warped

        result.waveform_image = waveform_image

        result.processed = processed

        result.waveform = waveform

        # ==========================
        # SIGNAL ANALYSIS
        # ==========================

        analysis = analyze_signal(
            waveform
        )

        result.waveform_points = analysis["points"]

        result.frequency = analysis["frequency"]

        result.amplitude = analysis["amplitude"]

        result.vrms = analysis["vrms"]

        result.duty_cycle = analysis["duty_cycle"]

        # ==========================
        # AI PREDICTION
        # ==========================

        label, confidence = self.predictor.predict(
            processed
        )

        result.prediction = label

        result.confidence = confidence

        # ==========================
        # AI EXPLANATION
        # ==========================

        result = explain(result)

        return result