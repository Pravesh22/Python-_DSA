"""
--Created by Pravesh Budhathoki
--Created on 2022-07-06 
"""


class Node:
    def __init__(self, data, next_node=None, previous_node=None):
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node


class DoublyCircularLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.head.next_node = new_node
            self.head.previous_node = new_node
            self.tail = new_node
            return

        new_node.next_node = self.head
        new_node.previous_node = self.tail
        self.head.previous_node = new_node
        self.tail.next_node = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next_node = new_node
            self.head.previous_node = new_node
            self.tail = new_node
            return

        new_node.next_node = self.head
        new_node.previous_node = self.tail
        self.tail.next_node = new_node
        self.head.previous_node = new_node
        self.tail = new_node

    def insert_at_index(self, data, index):
        if self.head is None:
            raise Exception("List is empty. Create list first")

        if index > self.get_length() - 1:
            raise Exception("Index out of range of list!!!")

        if index == 0:
            self.insert_at_beginning(data)

        elif index == self.get_length() - 1:
            self.insert_at_end(data)

        else:
            count = 0
            current_node = self.head
            while current_node:
                if count == index - 1:
                    new_node = Node(data)
                    new_node.previous_node = current_node
                    new_node.next_node = current_node.next_node
                    current_node.next_node = new_node
                    break
                count += 1
                current_node = current_node.next_node

    def remove_at_beginning(self):
        if self.head is None:
            raise Exception("Item cannot be removed from empty list!!!")

        last_node = self.tail
        last_node.next_node = self.head.next_node
        self.head = self.head.next_node
        self.head.previous_node = last_node

    def remove_at_end(self):
        if self.head is None:
            raise Exception("Item cannot be removed from empty list!!!")

        self.head.previous_node = self.tail.previous_node
        self.tail = self.tail.previous_node
        self.tail.next_node = self.head

    def remove_at_index(self, index):
        if self.head is None:
            raise Exception("Item cannot be removed from empty list!!!")
        if index > self.get_length() - 1:
            raise Exception("Index out of range of list!!!")

        if index == 0:
            self.remove_at_beginning()

        elif index == self.get_length() - 1:
            self.remove_at_end()

        else:
            count = 0
            current_node = self.head
            while current_node:
                if count == index - 1:
                    current_node.next_node = current_node.next_node.next_node
                    current_node.next_node.previous_node = current_node
                    break
                count += 1
                current_node = current_node.next_node

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next_node
            if itr == self.head:
                break
        return count

    def print(self):
        current_node = self.head
        _list = ""
        while current_node:
            _list += str(current_node.data) + '-->'
            current_node = current_node.next_node
            if current_node == self.head:
                break
        return _list


if __name__ == '__main__':
    dcll = DoublyCircularLinkedList()
    dcll.insert_at_beginning(555)
    dcll.insert_at_beginning(222)
    dcll.insert_at_beginning(111)
    print(dcll.print())
    dcll.insert_at_end(333)
    dcll.insert_at_end(666)
    print("After inserting 333 and 666 at end:", dcll.print())
    dcll.insert_at_index(777, 3)
    print("Inserting 777 at index 3:", dcll.print())
    dcll.remove_at_beginning()
    print("Removing item from first index:", dcll.print())
    dcll.remove_at_end()
    print("Removing item from last index:", dcll.print())
    dcll.remove_at_index(2)
    print("Removing item from 2 index", dcll.print())
