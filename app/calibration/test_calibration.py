from app.calibration.engine import CalibrationEngine


waveform = [

    (0, 150),

    (10, 130),

    (20, 110),

    (30, 90),

    (40, 70),

    (50, 90),

    (60, 110),

    (70, 130),

    (80, 150)

]

engine = CalibrationEngine(

    waveform,

    (800, 1000)

)

print()

print("=" * 50)

print("Amplitude :", engine.amplitude())

print("Vpp       :", engine.vpp())

print("Period    :", engine.period())

print("Frequency :", engine.frequency())

print("=" * 50)