import os
import sys
from dotenv import load_dotenv
from loguru import logger

# Load environment variables from .env file
load_dotenv()

def setup_logging():
    # Fetch settings from environment or use defaults
    log_level = os.getenv("LOG_LEVEL", "INFO")
    log_file = os.getenv("LOG_DESTINATION", "logs/app.log")
    # Convert string from .env to boolean
    serialize = os.getenv("LOG_SERIALIZE", "False").lower() == "true"

    # Remove default handler to prevent duplicate logs
    logger.remove()

    # 1. Console handler for development (colorized output)
    logger.add(
        sys.stdout,
        level=log_level,
        colorize=True,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
    )

    # 2. File handler for production (structured logs)
    logger.add(
        log_file,
        level=log_level,
        serialize=serialize, # If True, logs are stored as JSON
        rotation="100 MB",
        retention="7 days",
        compression="zip"
    )

    return logger