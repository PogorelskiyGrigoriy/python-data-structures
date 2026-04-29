import time
import functools
from logger_config import setup_logging

logger = setup_logging()

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        
        logger.info(f"Функция {func.__name__} выполнена за {end_time - start_time:.4f} сек")
        return result
    return wrapper

@timer
def heavy_computation():
    time.sleep(1.5) # Имитация долгой работы
    return "Done"

heavy_computation()