import pytest

from dfs import SimpleGraph


def test_dfs_no_path():
    g = SimpleGraph(4)
    g.AddVertex(7)
    g.AddVertex(8)
    g.AddVertex(9)
    g.AddEdge(0, 1)

    assert g.DepthFirstSearch(0, 2) == []


def test_dfs_path():
    g = SimpleGraph(4)
    g.AddVertex(7)
    g.AddVertex(8)
    g.AddVertex(9)
    g.AddVertex(7)

    g.AddEdge(0, 1)
    g.AddEdge(0, 2)
    g.AddEdge(2, 3)

    arr = g.vertex
    expected = [arr[0], arr[2], arr[3]]

    assert  g.DepthFirstSearch(0, 3) == expected
    assert  g.DepthFirstSearch(0, 3) == expected