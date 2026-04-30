import functools
from collections import OrderedDict
from collections.abc import Hashable
from typing import Any, Callable, Generic, Optional, TypeVar

K = TypeVar("K", bound=Hashable)
V = TypeVar("V")


class MyLruCache(Generic[K, V]):
    def __init__(self, capacity: int=128):
        self.capacity = capacity
        self.cache: OrderedDict[K, V] = OrderedDict()

    def access(self, key: K) -> Optional[V]:
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)
        return self.cache[key]

    def add(self, key: K, value: V) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def clear(self) -> None:
        self.cache.clear()


#######################


def lru_cache_wrapper(capacity: int):
    def decorator(func: Callable) -> Callable:
        # Создаем экземпляр твоего класса для конкретной функции
        my_cache = MyLruCache[tuple, Any](capacity=capacity)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Генерируем ключ из аргументов
            # Важно: аргументы должны быть хэшируемыми!
            key = (args, tuple(sorted(kwargs.items())))

            # Пытаемся достать из кеша через твой метод access
            cached_result = my_cache.access(key)

            if cached_result is not None:
                return cached_result

            # Если в кеше нет — вычисляем
            result = func(*args, **kwargs)

            # Добавляем в кеш через твой метод add
            my_cache.add(key, result)

            return result

        # Привязываем метод очистки твоего класса к обертке
        wrapper.cache_clear = my_cache.clear
        return wrapper

    return decorator


# Пример использования:
@lru_cache_wrapper(capacity=2)
def get_data(user_id: int):
    print(f"--- Вычисляем данные для {user_id} ---")
    return {"id": user_id, "data": "some_heavy_payload"}


# Тест
get_data(1)  # Вычислит
get_data(1)  # Возьмет из твоего MyLruCache
get_data(2)  # Вычислит
get_data(3)  # Вычислит, вытеснит (1) из твоего OrderedDict
