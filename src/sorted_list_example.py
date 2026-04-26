from sortedcontainers import SortedList

my_sorted_list = SortedList([5,5,5,5, 3, 1, 4, 2])
print("Sorted List:", my_sorted_list)
my_sorted_list.add(0)
print("After adding 0:", my_sorted_list)

print(list(reversed(my_sorted_list)))
