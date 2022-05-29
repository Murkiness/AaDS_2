import pytest


from balanced_binary_tree import GenerateBBSTArray


def test_balanced_tree():
    a = [500, 300, 25, 50, 75, 100, 200]
    res = GenerateBBSTArray(a)
    assert res == [100, 50, 300, 25, 75, 200, 500]


def test_balanced_tree_empty():
    a = []
    res = GenerateBBSTArray(a)
    assert res is None


def test_balanced_tree_2_elements():
    a = [100, 200]
    res = GenerateBBSTArray(a)
    assert res == [200, 100]