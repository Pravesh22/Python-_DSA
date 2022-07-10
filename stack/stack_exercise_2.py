"""
--Created by Pravesh Budhathoki
--Created on 2022-07-10 
"""

"""In this exercise we are going to check whether 
the parenthesis is balanced in given string or not"""

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


def is_matched(str1, str2):
    match_parenthesis = {"}": "{", ")": "(", "]": "["}
    return match_parenthesis[str1] == str2


def check_balanced_parenthesis(_stack, string):
    for ch in string:
        if ch == "{" or ch == "(" or ch == "[":
            _stack.push(ch)
        if ch == "}" or ch == ")" or ch == "]":
            if _stack.size() == 0:
                return False
            if is_matched(ch, _stack.pop()):
                return True

    return _stack.size() == 0


if __name__ == '__main__':
    stack = Stack()
    print(check_balanced_parenthesis(stack, "({a+b})"))
