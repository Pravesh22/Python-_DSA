"""
--Created by Pravesh Budhathoki
--Created on 2022-07-11 
"""

"""For question please go to 
https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/7_Tree/7_tree_exercise.md"""


# Question Number 1 Solution
class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, string):
        if string == "both":
            data = f"{self.name} ({self.designation})"
        elif string == "name":
            data = self.name
        else:
            data = self.designation
        spaces = " " * self.get_node_level() * 2 + f"|__{data}" if self.parent else f"{data}"
        print(spaces)
        if self.children:
            for child in self.children:
                child.print_tree(string)

    def get_node_level(self):
        level = 0
        _parent = self.parent
        while _parent:
            level += 1
            _parent = _parent.parent
        return level


def build_management_tree():
    root = TreeNode("Nilupul", "CEO")

    _chinmay = TreeNode("Chinmay", "CTO")
    _vishwa = TreeNode("Vishwa", "Infrastructure Head")
    _aamir = TreeNode("Aamir", "Application Head")
    _vishwa.add_child(TreeNode("Dhaval", "Cloud Manager"))
    _vishwa.add_child(TreeNode("Abhijit", "App Manager"))
    _chinmay.add_child(_vishwa)
    _chinmay.add_child(_aamir)

    _gels = TreeNode("Gels", "HR Head")
    _gels.add_child(TreeNode("Peter", "Recruitment Manager"))
    _gels.add_child(TreeNode("Waqas", "Policy Manager"))

    root.add_child(_chinmay)
    root.add_child(_gels)

    return root


if __name__ == '__main__':
    tree = build_management_tree()
    tree.print_tree("name") # prints only name hierarchy
    tree.print_tree("designation") # prints only designation hierarchy
    tree.print_tree("both") # prints both (name and designation) hierarchy
