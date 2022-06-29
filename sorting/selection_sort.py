"""
--Created by Pravesh Budhathoki
--Created on 2022-06-27 
"""

"""Worst Time complexity O(n * n)"""


def selection_sort(arr):
    n = len(arr) - 1

    for i in range(n):
        min_val_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_val_index]:
                min_val_index = j

        if min_val_index != i:
            arr[min_val_index], arr[i] = arr[i], arr[min_val_index]
    return arr


if __name__ == '__main__':
    sorted_arr = selection_sort([31, 41, 59, 26, 41, 58])
    print(sorted_arr)
