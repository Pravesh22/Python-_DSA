"""
--Created by Pravesh Budhathoki
--Created on 2022-07-02 
"""


class Node:
    def __init__(self, data, pointer):
        self.data = data
        self.next = pointer


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, self.head)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def print(self):
        temp = self.head
        _list = ""
        while temp:
            _list += str(temp.data) + '-->'
            temp = temp.next
        return _list

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        temp = self.head

        if index == 0:
            self.head = temp.next
            return

        count = 0
        while temp:
            if count == index - 1:
                temp.next = temp.next.next
                break
            temp = temp.next
            count += 1

    def insert_at(self, index, value):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(value)

        count = 0
        temp = self.head
        while temp:
            if count == index - 1:
                node = Node(value, temp.next)
                temp.next = node
                break
            temp = temp.next
            count += 1

    # reverse the linked list
    def reverse_list(self):
        if self.head is None:
            raise Exception("Null list cannot be reversed")

        current_node = self.head
        count = 0
        while current_node.next:
            temp_node = current_node.next
            if count == 0:
                current_node.next = None
            else:
                current_node.next = self.head
                self.head = current_node
            current_node = temp_node
            count += 1
        current_node.next = self.head
        self.head = current_node

    # Exercise

    """if given data is present in the linked list then it will insert the requested data_to_insert after the 
    data_after node """

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        temp_len = self.get_length()
        while itr:
            if data_after == itr.data:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next

        if temp_len == self.get_length():
            print("Insertion failed.Given data doesn't exist in Linked List")
        else:
            print(f"Insertion successful after {data_after} value in linked_list")

    """remove the node of the linked list if the given data is present in the linked list"""

    def remove_by_value(self, data):
        itr = self.head
        while itr:
            if data == itr.next.data:
                itr.next = itr.next.next
                break
            itr = itr.next


if __name__ == '__main__':
    singly_linked_list = SinglyLinkedList()
    singly_linked_list.insert_values([12, 13, 14, 2, 3])
    print("Original Linked List: ", singly_linked_list.print())

    singly_linked_list.remove_at(2)
    print("Removed at index 2 in Linked List: ", singly_linked_list.print())

    singly_linked_list.insert_at(2, 14)
    print("Insert at index 2 in Linked List: ", singly_linked_list.print())

    print("Length of linked list: ", singly_linked_list.get_length())

    singly_linked_list.insert_after_value(13, 20)
    print("Insert after value 13 in Linked List: ", singly_linked_list.print())

    singly_linked_list.remove_by_value(20)
    print("Remove after value 20 in Linked List: ", singly_linked_list.print())
    singly_linked_list.reverse_list()
    print("After reversing linked list: ", singly_linked_list.print())
