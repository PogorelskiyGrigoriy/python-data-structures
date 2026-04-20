import random
import time
import sys
from array import array

N = 10_000_000

big_generator = (random.uniform(0, 1) for _ in range(N))
big_array: array
start_time = time.perf_counter()
big_array = array('d', big_generator)
end_time = time.perf_counter()

print(f"running time to create array of {N} random numbers: {end_time - start_time:.6f} sec.")
print(sys.getsizeof(big_array))