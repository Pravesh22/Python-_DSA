"""
--Created by Pravesh Budhathoki
--Created on 2022-06-27
"""


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr


if __name__ == '__main__':
    sorted_arr = insertion_sort([31, 41, 59, 26, 41, 58])
    print(sorted_arr)
