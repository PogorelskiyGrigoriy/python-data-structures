from abc import ABC, abstractmethod
from logger_config import setup_logging

logger = setup_logging()

class LegacyLogger(ABC):
    @abstractmethod
    def print_message(self, message: str):
        pass
    
class RegularPrinter(LegacyLogger):
    def print_message(self, message: str):
        logger.info(f"RegularPrinter: {message}")
        
class NewLogger(ABC):
    @abstractmethod
    def info(self, message: str):
        pass
    
class LoggerAdapter(NewLogger):
    def __init__(self, legacy_logger: LegacyLogger):
        self.__legacy_logger = legacy_logger
        
    def info(self, message: str):
        self.__legacy_logger.print_message(message)