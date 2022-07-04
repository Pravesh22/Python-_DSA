"""
-- Created by Pravesh Budhathoki
-- Treeleaf Technologies Pvt. Ltd.
-- Created on 2022-07-04 
"""


class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class CircularSinglyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.head.next_node = new_node
            self.tail = new_node
            return

        if self.tail is not None:
            self.tail.next_node = new_node
            new_node.next_node= self.head
            self.tail = new_node
            return

    def print(self):
        current_node = self.head

        while current_node.next_node:
            print(current_node.data)
            current_node = current_node.next_node
            if current_node == self.head:
                break

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.head.next_node = new_node
            self.tail = new_node
            return

        if self.tail is not None:
            self.tail.next_node = new_node
            new_node.next_node = self.head
            self.head = new_node
            return


if __name__ == '__main__':
    csll = CircularSinglyLinkedList()
    csll.insert_at_beginning(10)
    csll.insert_at_beginning(1)
    csll.insert_at_beginning(55)

    csll.insert_at_end(22)
    csll.insert_at_end(44)
    csll.print()


