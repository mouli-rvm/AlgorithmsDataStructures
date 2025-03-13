def quicksort(arr):

    if len(arr) < 2:
        return arr

    partition = arr[0]
    less = []
    greater = []

    for i in arr[1:]:
        if i <= partition:
            less.append(i)
        else:
            greater.append(i)

    return quicksort(less) + [partition] + quicksort(greater)

j1 = quicksort([6, 9, 4, 10, 4, 5, 3 ,2, 1])
print(j1)