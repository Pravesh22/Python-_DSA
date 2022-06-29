"""
--Created by Pravesh Budhathoki
--Created on 2022-06-29 
"""

"""Worst Time complexity O(n * n)"""


def bubble_sort(arr):
    n = len(arr) - 1
    flag = False
    while not flag:
        flag = True
        for i in range(n):
            if arr[i] > arr[i + 1]:
                flag = False
                arr[i + 1], arr[i] = arr[i], arr[i + 1]
    return arr


if __name__ == '__main__':
    sorted_arr = bubble_sort([31, 41, 59, 26, 41, 58])
    print(sorted_arr)
