import pytest

from task_3 import BSTNode, BSTFind, BST


def _test_data():
    root = BSTNode(5, "5", None)
    bst = BST(root)

    node3 = BSTNode(3, "3", root)
    node16 = BSTNode(16, "16", root)
    root.LeftChild = node3
    root.RightChild = node16

    node2 = BSTNode(2, "2", node3)
    node4 = BSTNode(4, "4", node3)
    node3.LeftChild = node2
    node3.RightChild = node4

    node8 = BSTNode(8, "8", node16)
    node20 = BSTNode(20, "20", node16)
    node16.LeftChild = node8
    node16.RightChild = node20

    node7 = BSTNode(7, "7", node8)
    node8.LeftChild = node7

    node25 = BSTNode(25, "25", node20)
    node20.RightChild = node25

    return {
        'root': root,
        'tree': bst,
        'node3': node3,
        'node2': node2,
        'node4': node4,
        'node16': node16,
        'node8': node8,
        'node7': node7,
        'node20': node20,
        'node25': node25
    }

def get_nodes_in_order(node_names, test_data):
    res = []
    for n in node_names:
        res.append(test_data[n])

    return tuple(res)


def test_WideAllNodes():
    test_data = _test_data()
    tree = test_data['tree']

    actual = tree.WideAllNodes()
    expected = get_nodes_in_order(['root', 'node3', 'node16', 'node2', 'node4', 'node8', 'node20', 'node7', 'node25'], test_data)
    assert actual == expected
    assert tree.Count() == 9

    tree.DeleteNodeByKey(16)
    expected = get_nodes_in_order(['root', 'node3', 'node20', 'node2', 'node4', 'node8',  'node7', 'node25'], test_data)
    assert tree.Count() == 8 == len(expected)


def test_WideAllNodes_empty():
    tree = BST(None)
    actual = tree.WideAllNodes()
    assert actual == tuple()


def test_DeepAllNodes_empty():
    tree = BST(None)
    for order in [0, 1, 2]:
        actual = tree.DeepAllNodes(order)
        assert actual == tuple()


def test_DeepAllNodes():
    test_data = _test_data()
    tree = test_data['tree']

    actual = tree.DeepAllNodes(0)
    expected = get_nodes_in_order(['node2', 'node3', 'node4', 'root', 'node7',  'node8', 'node16', 'node20', 'node25'], test_data)
    assert actual == expected

    actual1 = tree.DeepAllNodes(1)
    expected1 = get_nodes_in_order(['node2', 'node4', 'node3', 'node7',  'node8', 'node25', 'node20', 'node16', 'root'], test_data)
    assert actual1 == expected1

    actual2 = tree.DeepAllNodes(2)
    expected2 = get_nodes_in_order(['root', 'node3', 'node2', 'node4', 'node16', 'node8', 'node7', 'node20', 'node25'], test_data)
    assert actual2 == expected2