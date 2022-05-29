def GenerateBBSTArray(a):
    if a == [] or a is None:
        return None

    a.sort()
    new_array = [None] * len(a)
    mid = len(a) // 2

    mid_element = a[mid]
    new_array[0] = mid_element

    left_array = a[0:mid]
    right_array = a[mid+1:]

    build_tree(left_array, new_array, 1)
    build_tree(right_array, new_array, 2)

    return new_array


def build_tree(orig_array, new_array, current_index):
    orig_length = len(orig_array)
    if orig_length == 0:
        return

    if orig_length == 1:
        new_array[current_index] = orig_array[0]
        return

    mid = orig_length // 2
    new_array[current_index] = orig_array[mid]
    left_array = orig_array[0:mid]
    right_array = orig_array[mid+1:]

    build_tree(left_array, new_array, 2 * current_index + 1)
    build_tree(right_array, new_array, 2 * current_index + 2)
