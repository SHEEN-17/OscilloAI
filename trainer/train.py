from loader import load_dataset
from model import build_model

import tensorflow as tf

print("="*50)
print("OscilloAI Training")
print("="*50)

train_ds, val_ds = load_dataset()

model = build_model()

model.summary()

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=20
)

model.save("../models/oscilloAI.keras")

print("\nTraining selesai.")