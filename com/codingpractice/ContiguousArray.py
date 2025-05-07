
def contiguousArray(arr):
    curr_sum = 0
    max_sum = arr[0]

    for i in arr:
        curr_sum += i
        max_sum = max(curr_sum, max_sum)

        if curr_sum < 0:
            curr_sum = 0

    return max_sum

print(contiguousArray([-1,-3,5,-4,3,-6,9,2]))