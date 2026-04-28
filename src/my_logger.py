from logger_config import setup_logging

# Инициализируем настройки
logger = setup_logging()

logger.debug("Logger initialized successfully.")
logger.info("Logging is set up and ready to use.")
logger.trace("This is a trace message, useful for very detailed debugging.")
logger.warning("This is a warning message, indicating a potential issue.")
logger.error("This is an error message, indicating a failure in the application.")