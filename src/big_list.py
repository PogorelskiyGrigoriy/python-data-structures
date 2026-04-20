import random
import time
import sys

N = 10_000_000

big_generator = (random.uniform(0, 1) for _ in range(N))
big_list: list
start_time = time.perf_counter()
big_list = [n for n in big_generator]
end_time = time.perf_counter()

print(f"running time to create list of {N} random numbers: {end_time - start_time:.6f} sec.")
print(sys.getsizeof(big_list))