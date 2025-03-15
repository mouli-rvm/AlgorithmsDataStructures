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

class MedianMaintainingHeap:
    def __init__(self):
        self.hmin = MinHeap()
        self.hmax = MaxHeap()

    def satisfies_assertions(self):
        if self.hmin.size() == 0:
            assert self.hmax.size() == 0
            return
        if self.hmax.size() == 0:
            assert self.hmin.size() == 1
            return
        assert self.hmax.max_element() <= self.hmin.min_element(), f'Failed: Max element of max heap = {self.hmax.max_element()} > min element of min heap {self.hmin.min_element()}'
        s_min = self.hmin.size()
        s_max = self.hmax.size()
        assert (s_min == s_max or s_max == s_min - 1), f'Heap sizes are unbalanced. Min heap size = {s_min} and Maxheap size = {s_max}'

    def __repr__(self):
        return 'Maxheap:' + str(self.hmax) + ' Minheap:' + str(self.hmin)

    def get_median(self):
        if self.hmin.size() == 0:
            assert self.hmax.size() == 0, 'Sizes are not balanced'
            assert False, 'Cannot ask for median from empty heaps'
        if self.hmax.size() == 0:
            assert self.hmin.size() == 1, 'Sizes are not balanced'
            return self.hmin.min_element()
        if self.hmin.size() == self.hmax.size():
            return (self.hmax.max_element() + self.hmin.min_element()) / 2
        else:
            return self.hmin.min_element()

    def balance_heap_sizes(self):
        s_min = self.hmin.size()
        s_max = self.hmax.size()
        if s_min > s_max + 1:
            self.hmax.insert(self.hmin.delete_min())
        elif s_max > s_min:
            self.hmin.insert(self.hmax.delete_max())



    def insert(self, elt):
        if self.hmin.size() == 0:
            self.hmin.insert(elt)
            return
        if self.hmax.size() == 0:
            assert self.hmin.size() == 1
            if elt > self.hmin.min_element():
                current_min = self.hmin.min_element()
                self.hmin.delete_min()
                self.hmin.insert(elt)
                self.hmax.insert(current_min)
            else:
                self.hmax.insert(elt)
            return
        if elt < self.hmax.max_element():
            self.hmax.insert(elt)
        else:
            self.hmin.insert(elt)
        self.balance_heap_sizes()

    def delete_median(self):
        self.hmax.delete_max()
        self.balance_heap_sizes()

m = MedianMaintainingHeap()
print('Inserting 1, 5, 2, 4, 18, -4, 7, 9')

m.insert(1)
print(m)
print(m.get_median())
m.satisfies_assertions()
assert m.get_median() == 1,  f'expected median = 1, your code returned {m.get_median()}'

m.insert(5)
print(m)
print(m.get_median())
m.satisfies_assertions()
assert m.get_median() == 3,  f'expected median = 3.0, your code returned {m.get_median()}'

m.insert(2)
print(m)
print(m.get_median())
m.satisfies_assertions()
assert m.get_median() == 2,  f'expected median = 2, your code returned {m.get_median()}'

m.insert(4)
print(m)
print(m.get_median())
m.satisfies_assertions()
assert m.get_median() == 3,  f'expected median = 3, your code returned {m.get_median()}'

m.insert(18)
print(m)
print(m.get_median())
m.satisfies_assertions()
assert m.get_median() == 4,  f'expected median = 4, your code returned {m.get_median()}'

m.insert(-4)
print(m)
print(m.get_median())
m.satisfies_assertions()
assert m.get_median() == 3,  f'expected median = 3, your code returned {m.get_median()}'

m.insert(7)
print(m)
print(m.get_median())
m.satisfies_assertions()
assert m.get_median() == 4, f'expected median = 4, your code returned {m.get_median()}'

m.insert(9)
print(m)
print(m.get_median())
m.satisfies_assertions()
assert m.get_median()== 4.5, f'expected median = 4.5, your code returned {m.get_median()}'

print('All tests passed: 15 points')
