class MaxHeap:
    def __init__(self):
        self.H = [None]

    def size(self):
        return len(self.H) - 1

    def __repr__(self):
        return str(self.H[1:])

    def satisfies_assertions(self):
        for i in range(2, len(self.H)):
            assert self.H[i] <= self.H[i // 2], f'Maxheap property fails at position {i // 2}, parent elt: {self.H[i // 2]}, child elt: {self.H[i]}'

    def max_element(self):
        return self.H[1]

    def bubble_up(self, index):
        assert index >= 1
        if index == 1:
            return
        parent_index = index // 2
        if self.H[parent_index] < self.H[index]:
            self.H[parent_index], self.H[index] = self.H[index], self.H[parent_index]
            self.bubble_up(parent_index)

    def bubble_down(self, index):
        assert index >= 1 and index < len(self.H)
        lchild_index = 2 * index
        rchild_index = 2 * index + 1
        lchild_value = self.H[lchild_index] if lchild_index < len(self.H) else float('-inf')
        rchild_value = self.H[rchild_index] if rchild_index < len(self.H) else float('-inf')
        if self.H[index] >= max(lchild_value, rchild_value):
            return
        max_child_value, max_child_index = max((lchild_value, lchild_index), (rchild_value, rchild_index))
        self.H[index], self.H[max_child_index] = self.H[max_child_index], self.H[index]
        self.bubble_down(max_child_index)

    def insert(self, elt):
        self.H.append(elt)
        self.bubble_up(self.size())

    def delete_max(self):
        if self.size() == 0:
            return None
        if self.size() == 1:
            return self.H.pop(1)
        max_elt = self.H[1]
        self.H[1] = self.H.pop()
        self.bubble_down(1)
        return max_elt


h = MaxHeap()
print('Inserting: 5, 2, 4, -1 and 7 in that order.')
h.insert(5)
print(f'\t Heap = {h}')
assert(h.max_element() == 5)
h.insert(2)
print(f'\t Heap = {h}')
assert(h.max_element() == 5)
h.insert(4)
print(f'\t Heap = {h}')
assert(h.max_element() == 5)
h.insert(-1)
print(f'\t Heap = {h}')
assert(h.max_element() == 5)
h.insert(7)
print(f'\t Heap = {h}')
assert(h.max_element() == 7)
h.satisfies_assertions()

print('Deleting maximum element')
h.delete_max()
print(f'\t Heap = {h}')
assert(h.max_element() == 5)
h.delete_max()
print(f'\t Heap = {h}')
assert(h.max_element() == 4)
h.delete_max()
print(f'\t Heap = {h}')
assert(h.max_element() == 2)
h.delete_max()
print(f'\t Heap = {h}')
assert(h.max_element() == -1)
# Test delete_max on heap of size 1, should result in empty heap.
h.delete_max()
print(f'\t Heap = {h}')
print('All tests passed: 5 points!')
