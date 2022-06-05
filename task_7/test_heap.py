import pytest


from heap import Heap


def test_MakeHeap():
    h = Heap()
    h.MakeHeap([1, 2 ,3, 5, 10], 2)

    assert h.HeapArray == [10, 5, 2, 1, 3, None, None]

def test_GetMax():
    h = Heap()
    h.MakeHeap([1, 2 ,3, 5, 10], 2)

    assert 10 == h.GetMax()
    assert h.HeapArray == [5, 3, 2, 1, None, None, None]

    for i in [5, 3, 2, 1, -1]:
        assert i == h.GetMax()

