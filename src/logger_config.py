import os
import sys
from dotenv import load_dotenv
from loguru import logger

# Загружаем переменные из .env
load_dotenv()

def setup_logging():
    # Извлекаем настройки или ставим дефолты
    log_level = os.getenv("LOG_LEVEL", "INFO")
    log_file = os.getenv("LOG_DESTINATION", "logs/app.log")
    # Переменные из .env всегда строки, приводим к bool
    serialize = os.getenv("LOG_SERIALIZE", "False").lower() == "true"

    # Удаляем дефолтный обработчик
    logger.remove()

    # 1. Консольный логгер (красивый, для разработчика)
    logger.add(
        sys.stdout,
        level=log_level,
        colorize=True,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
    )

    # 2. Файловый логгер (структурированный, для продакшена)
    logger.add(
        log_file,
        level=log_level,
        serialize=serialize, # Если True, лог станет JSON-строкой
        rotation="100 MB",
        retention="7 days",
        compression="zip"
    )

    return logger