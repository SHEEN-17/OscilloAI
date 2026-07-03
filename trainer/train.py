from loader import load_dataset
from model import create_model
from metrics import plot_history

import os

print("=" * 50)
print("OscilloAI Training")
print("=" * 50)

# Load dataset
X_train, X_val, y_train, y_val, classes = load_dataset("../dataset")

print(f"Jumlah kelas : {len(classes)}")
print(f"Kelas        : {classes}")

# Build model
model = create_model(len(classes))

model.summary()

# Training
history = model.fit(

    X_train,

    y_train,

    validation_data=(X_val, y_val),

    epochs=20,

    batch_size=32

)

# Pastikan folder models ada
os.makedirs("../models", exist_ok=True)

# Simpan model
model.save("../models/oscilloAI.keras")

print("\nModel berhasil disimpan.")

# Tampilkan grafik
plot_history(history)