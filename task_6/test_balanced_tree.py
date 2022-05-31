import pytest

from balanced_tree import BalancedBST


def test_GenerateTree():
    a = [500, 300, 25, 50, 75, 100, 200]

    tree = BalancedBST()
    tree.GenerateTree(a)

    assert tree.Root.NodeKey == 100
    l_c1 = tree.Root.LeftChild
    r_c1 = tree.Root.RightChild

    assert l_c1.NodeKey == 50
    assert r_c1.NodeKey == 300

    l_c2 = l_c1.LeftChild
    r_c2 = l_c1.RightChild

    l_c3 = r_c1.LeftChild
    r_c3 = r_c1.RightChild

    assert l_c2.NodeKey == 25
    assert r_c2.NodeKey == 75
    assert l_c3.NodeKey == 200
    assert r_c3.NodeKey == 500


def test_GenerateTree_empty():
    a = []
    tree = BalancedBST()
    tree.GenerateTree(a)

    assert tree.Root is None


def test_IsBalanced():
    a = [500, 300, 25, 50, 75, 100, 200]

    tree = BalancedBST()
    tree.GenerateTree(a)

    assert tree.IsBalanced(tree.Root)

    tree.Root.LeftChild = None
    assert not tree.IsBalanced(tree.Root)