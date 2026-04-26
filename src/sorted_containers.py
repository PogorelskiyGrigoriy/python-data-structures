from bisect import bisect_left, bisect_right

numbers = [10, 20, 20, 20, 20, 30, 40, 50]
print(bisect_left(numbers, 20))
print(bisect_right(numbers, 20))
min = bisect_left(numbers, 20)
max = bisect_right(numbers, 30)
print(numbers[min:max])
