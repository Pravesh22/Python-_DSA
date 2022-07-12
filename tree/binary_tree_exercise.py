"""
--Created by Pravesh Budhathoki
--Created on 2022-07-12 
"""
"""The question of following code is available on:
https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/8_Binary_Tree_1/8_binary_tree_part_1_exercise.md"""

"""Exercise is to find_max(), find_min() elements from binary tree, calculate sum of elements in binary tree,
WAP for pre_order_traversal and post_order_traversal"""


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

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def calc_sum(self):
        if self.left:
            left_sum = self.left.calc_sum()
        else:
            left_sum = 0

        if self.right:
            right_sum = self.right.calc_sum()
        else:
            right_sum = 0

        return left_sum + right_sum + self.data

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements


def build_tree(elements):
    root = BinaryTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    binary_tree = build_tree(numbers)
    print("In order traversal: ", binary_tree.in_order_traversal())
    print("Pre order traversal: ", binary_tree.pre_order_traversal())
    print("Post order traversal: ", binary_tree.post_order_traversal())
    print("Maximum element of tree: ", binary_tree.find_max())
    print("Minimum element of tree: ", binary_tree.find_min())
    print("Sum of total elements of tree: ", binary_tree.calc_sum())
