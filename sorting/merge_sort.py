"""
--Created by Pravesh Budhathoki
--Created on 2022-06-29 
"""

"""Worst Time complexity O(n log n)"""

def merge_sort(_arr):
    if len(_arr) <= 1:
        return

    mid = len(_arr)//2

    left = _arr[:mid]
    right = _arr[mid:]

    """recursively calling merge_sort function to divide elements of list in single sorted list"""
    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_list(left, right, _arr)


def merge_two_sorted_list(list_a, list_b, _arr):
    len_a = len(list_a)
    len_b = len(list_b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if list_a[i] <= list_b[j]:
            _arr[k] = list_a[i]
            i += 1
        else:
            _arr[k] = list_b[j]
            j += 1
        k += 1

    """calling this code to compute last index element of sub-sorted list"""
    while i < len_a:
        _arr[k] = list_a[i]
        i += 1
        k += 1
    while j < len_b:
        _arr[k] = list_b[j]
        j += 1
        k += 1


if __name__ == '__main__':
    arr = [3, 2, 5, 4, 8, 9, 7, 0, 1]
    merge_sort(arr)
    print(arr)
