import time
from functools import lru_cache

arg = [1, 1, 2, 2, 2, 3, 4, 5]  # Example input


@lru_cache()  # Cache results of the function
def long_square(n):
    time.sleep(2)  # Simulate a long computation
    return n * n


def run_test():
    for n in arg:
        start = time.perf_counter()
        result = long_square(n)
        end = time.perf_counter()
        print(f"Result for {n}: {result} | Time: {end - start:.4f}s")

print("--- First Run (Computing) ---")
run_test()

print("\n--- Second Run (From Cache) ---")
run_test()

print("\nCache Info:", long_square.cache_info())
