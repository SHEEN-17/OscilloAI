from core.engine import OscilloEngine

engine = OscilloEngine()

result = engine.analyze("test_images/test.png")

print("=" * 60)

print("Prediction :", result.prediction)

print("Confidence :", f"{result.confidence*100:.2f}%")

print()

print(result.explanation["title"])

print()

print(result.explanation["description"])

print()

print("Application")

print(result.explanation["application"])

print()

print(result.explanation["recommendation"])

print("=" * 60)