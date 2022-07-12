"""
--Created by Pravesh Budhathoki
--Created on 2022-07-12 
"""
"""Binary Search Tree must have at most 2 child nodes and doesn't allow duplication of elements in tree"""


class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            # add in left node of tree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTree(data)

        else:
            # add in right node of tree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTree(data)

    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements


def build_tree(elements):
    root = BinaryTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers = [20, 88, 23, 15, 7, 14, 27, 12]
    binary_tree = build_tree(numbers)
    print(binary_tree.search(88))
