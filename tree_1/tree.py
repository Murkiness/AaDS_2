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

    def GetAllNodes(self):
        collection = []
        self.collect_nodes(self.Root, collection)
        return collection

    def collect_nodes(self, node, collection):
        collection.append(node)

        if node.Children == []:
            return

        for n in node.Children:
            self.collect_nodes(n, collection)

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

    def Count(self):
        return len(self.GetAllNodes())

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