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
    def __init__(self, k):
        self.k = k
        self.A = []
        self.H = MinHeap()

    def size(self):
        return len(self.A) + self.H.size()

    def get_jth_element(self, j):
        assert 0 <= j < self.k - 1
        assert j < self.size()
        return self.A[j]

    def satisfies_assertions(self):
        for i in range(len(self.A) - 1):
            assert self.A[i] <= self.A[i + 1], f'Array A fails to be sorted at position {i}, {self.A[i], self.A[i + 1]}'
        self.H.satisfies_assertions()
        for i in range(len(self.A)):
            assert self.A[i] <= self.H.min_element(), f'Array element A[{i}] = {self.A[i]} is larger than min heap element {self.H.min_element()}'

    def insert_into_A(self, elt):
        assert self.size() < self.k
        self.A.append(elt)
        j = len(self.A) - 1
        while j >= 1 and self.A[j] < self.A[j - 1]:
            self.A[j], self.A[j - 1] = self.A[j - 1], self.A[j]
            j -= 1

    def insert(self, elt):
        size = self.size()
        if size < self.k:
            self.insert_into_A(elt)
            return
        else:
            if elt < self.A[-1]:
                self.H.insert(self.A.pop())
                self.insert_into_A(elt)
            else:
                self.H.insert(elt)
            while self.H.size() > 0 and self.H.min_element() < self.A[-1]:
                self.insert_into_A(self.H.delete_min())
                if len(self.A) > self.k:
                    self.H.insert(self.A.pop())

    def delete_top_k(self, j):
        assert self.size() > self.k
        assert 0 <= j < self.k
        removed_elt = self.A.pop(j)
        if self.H.size() > 0:
            self.insert_into_A(self.H.delete_min())
        else:
            # If H is empty, A will have fewer than k elements, so we don't need to do anything else
            pass


h = TopKHeap(5)
h.A = [-10, -9, -8, -4, 0]
[h.H.insert(elt) for elt in [1, 4, 5, 6, 15, 22, 31, 7]]

print('Initial data structure: ')
print('\t A = ', h.A)
print('\t H = ', h.H)

print('Test 1: Inserting element -2')
h.insert(-2)
print('\t A = ', h.A)
print('\t H = ', h.H)
assert h.A == [-10, -9, -8, -4, -2]
assert h.H.min_element() == 0, 'Minimum element of the heap is no longer 0'
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
assert h.A == [-11, -10, -9, -4, -2]
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
