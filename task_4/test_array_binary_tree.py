import pytest

from array_binary_tree import aBST


def test_FindKeyIndex_empty():
    tree = aBST(1)
    assert tree.FindKeyIndex(5) == 0


def test_FindKeyIndex_non_existing():
    tree = aBST(1)
    tree.Tree[0] = 5
    assert tree.FindKeyIndex(1) == -1
    assert tree.FindKeyIndex(6) == -2


def test_FindKeyIndex_existing():
    tree = aBST(1)
    tree.Tree[0] = 5
    tree.Tree[1] = 2
    tree.Tree[2] = 7
    assert tree.FindKeyIndex(5) == 0
    assert tree.FindKeyIndex(2) == 1
    assert tree.FindKeyIndex(7) == 2


def test_AddKey():
    tree = aBST(2)
    assert len(tree.Tree) == 7
    arr = [50, 25, 75, 100, 60, 15]

    for el in arr:
        tree.AddKey(el)

    assert tree.Tree == [50, 25, 75, 15, None, 60, 100]
    assert tree.FindKeyIndex(100) == 6
    assert tree.FindKeyIndex(15) == 3
    assert tree.FindKeyIndex(101) is None
    assert tree.AddKey(101) == -1
