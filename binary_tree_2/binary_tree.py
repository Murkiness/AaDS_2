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
            return None

        if FindMax:
            max_key = self.get_last_right(FromNode)
            return self.FindNodeByKey(max_key).Node

        min_key = self.get_last_left(FromNode)
        return self.FindNodeByKey(min_key).Node

    def get_last_left(self, node):
        if node.LeftChild is None:
            return node.NodeKey
        return self.get_last_left(node.LeftChild)

    def get_last_right(self, node):
        if node.RightChild is None:
            return node.NodeKey
        return self.get_last_right(node.RightChild)

    def DeleteNodeByKey(self, key):
        search_result = self.FindNodeByKey(key)
        if not search_result.NodeHasKey:
            return False

        removed_node = search_result.Node
        if removed_node.LeftChild and not removed_node.RightChild:
            new_node = removed_node.LeftChild
        else:
            new_node = self.FinMinMax(removed_node.RightChild, False)

        if removed_node is not self.Root:
            if removed_node.Parent.LeftChild == removed_node:
                removed_node.Parent.LeftChild = new_node
            else:
                removed_node.Parent.RightChild = new_node
        else:
            self.Root = new_node

        if removed_node.LeftChild and not removed_node.RightChild:
            removed_node.LeftChild.Parent = removed_node.Parent
            removed_node.LeftChild = None
        elif removed_node.RightChild:
            if removed_node.RightChild != new_node:
                if new_node.RightChild:
                    new_node.RightChild.Parent = new_node.Parent

                new_node.Parent.LeftChild = new_node.RightChild
                new_node.RightChild = removed_node.RightChild
                removed_node.RightChild.Parent = new_node

            if removed_node.LeftChild:
                removed_node.LeftChild.Parent = new_node
                new_node.LeftChild = removed_node.LeftChild

            new_node.Parent = removed_node.Parent
            removed_node.RightChild = None
            removed_node.LeftChild = None

        removed_node.Parent = None
        return True

    def Count(self):
        if self.Root is None:
            return 0

        return self.count_node(self.Root)

    def count_node(self, node):
        if node is None:
            return 0

        return 1 + self.count_node(node.LeftChild) + self.count_node(node.RightChild)
