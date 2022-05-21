class BSTNode:
	
    def __init__(self, key, val, parent):
        self.NodeKey = key # ключ узла
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок


class BSTFind: # промежуточный результат поиска

    def __init__(self):
        self.Node = None # None если 
        # в дереве вообще нету узлов

        self.NodeHasKey = False # True если узел найден
        self.ToLeft = False # True, если родительскому узлу надо 
        # добавить новый узел левым потомком

    def set_values(self, node, has_key = False, to_left = False):
        self.Node = node
        self.NodeHasKey = has_key
        self.ToLeft = to_left

class BST:

    def __init__(self, node):
        self.Root = node # корень дерева, или None

    def FindNodeByKey(self, key):
        if self.Root is None:
            return BSTFind()

        return self.search_node(key, self.Root)

    def search_node(self, key, current_node):
        left_is_none = current_node.LeftChild is None
        right_is_none = current_node.RightChild is None
        is_bigger = current_node.NodeKey > key

        if current_node.NodeKey == key:
            return self.produce_search_result(current_node, True, False)
        elif is_bigger and left_is_none:
            return self.produce_search_result(current_node, False, True)
        elif is_bigger:
            return self.search_node(key, current_node.LeftChild)
        elif right_is_none:
            return self.produce_search_result(current_node, False, False)
        else:
            return self.search_node(key, current_node.RightChild)

    def produce_search_result(self, node, has_key, to_left):
        result = BSTFind()
        result.set_values(node, has_key, to_left)
        return result

    def AddKeyValue(self, key, val):
        search_res = self.FindNodeByKey(key)
        if search_res.NodeHasKey:
            return False

        if self.Root:
            new_node = BSTNode(key, val, None)
            if search_res.ToLeft:
                search_res.Node.LeftChild = new_node
            else:
                search_res.Node.RightChild = new_node

            new_node.Parent = search_res.Node
        else:
            self.Root = BSTNode(key, val, None)

        return True

    def FinMinMax(self, FromNode, FindMax):
        if FromNode is None:
            return BSTFind()

        if FindMax:
            max_key = self.get_last_right(FromNode)
            return self.FindNodeByKey(max_key)

        min_key = self.get_last_left(FromNode)
        return self.FindNodeByKey(min_key)

    def get_last_left(self, node):
        if node.LeftChild is None:
            return node.NodeKey
        return self.get_last_left(node.LeftChild)

    def get_last_right(self, node):
        if node.RightChild is None:
            return node.NodeKey
        return self.get_last_right(node.RightChild)

    def DeleteNodeByKey(self, key):
        search_res = self.FindNodeByKey(key)
        if not search_res.NodeHasKey:
            return False

        target_node = search_res.Node
        if target_node is self.Root:
            self.delete_root()
            return True

        left_child = target_node.LeftChild
        right_child = target_node.RightChild
        left_is_none = left_child is None
        right_is_none = right_child is None
        parent = None if target_node is self.Root else target_node.Parent
        is_left_child = parent.LeftChild is target_node

        if left_is_none and not right_is_none:
            self.add_new_child_to_parent(right_child, parent, is_left_child)
        elif not left_is_none and right_is_none:
            self.add_new_child_to_parent(left_child, parent, is_left_child)
        elif left_is_none and right_is_none:
            self.add_new_child_to_parent(None, parent, is_left_child)
        else:
            substitution_node = self.FinMinMax(right_child, False).Node
            self.add_new_child_to_parent(substitution_node, parent, is_left_child)

        return True

    def add_new_child_to_parent(self, child, parent, is_left_child):
        if is_left_child:
            parent.LeftChild = child
        else:
            parent.RightChild = child

    def delete_root(self):
        left_child = self.Root.LeftChild
        right_child = self.Root.RightChild
        left_is_none = left_child is None
        right_is_none = right_child is None

        if left_is_none and right_is_none:
            self.Root = None
        elif right_is_none:
            self.Root = left_child
        elif left_is_none:
            self.Root = right_child
        else:
            substitution_node = self.FinMinMax(right_child, False).Node
            self.Root = substitution_node

    def Count(self):
        if self.Root is None:
            return 0

        return self.count_node(self.Root)

    def count_node(self, node):
        if node is None:
            return 0

        return 1 + self.count_node(node.LeftChild) + self.count_node(node.RightChild)
