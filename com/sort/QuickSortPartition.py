def swap(a, i, j):
    assert 0 <= i < len(a), f'accessing index {i} beyond end of array {len(a)}'
    assert 0 <= j < len(a), f'accessing index {j} beyond end of array {len(a)}'
    a[i], a[j] = a[j], a[i]

def tryPartition(a):
    # implementation of Lomuto partitioning algorithm
    n = len(a)
    pivot = a[n-1] # choose last element as the pivot.
    i,j = 0,0 # initialize i and j both to be 0
    for j in range(n-1): # j = 0 to n-2 (inclusive)
        # Invariant: a[0] .. a[i] are <= pivot
        #            a[i+1]...a[j-1] are > pivot
        if a[j] <= pivot:
            swap(a, i+1, j)
            i = i + 1
    swap(a, i+1, n-1) # place pivot in its correct place.
    return i+1 # return the index where we placed the pivot

def testIfPartitioned(a, k):
    # return TRUE if the array is correctly partitioned around a[k] and return FALSE otherwise
    assert 0 <= k < len(a)
    # your code here
    for i in range(len(a)):

        if (i <= k and a[i] <= a[k]) or (i > k and a[i] > a[k]):
            continue
        else:
            print(i, k, a[i], a[k])
            return False
    return True


assert testIfPartitioned([-1, 5, 2, 3, 4, 8, 9, 14, 10, 23],5) == True, ' Test # 1 failed.'
assert testIfPartitioned([-1, 5, 2, 3, 4, 8, 9, 14, 11, 23],4) == False, ' Test # 2 failed.'
assert testIfPartitioned([-1, 5, 2, 3, 4, 8, 9, 14, 23, 21],0) == True, ' Test # 3 failed.'
assert testIfPartitioned([-1, 5, 2, 3, 4, 8, 9, 14, 22, 23],9) == True, ' Test # 4 failed.'
assert testIfPartitioned([-1, 5, 2, 3, 4, 8, 9, 14, 8, 23],5) == False, ' Test # 5 failed.'
assert testIfPartitioned([-1, 5, 2, 3, 4, 8, 9, 13, 9, -11],5) == False, ' Test # 6 failed.'
assert testIfPartitioned([4, 4, 4, 4, 4, 8, 9, 13, 9, 11],4) == True, ' Test # 7 failed.'
print('Passed all tests (10 points)')

a1 = [-1, 5, 2, 3, 4, 8, 9, 14, 10, 23]
assert( len(a1) > 0)
#print(tryPartition(a1))

a2 = [-1, 5, 2, 3, 4, 8, 9, 14, 10, 23, 40]
assert( len(a2) > 0)
assert (a1 != a2)
#print(tryPartition(a2))

a3 = [-1, 5, 2, 3, 4, 8, 9]
assert( len(a3) > 0)
assert (a3 != a2)
assert (a3 != a1)
print(tryPartition(a3))