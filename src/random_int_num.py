import random
from typing import Iterator

class RandomIntNums:
    def __init__(self, min_val: int, max_val: int, *, amount: int = -1, isDistinct: bool = False):
        if min_val >= max_val:
            raise ValueError("min must be less than max")
        
        self._min = min_val
        self._max = max_val
        self._amount = amount
        self._is_distinct = isDistinct
        self._range_size = max_val - min_val + 1

        if self._is_distinct and self._amount > self._range_size:
            raise ValueError(
                f"Cannot yield {self._amount} distinct numbers from a range of size {self._range_size}"
            )

    def __iter__(self) -> Iterator[int]:
        count = 0
        seen = set()
        
        while self._amount == -1 or count < self._amount:
            if self._is_distinct and len(seen) >= self._range_size:
                break

            num = self._get_random_number()
            
            if self._is_distinct:
                while num in seen:
                    num = self._get_random_number()
                seen.add(num)
            
            yield num
            count += 1
            
    def _get_random_number(self) -> int:       
        return random.randint(self._min, self._max)