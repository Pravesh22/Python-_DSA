"""
--Created by Pravesh Budhathoki
--Created on 2022-07-11 
"""

"""For question please go to 
https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/7_Tree/7_tree_exercise.md"""


# Question Number 2 Solution
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, level):
        if self.get_node_level() > level:
            return
        root_node = self.data
        string = " " * self.get_node_level() * 2 + f"|__{root_node}" if self.parent else f"{root_node}"
        print(string)
        for child in self.children:
            child.print_tree(level)

    def get_node_level(self):
        level = 0
        parent_node = self.parent
        while parent_node:
            parent_node = parent_node.parent
            level += 1
        return level


def build_location_tree():
    root_node = TreeNode("Global")

    india_node = TreeNode("India")
    gujarat_node = TreeNode("Gujarat")
    gujarat_node.add_child(TreeNode("Ahmedabad"))
    gujarat_node.add_child(TreeNode("Baroda"))
    karnataka_node = TreeNode("Karnataka")
    karnataka_node.add_child(TreeNode("Bangluru"))
    karnataka_node.add_child(TreeNode("Mysore"))
    india_node.add_child(gujarat_node)
    india_node.add_child(karnataka_node)

    usa_node = TreeNode("USA")
    new_jersey_node = TreeNode("New Jersey")
    new_jersey_node.add_child(TreeNode("Princeton"))
    new_jersey_node.add_child(TreeNode("Trenton"))
    california_node = TreeNode("California")
    california_node.add_child(TreeNode("San Francisco"))
    california_node.add_child(TreeNode("Mountain View"))
    california_node.add_child(TreeNode("Palo Alto"))
    usa_node.add_child(new_jersey_node)
    usa_node.add_child(california_node)

    root_node.add_child(india_node)
    root_node.add_child(usa_node)
    return root_node


if __name__ == '__main__':
    tree = build_location_tree()
    tree.print_tree(0)
    tree.print_tree(1)
    tree.print_tree(2)
    tree.print_tree(3)


