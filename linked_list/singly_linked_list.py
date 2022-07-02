"""
--Created by Pravesh Budhathoki
--Created on 2022-07-02 
"""


class Node:
    def __init__(self, data, pointer):
        self.data = data
        self.next = pointer


class Singly_Linked_List:
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


if __name__ == '__main__':
    singly_linked_list = Singly_Linked_List()
    singly_linked_list.insert_values([12, 13, 14, 2, 3])
    print("Original Linked List: ", singly_linked_list.print())

    singly_linked_list.remove_at(2)
    print("Removed at index 2 in Linked List: ", singly_linked_list.print())

    singly_linked_list.insert_at(2, 14)
    print("Insert at index 2 in Linked List: ", singly_linked_list.print())

    print("Length of linked list: ", singly_linked_list.get_length())
