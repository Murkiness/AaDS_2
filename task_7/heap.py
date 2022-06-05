class Heap:

    def __init__(self):
        self.HeapArray = [] # хранит неотрицательные числа-ключи

    def MakeHeap(self, a, depth):
        heap_size = pow(2, depth + 1) - 1
        self.HeapArray = [None] * heap_size
        for key in a[:heap_size]:
            self.Add(key)

    def GetMax(self):
        if self.HeapArray is None or self.HeapArray[0] is None:
            return -1

        largest_key = self.HeapArray[0]
        last_non_none_index = self.HeapArray.index(None) - 1 if None in self.HeapArray else len(self.HeapArray) - 1
        self.HeapArray[0] = self.HeapArray[last_non_none_index]
        self.HeapArray[last_non_none_index] = None
        self._sift_down()
        return largest_key

    def Add(self, key):
        new_ind = self._find_index()
        if key is None or new_ind is None:
            return False

        self.HeapArray[new_ind] = key
        self._sift_up(new_ind)

    def _find_index(self):
        try:
            return self.HeapArray.index(None)
        except ValueError:
            return

    def _sift_up(self, index):
        if index < 1:
            return

        parent_ind = (index - 1) // 2
        if self.HeapArray[parent_ind] < self.HeapArray[index]:
            self.swap(self.HeapArray, parent_ind, index)
            self._sift_up(parent_ind)

    def _sift_down(self, index=0):
        root = self.HeapArray[index]
        try:
            left_child = self.HeapArray[index * 2 + 1]
            right_child = self.HeapArray[index * 2 + 2]
        except IndexError:
            return

        if left_child is None or right_child is None:
            return

        if left_child > right_child and left_child > root:
            child_ind = index * 2 + 1
            self.swap(self.HeapArray, child_ind, index)
            self._sift_down(child_ind)
        elif right_child > left_child and right_child > root:
            child_ind = index * 2 + 2
            self.swap(self.HeapArray, child_ind, index)
            self._sift_down(child_ind)

    def swap(self, arr, a, b):
        arr[a], arr[b] = arr[b], arr[a]
