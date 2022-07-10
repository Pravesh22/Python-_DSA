"""
--Created by Pravesh Budhathoki
--Created on 2022-07-10 
"""

"""In this exercise the input string is reversed using stack implementation.
Stack is implemented using "deque" function from python collections """
from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, item):
        return self.container.append(item)

    def pop(self):
        return self.container.pop()

    def is_empty(self):
        return len(self.container) == 0

    def is_not_empty(self):
        return len(self.container) != 0

    def size(self):
        return len(self.container)


def reverse_string(_stack, string):
    reversed_string = ""
    for s in string:
        _stack.push(s)

    while _stack.is_not_empty():
        pop_item = _stack.pop()
        reversed_string += pop_item
    return reversed_string


if __name__ == '__main__':
    stack = Stack()
    print(reverse_string(stack, "We will conquere COVID-19"))
