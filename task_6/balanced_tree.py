class BSTNode:
	
    def __init__(self, key, parent):
        self.NodeKey = key # ключ узла
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок
        self.Level = 0 # уровень узла

class BalancedBST:
    def __init__(self):
        self.Root = None # корень дерева

    def GenerateTree(self, a):
        if a == [] or a is None:
            return None

        a.sort()

        mid = len(a) // 2
        mid_element = a[mid]
        self.Root = BSTNode(mid_element, None)

        left_array = a[0:mid]
        right_array = a[mid+1:]

        self.gen_tree(left_array, self.Root, True)
        self.gen_tree(right_array, self.Root, False)

    def gen_tree(self, array, parent, is_left_child):
        array_length = len(array)
        if array_length == 0:
            return

        if array_length == 1:
            node = BSTNode(array[0], parent)
            node.Level = parent.Level + 1
            self.assign_child(parent, node, is_left_child)
            return

        mid = array_length // 2

        node = BSTNode(array[mid], parent)
        node.Level = parent.Level + 1
        self.assign_child(parent, node, is_left_child)

        left_array = array[0:mid]
        right_array = array[mid+1:]

        self.gen_tree(left_array, node, True)
        self.gen_tree(right_array, node, False)

    def assign_child(self, node, child_node, is_left_child):
        if is_left_child:
            node.LeftChild = child_node
        else:
            node.RightChild = child_node

    def IsBalanced(self, root_node):
        if root_node is None:
            return False

        left = self.find_last_level(root_node.LeftChild, root_node.Level)
        right = self.find_last_level(root_node.RightChild, root_node.Level)

        return abs(left-right) < 2

    def find_last_level(self, node, last_val):
        if node is None:
            return last_val

        left = self.find_last_level(node.LeftChild, node.Level)
        right = self.find_last_level(node.RightChild, node.Level)

        return max(left, right)
