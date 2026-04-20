import numpy as np
import time
import sys

N = 100_000_000

# 1. "Неправильный" способ (через конвертацию из Python-объектов)
# Мы делаем это, чтобы ты увидел разницу в скорости конвертации
big_generator = (float(i) for i in range(N)) # имитируем поток данных
start_time = time.perf_counter()
# NumPy будет пытаться упаковать каждый элемент
np_array_from_gen = np.fromiter(big_generator, dtype=np.float64, count=N)
end_time = time.perf_counter()

print(f"NumPy (fromiter): {end_time - start_time:.6f} sec.")

# 2. "Правильный" способ (Векторизованный)
# NumPy создает массив сразу в C, минуя создание объектов Python
start_time = time.perf_counter()
big_np_array = np.random.uniform(0, 1, N)
end_time = time.perf_counter()

print(f"NumPy (native random): {end_time - start_time:.6f} sec.")

# Проверка памяти
print(f"getsizeof (metadata only): {sys.getsizeof(big_np_array)} bytes")
print(f"nbytes (actual data): {big_np_array.nbytes} bytes (~{big_np_array.nbytes / 1024 / 1024:.2f} MB)")