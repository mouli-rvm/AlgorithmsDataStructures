"""
binary search takes a sorted list and searches for a value
the runtime of binary search is O(log n)
"""


def binary_search(arr, item):

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            high = mid - 1
            continue
        elif arr[mid] < item:
            low = mid + 1
            continue

    return None


listVal = [1, 2, 3, 6, 8, 9, 10, 11, 12, 15]
searchVal = 11
print(binary_search(listVal, searchVal))