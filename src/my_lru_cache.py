from collections import OrderedDict
from collections.abc import Hashable
from typing import Generic, TypeVar, Optional

K = TypeVar('K', bound=Hashable)
V = TypeVar('V')

class MyLruCache(Generic[K, V]):
    def __init__(self, capacity: int):
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