# import random

# N = 10
# x, y = -55, 55
# my_random_list = [random.randint(x, y) for _ in range(N)]

my_list = [13, 2, 100, 17, -1, -30, 8]

result = sorted(my_list, key=lambda x: (x % 2, -x if x % 2 else x))
print(result)
