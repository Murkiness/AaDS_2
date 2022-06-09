class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.Children = [] # список дочерних узлов

class SimpleTree:

    def __init__(self, root):
        self.Root = root # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode

    def DeleteNode(self, NodeToDelete):
        if NodeToDelete is self.Root:
            return

        parent = NodeToDelete.Parent
        parent.Children.remove(NodeToDelete)
        NodeToDelete = None

    def GetAllNodes(self, root=None):
        if root is None:
            root = self.Root

        if root is None:
            return []

        nodes = []
        nodes.append(root)
        for node in nodes:
            nodes.extend(node.Children)

        return nodes

    def FindNodesByValue(self, val):
        all_nodes = self.GetAllNodes()
        nodes_w_value = []

        for n in all_nodes:
            if n.NodeValue == val:
                nodes_w_value.append(n)
        return nodes_w_value

    def MoveNode(self, OriginalNode, NewParent):
        parent = OriginalNode.Parent
        parent.Children.remove(OriginalNode)
        self.AddChild(NewParent, OriginalNode)

    def Count(self, root=None):
        if root is None:
            root = self.Root
        return len(self.GetAllNodes(root))

    def LeafCount(self):
        leafs = []
        self.collect_leafs(self.Root, leafs)
        return len(leafs)

    def collect_leafs(self, node, leafs):
        if node.Children == []:
            leafs.append(node)
            return

        for n in node.Children:
            self.collect_leafs(n, leafs)

    def set_levels(self):
        self.set_level_for_node(self.Root, -1)

    def set_level_for_node(self, node, parent_level):
        current_level = parent_level + 1
        node.level = current_level

        for n in node.Children:
            self.set_level_for_node(n, current_level)

    def EvenTrees(self):
        if self.Root is None or self.Count(self.Root) % 2 != 0 :
            return []

        split_nodes = []
        nodes = self.Root.Children.copy()
        for node in nodes:
            if self.Count(node) % 2 == 0:
                nodes.extend(node.Children)
                split_nodes.append(node.Parent)
                split_nodes.append(node)

        return split_nodes
