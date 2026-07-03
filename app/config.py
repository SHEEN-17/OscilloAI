import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

APP_DIR = os.path.join(BASE_DIR, "app")

MODEL_DIR = os.path.join(BASE_DIR, "models")

DATASET_DIR = os.path.join(BASE_DIR, "dataset")

REPORT_DIR = os.path.join(BASE_DIR, "reports")

EXPORT_DIR = os.path.join(BASE_DIR, "exports")

LOG_DIR = os.path.join(BASE_DIR, "logs")

TEMP_DIR = os.path.join(BASE_DIR, "temp")

ASSET_DIR = os.path.join(APP_DIR, "assets")

MODEL_PATH = os.path.join(
    MODEL_DIR,
    "oscilloAI.keras"
)

LABEL_PATH = os.path.join(
    MODEL_DIR,
    "labels.json"
)