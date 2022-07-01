"""
--Created by Pravesh Budhathoki
--Created on 2022-06-30 
"""


def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]


"""this code is used for swap down the elements of nodes if child is greater than parent and changes the input array 
where the greatest number is in root position of node i.e.(first index in array) """


def down_shift(arr, node, upper_bound):
    while True:
        l_child = 2 * node + 1
        r_child = 2 * node + 2

        if max(l_child, r_child) < upper_bound:
            if arr[node] >= max(arr[l_child], arr[r_child]):
                break
            elif arr[l_child] > arr[r_child]:
                swap(arr, node, l_child)
                node = l_child
            elif arr[r_child] > arr[l_child]:
                swap(arr, node, r_child)
                node = r_child
            else:
                break
        elif l_child < upper_bound:
            if arr[l_child] >= arr[node]:
                swap(arr, node, l_child)
                node = l_child
            else:
                break
        elif r_child < upper_bound:
            if arr[r_child] > arr[node]:
                swap(arr, node, r_child)
                node = r_child
            else:
                break
        else:
            break


def heap_sort(arr):
    n = len(arr)
    internal_nodes = (n // 2) - 1

    """this line process the nodes and fix the largest number in the node to root node 
    i.e. greatest number of list comes to index 0 of list"""
    for _node in range(internal_nodes, -1, -1):
        down_shift(arr, _node, len(arr))

    """this code swap the position of largest number from 0 index to last index and process remaining nodes for same 
    recursion task """
    for j in range(n - 1, 0, -1):
        swap(arr, 0, j)
        down_shift(arr, 0, j)
    return arr


if __name__ == '__main__':
    unsorted_list = [5, 3, 6, 8, 0, 1, 2, 4]
    print(heap_sort(unsorted_list))
