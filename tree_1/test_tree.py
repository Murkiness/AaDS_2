import pytest

from tree import *

def _test_data():
    root = SimpleTreeNode(0, None)
    tree = SimpleTree(root)
    child1 = SimpleTreeNode(1, None)
    child2 = SimpleTreeNode(2, None)
    subchild1_1 = SimpleTreeNode(3, None)
    subchild1_2 = SimpleTreeNode(4, None)
    subchild2_1 = SimpleTreeNode(5, None)
    subchild2_2 = SimpleTreeNode(6, None)

    tree.AddChild(root, child1)
    tree.AddChild(root, child2)
    tree.AddChild(child1, subchild1_1)
    tree.AddChild(child1, subchild1_2)
    tree.AddChild(child2, subchild2_1)
    tree.AddChild(child2, subchild2_2)

    return {
        'root': root,
        'tree': tree,
        'child1': child1,
        'child2': child2,
        'subchild1_1': subchild1_1,
        'subchild1_2': subchild1_2,
        'subchild2_1': subchild2_1,
        'subchild2_2': subchild2_2
    }


def test_GetAllNodes():
    test_data = _test_data()
    tree = test_data['tree']

    assert [0, 1, 3, 4, 2, 5, 6] == [node.NodeValue for node in tree.GetAllNodes()]


def test_LeafCount():
    test_data = _test_data()
    tree = test_data['tree']

    assert(4 == tree.LeafCount())


def test_Count():
    test_data = _test_data()
    tree = test_data['tree']

    assert(7 == tree.Count())


def test_FindNodesByValue():
    test_data = _test_data()
    tree = test_data['tree']

    assert([test_data['child1']] == tree.FindNodesByValue(1))
    new_child = SimpleTreeNode(1, None)
    tree.AddChild(test_data['child1'], new_child)
    assert([test_data['child1'], new_child] == tree.FindNodesByValue(1))
    assert([test_data['subchild2_2']] == tree.FindNodesByValue(6))


def test_DeleteNode():
    test_data = _test_data()
    tree = test_data['tree']

    tree.DeleteNode(test_data['child1'])
    assert [0, 2, 5, 6] == [node.NodeValue for node in tree.GetAllNodes()]


def test_MoveNode():
    test_data = _test_data()
    tree = test_data['tree']

    tree.MoveNode(test_data['child1'], test_data['subchild2_2'])
    assert [0, 2, 5, 6, 1, 3, 4] == [node.NodeValue for node in tree.GetAllNodes()]


def test_set_levels():
    test_data = _test_data()
    tree = test_data['tree']

    tree.set_levels()
    assert [0, 1, 2, 2, 1, 2, 2] == [node.level for node in tree.GetAllNodes()]
