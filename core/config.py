from pathlib import Path

# =====================================
# PROJECT ROOT
# =====================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# =====================================
# FOLDER
# =====================================

DATASET_DIR = PROJECT_ROOT / "dataset"

MODEL_DIR = PROJECT_ROOT / "models"

TEST_IMAGE_DIR = PROJECT_ROOT / "test_images"

REPORT_DIR = PROJECT_ROOT / "reports"

EXPORT_DIR = PROJECT_ROOT / "exports"

LOG_DIR = PROJECT_ROOT / "logs"

# =====================================
# MODEL
# =====================================

MODEL_PATH = MODEL_DIR / "oscilloAI.keras"

LABEL_PATH = MODEL_DIR / "labels.json"

# =====================================
# IMAGE
# =====================================

IMAGE_SIZE = (224, 224)

# =====================================
# APP
# =====================================

APP_NAME = "OscilloAI"

VERSION = "0.1.0"