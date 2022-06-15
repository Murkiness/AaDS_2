from weak_vertices import SimpleGraph


def test_WeakVertices():
    g = SimpleGraph(6)

    for i in range(6):
        g.AddVertex(i)

    g.AddEdge(0, 1)
    g.AddEdge(0, 2)
    g.AddEdge(1, 2)
    g.AddEdge(1, 3)
    g.AddEdge(2, 3)
    g.AddEdge(2, 5)
    g.AddEdge(3, 4)
    g.AddEdge(4, 5)

    res = g.WeakVertices()
    values = []
    for v in res:
        values.append(v.Value)

    values.sort()

    assert values == [4, 5]


def test_WeakVertices_deficiency():
    g = SimpleGraph(2)

    for i in range(2):
        g.AddVertex(i)

    res = g.WeakVertices()
    values = []
    for v in res:
        values.append(v.Value)

    assert values == [0, 1]