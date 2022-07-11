"""
--Created by Pravesh Budhathoki
--Created on 2022-07-11 
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    # calling print_tree function recursively to print all nodes of the tree
    def print_tree(self):
        root_node = self.data
        spaces = " " * self.get_node_level() * 2 + "-->" if self.parent else ""
        print(spaces + root_node)
        if self.children:
            for child in self.children:
                child.print_tree()

    # this function returns the level of node in tree
    def get_node_level(self):
        level = 0
        _parent = self.parent
        while _parent:
            level += 1
            _parent = _parent.parent
        return level


def build_tree():
    root = TreeNode("Asia")

    nepal_country = TreeNode("Nepal")
    nepal_country.add_child(TreeNode("Kathmandu"))
    nepal_country.add_child(TreeNode("Pokhara"))
    nepal_country.add_child(TreeNode("Patan"))

    india_country = TreeNode("India")
    india_country.add_child(TreeNode("Mumbai"))
    india_country.add_child(TreeNode("Goa"))
    india_country.add_child(TreeNode("Delhi"))

    china_country = TreeNode("China")
    china_country.add_child(TreeNode("Beijing"))
    china_country.add_child(TreeNode("Yunnan"))
    china_country.add_child(TreeNode("Shanghai"))

    root.add_child(nepal_country)
    root.add_child(india_country)
    root.add_child(china_country)
    return root


if __name__ == '__main__':
    tree = build_tree()
    tree.print_tree()
