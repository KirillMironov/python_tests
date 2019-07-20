import random


def binary_search(my_list, item):
    low = 0
    high = len(my_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if my_list[mid] == item:
            return mid
        elif my_list[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


list_ex = random.sample(range(100000), 1000)
list_ex.sort()

print(binary_search(list_ex, random.randint(1, 1000000)))
print(binary_search(list_ex, random.randint(1, 1000000)))

