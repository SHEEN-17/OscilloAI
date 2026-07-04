import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATASET_DIR = os.path.join(BASE_DIR, "dataset")

MODEL_DIR = os.path.join(BASE_DIR, "models")

os.makedirs(MODEL_DIR, exist_ok=True)

# ============================
# MODEL
# ============================

MODEL_NAME = "oscilloAI.keras"

MODEL_PATH = os.path.join(
    MODEL_DIR,
    MODEL_NAME
)

LABEL_PATH = os.path.join(
    MODEL_DIR,
    "labels.json"
)

# ============================
# TRAINING
# ============================

IMAGE_SIZE = (224, 224)

BATCH_SIZE = 32

EPOCHS = 30

LEARNING_RATE = 1e-4

VALIDATION_SPLIT = 0.2

SEED = 42