class aBST:

    def __init__(self, depth):
        tree_size = sum([2**x for x in range(depth)])
        self.Tree = [None] * tree_size

    def FindKeyIndex(self, key):
        root = self.Tree[0]

        if root is None or root == key:
            return 0

        return self.search_index(key, 0)
 
    def search_index(self, key, current_index):
        if current_index > len(self.Tree):
            return None

        cur_val = self.Tree[current_index]

        if  cur_val is None:
            return -current_index
        elif cur_val == key:
            return current_index
        elif cur_val > key:
            return self.search_index(key, self.left_child_index(current_index))
        else:
            return self.search_index(key, self.right_child_index(current_index))

    def left_child_index(self, current_index):
        return 2 * current_index + 1

    def right_child_index(self, current_index):
        return 2 * current_index + 2

    def AddKey(self, key):
        index = self.FindKeyIndex(key)

        if index is None:
            return -1; 

        if index > 0:
            return index
        if index < 0:
            fixed_index = -index
            self.Tree[fixed_index] = key
            return fixed_index
        if index == 0 and self.Tree[0] is None:
            self.Tree[0] = key
            return 0
        else:
            return 0