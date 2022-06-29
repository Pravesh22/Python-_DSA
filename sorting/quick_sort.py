"""
--Created by Pravesh Budhathoki
--Created on 2022-06-29 
"""

"""Worst Time Complexity O(n*n)
    Average Time Complexity O(n log n)"""


def quick_sort(arr):
    n = len(arr)

    if n <= 1:
        return arr
    else:
        pivot = arr.pop()

        greater_numbers = []
        smaller_numbers = []
        for number in arr:
            if number > pivot:
                greater_numbers.append(number)
            else:
                smaller_numbers.append(number)
    return quick_sort(smaller_numbers) + [pivot] + quick_sort(greater_numbers)


if __name__ == '__main__':
    sorted_arr = quick_sort([31, 41, 59, 26, 41, 58, 16, 27])
    print(sorted_arr)
