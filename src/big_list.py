import random
import time
import sys

N = 1_000_000

big_list: list
start_time = time.perf_counter()
big_list = [random.uniform(0, 1) for _ in range(N)]
end_time = time.perf_counter()

print(f"running time to create list of {N} random numbers: {end_time - start_time:.6f} sec.")
print(sys.getsizeof(big_list))

