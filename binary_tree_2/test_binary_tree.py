import pytest

from binary_tree import BSTNode, BSTFind, BST


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
    

def test_FindNodeByKey_no_root():
    bst = BST(None)
    expected_res = BSTFind()

    assert bst.FindNodeByKey(5).Node == expected_res.Node


def test_FindNodeByKey_found_key():
    test_data = _test_data()
    tree = test_data['tree']
    expected_node = test_data['node20']
    assert tree.FindNodeByKey(20).Node is expected_node

    expected_node1 = test_data['node25']
    res = tree.FindNodeByKey(25)
    assert res.Node is expected_node1
    assert res.NodeHasKey
    assert not res.ToLeft

    expected_node2 = test_data['root']
    assert tree.FindNodeByKey(5).Node == expected_node2


def test_FindNodeByKey_not_found_key():
    test_data = _test_data()
    tree = test_data['tree']
    expected_node = test_data['node20']
    res = tree.FindNodeByKey(18)
    assert res.Node == expected_node
    assert not res.NodeHasKey
    assert res.ToLeft

    expected_node1 = test_data['node8']
    res = tree.FindNodeByKey(9)
    assert res.Node == expected_node1
    assert not res.NodeHasKey
    assert not res.ToLeft


def test_AddKeyValue_existing():
    test_data = _test_data()
    tree = test_data['tree']

    assert tree.AddKeyValue(20, "20") == False
    assert tree.AddKeyValue(5, "5") == False
    assert tree.AddKeyValue(25, "25") == False


def test_AddKeyValue_new():
    test_data = _test_data()
    tree = test_data['tree']

    # add left
    expected_parent = test_data['node20']
    res = tree.FindNodeByKey(18)
    assert not res.NodeHasKey
    assert tree.AddKeyValue(18, "18")
    res = tree.FindNodeByKey(18)
    assert res.NodeHasKey
    assert res.Node.Parent is expected_parent

    # add right
    expected_parent = test_data['node8']
    res = tree.FindNodeByKey(9)
    assert not res.NodeHasKey
    assert tree.AddKeyValue(9, "9")
    res = tree.FindNodeByKey(9)
    assert res.NodeHasKey
    assert res.Node.Parent is expected_parent


def test_Count():
    test_data = _test_data()
    tree = test_data['tree']

    assert tree.Count() == 9


def test_FinMinMax_from_none():
    tree = BST(None)
    res = tree.FinMinMax(None, False)
    assert res is None
    res = tree.FinMinMax(None, True)
    assert res is None


def test_FinMinMax_from_root():
    test_data = _test_data()
    tree = test_data['tree']

    expected_max = test_data['node25']
    expected_min = test_data['node2']

    assert tree.FinMinMax(tree.Root, True) is expected_max
    assert tree.FinMinMax(tree.Root, False) is expected_min


def test_FinMinMax_from_root_2_only_left():
    test_data = _test_data()
    tree = test_data['tree']
    tree.Root.RightChild = None

    expected_max = test_data['root']
    expected_min = test_data['node2']

    assert tree.FinMinMax(tree.Root, True) is expected_max
    assert tree.FinMinMax(tree.Root, False) is expected_min


def test_FinMinMax_from_root_2_only_right():
    test_data = _test_data()
    tree = test_data['tree']
    tree.Root.LeftChild = None

    expected_max = test_data['node25']
    expected_min = test_data['root']

    assert tree.FinMinMax(tree.Root, True) is expected_max
    assert tree.FinMinMax(tree.Root, False) is expected_min


def test_FinMinMax_from_root_2_no_children():
    test_data = _test_data()
    tree = test_data['tree']
    tree.Root.LeftChild = None
    tree.Root.RightChild = None

    expected = test_data['root']

    assert tree.FinMinMax(tree.Root, True) is expected
    assert tree.FinMinMax(tree.Root, False) is expected


def test_FinMinMax_from_node():
    test_data = _test_data()
    tree = test_data['tree']
    start_node = test_data['node3']

    expected_max = test_data['node4']
    expected_min = test_data['node2']

    assert tree.FinMinMax(start_node, True) is expected_max
    assert tree.FinMinMax(start_node, False) is expected_min


def test_FinMinMax_from_node_2():
    test_data = _test_data()
    tree = test_data['tree']

    # only left child
    start_node = test_data['node8']
    expected_max = test_data['node8']
    expected_min = test_data['node7']

    assert tree.FinMinMax(start_node, True) is expected_max
    assert tree.FinMinMax(start_node, False) is expected_min

    # only right child
    start_node = test_data['node20']
    expected_max = test_data['node25']
    expected_min = test_data['node20']

    assert tree.FinMinMax(start_node, True) is expected_max
    assert tree.FinMinMax(start_node, False) is expected_min


def test_FinMinMax_from_leaf():
    test_data = _test_data()
    tree = test_data['tree']

    node4 = test_data['node4']
    assert tree.FinMinMax(node4, True) is node4
    assert tree.FinMinMax(node4, False) is node4


def test_DeleteNodeByKey_non_existing():
    test_data = _test_data()
    tree = test_data['tree']

    assert tree.DeleteNodeByKey(88) == False


def test_DeleteNodeByKey_existing():
    test_data = _test_data()
    tree = test_data['tree']

    node_to_delete = test_data['node16']
    res = tree.FindNodeByKey(16)
    assert res.Node is node_to_delete
    assert res.NodeHasKey

    assert tree.DeleteNodeByKey(16)
    res = tree.FindNodeByKey(16)
    assert res.Node is not node_to_delete
    assert not res.NodeHasKey
    assert res.Node.NodeKey == 8


def test_DeleteNodeByKey_existing_2():
    test_data = _test_data()
    tree = test_data['tree']
    node_to_delete = test_data['node25']
    res = tree.FindNodeByKey(25)
    assert res.Node is node_to_delete
    assert res.NodeHasKey

    assert tree.DeleteNodeByKey(25)
    res = tree.FindNodeByKey(25)
    assert res.Node is not node_to_delete
    assert not res.NodeHasKey
    assert node_to_delete.RightChild is None


def test_DeleteNodeByKey_remove_root():
    test_data = _test_data()
    tree = test_data['tree']

    node_to_delete = test_data['root']
    res = tree.FindNodeByKey(5)
    assert res.Node is node_to_delete
    assert res.NodeHasKey

    assert tree.DeleteNodeByKey(5)
    res = tree.FindNodeByKey(5)
    assert res.Node is not node_to_delete
    assert not res.NodeHasKey
    assert tree.Count() == 8


def test_DeleteNodeByKey_remove_root_only_left():
    test_data = _test_data()
    tree = test_data['tree']
    new_root = test_data['node3']
    node_to_delete = test_data['root']
    node_to_delete.RightChild = None

    assert tree.DeleteNodeByKey(5)
    assert tree.Root is new_root


def test_DeleteNodeByKey_remove_root_only_right():
    test_data = _test_data()
    tree = test_data['tree']
    new_root = test_data['node7']
    node_to_delete = test_data['root']
    node_to_delete.LeftChild = None

    assert tree.DeleteNodeByKey(5)
    print(tree.Root.NodeKey)
    assert tree.Root is new_root


def test_DeleteNodeByKey_remove_root_no_children():
    test_data = _test_data()
    tree = test_data['tree']
    node_to_delete = test_data['root']
    node_to_delete.LeftChild = None
    node_to_delete.RightChild = None

    assert tree.DeleteNodeByKey(5)
    assert tree.Root is None