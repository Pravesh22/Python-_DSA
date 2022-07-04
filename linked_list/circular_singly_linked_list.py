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
            new_node.next_node = self.head
            self.tail = new_node
            return

    def print(self):
        current_node = self.head
        _list = ""
        while current_node.next_node:
            _list += str(current_node.data) + '-->'
            current_node = current_node.next_node
            if current_node == self.head:
                break
        return _list

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next_node
            if itr == self.head:
                break
        return count

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

    def insert_at(self, index, data):
        self.check_index(index)

        # Inserting while index is in range from 0 to length of list
        if index == 0:
            self.insert_at_beginning(data)
        elif index == self.get_length() - 1:
            self.insert_at_end(data)
        else:
            current_node = self.head
            count = 0
            while current_node:
                if count == index - 1:
                    new_node = Node(data)
                    new_node.next_node = current_node.next_node
                    current_node.next_node = new_node
                    break
                count += 1
                current_node = current_node.next_node

    def remove_by_index(self, index):
        self.check_index(index)
        current_node = self.head
        if index == 0:
            self.tail.next_node = current_node.next_node
            self.head = current_node.next_node
        elif index == self.get_length() - 1:
            count = 0
            while current_node:
                if count == index - 1:
                    current_node.next_node = self.head
                    break
                count += 1
                current_node = current_node.next_node
        else:
            count = 0
            while current_node:
                if count == index - 1:
                    current_node.next_node = current_node.next_node.next_node
                    break
                count += 1
                current_node = current_node.next_node

    def check_index(self, index):
        # Check if index given is greater than length of linked list
        if index > self.get_length() - 1:
            raise Exception("Index out of range.")

        # Raise exception if list is empty
        if self.head is None:
            raise Exception("Cannot insert element in empty list. Create list first")


if __name__ == '__main__':
    csll = CircularSinglyLinkedList()
    csll.insert_at_beginning(10)
    csll.insert_at_beginning(1)
    csll.insert_at_beginning(55)

    csll.insert_at_end(22)
    csll.insert_at_end(44)
    csll.insert_at_end(66)
    print("Original items in circular singly linked list", csll.print())
    csll.insert_at(4, 111)
    print("After insertion at index 4:", csll.print())
    csll.remove_by_index(0)
    print("After removing item 55 from first index 0:", csll.print())
    csll.remove_by_index(5)
    print("After removing item 66 from last index 5:", csll.print())
    csll.remove_by_index(3)
    print("After removing random item at middle index 3:", csll.print())
