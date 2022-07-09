"""
--Created by Pravesh Budhathoki
--Created on 2022-07-09 
"""

"""Basic function to calculate sum numbers using recursion approach"""


def calculate_sum(number):
    if number == 1:
        return 1
    return number + calculate_sum(number - 1)


if __name__ == '__main__':
    print(calculate_sum(6))
