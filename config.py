import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_DESTINATION = os.getenv("LOG_DESTINATION", "logs/app.log")

LOG_SERIALIZE = os.getenv("LOG_SERIALIZE", "False").lower() == "true"

# 3. Пример добавления других констант (будущих)
# APP_NAME = "MyCRM"
# DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"