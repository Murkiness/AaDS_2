import pytest

from even_tree import SimpleTreeNode, SimpleTree


def test_EvenTree():
    a = SimpleTreeNode('23', None)
    b = SimpleTreeNode('14', None)
    c = SimpleTreeNode('15', None)
    d = SimpleTreeNode('19', None)
    e = SimpleTreeNode('209', None)
    f = SimpleTreeNode('1', None)
    g = SimpleTreeNode('91', None)
    h = SimpleTreeNode('19', None)
    m = SimpleTreeNode('69', None)
    r = SimpleTreeNode('0', None)

    st = SimpleTree(r)
    st.AddChild(a, b)
    st.AddChild(c, d)
    st.AddChild(r, a)
    st.AddChild(r, c)
    st.AddChild(r, h)
    st.AddChild(h, m)
    st.AddChild(a, e)
    st.AddChild(b, f)
    st.AddChild(c, g)

    assert st.EvenTrees() == [r, a, r, h, a, b]

    st.DeleteNode(m)

    assert st.GetAllNodes() == [r, a, c, h, b, e, d, g, f, ]
    assert st.EvenTrees() == []

    st.DeleteNode(f)
    assert st.GetAllNodes() == [r, a, c, h, b, e, d, g]
    assert st.EvenTrees() == []

    st.DeleteNode(e)
    st.DeleteNode(d)
    assert st.GetAllNodes() == [r, a, c, h, b, g]
    assert st.EvenTrees() == [r, a, r, c]

    st.DeleteNode(c)
    st.DeleteNode(g)
    assert st.GetAllNodes() == [r, a, h, b]
    assert st.EvenTrees() == [r, a]

    st_1 = SimpleTree(None)
    assert st_1.EvenTrees() == []
    assert st_1.Count() == 0
