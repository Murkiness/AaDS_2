import pytest

from graph import SimpleGraph


def test_AddVertex():
    g = SimpleGraph(5)
    g.AddVertex(7)
    g.AddVertex(8)

    assert g.vertex[0].Value == 7
    assert g.vertex[1].Value == 8
    assert g.vertex[2] is None


def test_AddEdge():
    g = SimpleGraph(4)
    g.AddVertex(7)
    g.AddVertex(8)
    g.AddEdge(0, 1)

    for i in range(4):
        for j in range(4):
            if (i==0 and j==1) or (i==1 and j==0):
                assert g.m_adjacency[i][j] == 1
            else:
                assert g.m_adjacency[i][j] == 0


def test_IsEdge():
    g = SimpleGraph(4)
    g.AddVertex(7)
    g.AddVertex(8)
    g.AddEdge(0, 1)

    assert g.IsEdge(0, 1) == True
    assert g.IsEdge(0, 3) == False


def test_RemoveEdge():
    g = SimpleGraph(4)
    g.AddVertex(7)
    g.AddVertex(8)
    g.AddEdge(0, 1)

    assert g.IsEdge(0, 1) == True
    g.RemoveEdge(0, 1)
    assert g.IsEdge(0, 1) == False


def test_RemoveVertex():
    g = SimpleGraph(4)
    g.AddVertex(7)
    g.AddVertex(8)
    g.AddEdge(0, 1)

    g.RemoveVertex(0)
    assert g.IsEdge(0, 1) == False
    assert g.vertex[0] is None