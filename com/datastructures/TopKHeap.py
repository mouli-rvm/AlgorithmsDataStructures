class MinHeap:
    def __init__(self):
        self.H = [None]

    def size(self):
        return len(self.H) - 1

    def __repr__(self):
        return str(self.H[1:])

    def satisfies_assertions(self):
        for i in range(2, len(self.H)):
            assert self.H[i] >= self.H[i // 2], f'Min heap property fails at position {i // 2}, parent elt: {self.H[i // 2]}, child elt: {self.H[i]}'

    def min_element(self):
        return self.H[1]

    def bubble_up(self, index):
        assert index >= 1
        if index == 1:
            return
        parent_index = index // 2
        if self.H[parent_index] < self.H[index]:
            return
        else:
            self.H[parent_index], self.H[index] = self.H[index], self.H[parent_index]
            self.bubble_up(parent_index)

    def bubble_down(self, index):
        assert index >= 1 and index < len(self.H)
        lchild_index = 2 * index
        rchild_index = 2 * index + 1
        lchild_value = self.H[lchild_index] if lchild_index < len(self.H) else float('inf')
        rchild_value = self.H[rchild_index] if rchild_index < len(self.H) else float('inf')
        if self.H[index] <= min(lchild_value, rchild_value):
            return
        min_child_value, min_child_index = min((lchild_value, lchild_index), (rchild_value, rchild_index))
        self.H[index], self.H[min_child_index] = self.H[min_child_index], self.H[index]
        self.bubble_down(min_child_index)

    def insert(self, elt):
        self.H.append(elt)
        self.bubble_up(self.size())

    def delete_min(self):
        if self.size() == 0:
            return None
        if self.size() == 1:
            return self.H.pop(1)
        root = self.H[1]
        self.H[1] = self.H.pop()
        self.bubble_down(1)
        return root

class TopKHeap:
    # The constructor of the class to initialize an empty data structure
    def __init__(self, k):
        self.k = k
        self.A = []
        self.H = MinHeap()

    def size(self):
        return len(self.A) + (self.H.size())

    def get_jth_element(self, j):
        assert 0 <= j < self.k-1
        assert j < self.size()
        return self.A[j]

    def satisfies_assertions(self):
        # is self.A sorted
        for i in range(len(self.A) -1 ):
            assert self.A[i] <= self.A[i+1], f'Array A fails to be sorted at position {i}, {self.A[i], self.A[i+1]}'
        # is self.H a heap (check min-heap property)
        self.H.satisfies_assertions()
        # is every element of self.A less than or equal to each element of self.H
        for i in range(len(self.A)):
            assert self.A[i] <= self.H.min_element(), f'Array element A[{i}] = {self.A[i]} is larger than min heap element {self.H.min_element()}'

    # Function : insert_into_A
    # This is a helper function that inserts an element `elt` into `self.A`.
    # whenever size is < k,
    #       append elt to the end of the array A
    # Move the element that you just added at the very end of
    # array A out into its proper place so that the array A is sorted.
    # return the "displaced last element" jHat (None if no element was displaced)
    def insert_into_A(self, elt):
        print("k = ", self.k)
        assert(self.size() < self.k)
        self.A.append(elt)
        j = len(self.A)-1
        while (j >= 1 and self.A[j] < self.A[j-1]):
            # Swap A[j] and A[j-1]
            (self.A[j], self.A[j-1]) = (self.A[j-1], self.A[j])
            j = j -1
        return


    # Function: insert -- insert an element into the data structure.
    # Code to handle when self.size < self.k is already provided
    def insert(self, elt):
        size = self.size()
        # If we have fewer than k elements, handle that in a special manner
        if size <= self.k:
            self.insert_into_A(elt)
            return
            # Code up your algorithm here.
        # your code here
        if(elt < self.A[self.k - 1]):
            jHat = self.A[self.k - 1]
            self.A[self.k - 1] = elt
            i = len(self.A)-1
            while (i >= 1 and self.A[i] < self.A[i-1]):
                # Swap A[j] and A[j-1]
                (self.A[i], self.A[i-1]) = (self.A[i-1], self.A[i])
                i = i -1
            #self.insert_into_A(elt)
            self.H.insert(jHat)
        else:
            self.H.insert(elt)



    # Function: Delete top k -- delete an element from the array A
    # In particular delete the j^{th} element where j = 0 means the least element.
    # j must be in range 0 to self.k-1
    def delete_top_k(self, j):
        k = self.k
        assert self.size() > k # we need not handle the case when size is less than or equal to k
        assert j >= 0
        assert j < self.k
        # your code here
        for i in range(j, len(self.A) - 1):
            self.A[i] = self.A[i+1]
        self.A[len(self.A)-1] = self.H.min_element()
        self.H.delete_min()

h = TopKHeap(5)
# Force the array A
h.A = [-10, -9, -8, -4, 0]
# Force the heap to this heap
[h.H.insert(elt) for elt in  [1, 4, 5, 6, 15, 22, 31, 7]]

print('Initial data structure: ')
print('\t A = ', h.A)
print('\t H = ', h.H)

# Insert an element -2
print('Test 1: Inserting element -2')
h.insert(-2)
print('\t A = ', h.A)
print('\t H = ', h.H)
# After insertion h.A should be [-10, -9, -8, -4, -2]
# After insertion h.H should be [None, 0, 1, 5, 4, 15, 22, 31, 7, 6]
assert h.A == [-10,-9,-8,-4,-2]
assert h.H.min_element() == 0 , 'Minimum element of the heap is no longer 0'
h.satisfies_assertions()

print('Test2: Inserting element -11')
h.insert(-11)
print('\t A = ', h.A)
print('\t H = ', h.H)
assert h.A == [-11, -10, -9, -8, -4]
assert h.H.min_element() == -2
h.satisfies_assertions()

print('Test 3 delete_top_k(3)')
h.delete_top_k(3)
print('\t A = ', h.A)
print('\t H = ', h.H)
h.satisfies_assertions()
assert h.A == [-11,-10,-9,-4,-2]
assert h.H.min_element() == 0
h.satisfies_assertions()

print('Test 4 delete_top_k(4)')
h.delete_top_k(4)
print('\t A = ', h.A)
print('\t H = ', h.H)
assert h.A == [-11, -10, -9, -4, 0]
h.satisfies_assertions()

print('Test 5 delete_top_k(0)')
h.delete_top_k(0)
print('\t A = ', h.A)
print('\t H = ', h.H)
assert h.A == [-10, -9, -4, 0, 1]
h.satisfies_assertions()

print('Test 6 delete_top_k(1)')
h.delete_top_k(1)
print('\t A = ', h.A)
print('\t H = ', h.H)
assert h.A == [-10, -4, 0, 1, 4]
h.satisfies_assertions()
print('All tests passed - 15 points!')