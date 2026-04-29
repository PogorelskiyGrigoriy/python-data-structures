from functools import wraps
from time import perf_counter

from logger_config import setup_logging

logger = setup_logging()


def timer(func):
    @wraps(func)
    def wrapper(*a, **k):
        start_time = perf_counter()
        result = func(*a, **k)
        end_time = perf_counter()

        logger.info(
            f"Функция {func.__name__} выполнена за {end_time - start_time:.4f} сек"
        )
        return result

    return wrapper


@timer
def heavy_computation():
    for i in range(10000):
        i**i


heavy_computation()
