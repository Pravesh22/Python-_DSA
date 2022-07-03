"""
--Created by Pravesh Budhathoki
--Created on 2022-07-03 
"""


class Node:
    def __init__(self, data, _next=None, _previous=None):
        self.data = data
        self.next = _next
        self.previous = _previous


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node
        else:
            node = Node(data, self.head)
            self.head.previous = node
            self.head = node

    def print_forward(self):
        if self.head is None:
            print("Linked List is empty")
            return
        temp = self.head
        _list = ""
        while temp:
            _list += str(temp.data) + '-->'
            temp = temp.next
        return _list

    def print_backward(self):
        if self.head is None:
            print("Linked List is empty")
            return

        temp_head = self.head
        while temp_head.next:
            temp_head = temp_head.next

        _list = ''
        while temp_head:
            _list += str(temp_head.data) + '-->'
            temp_head = temp_head.previous
        return _list

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node
            return

        temp_head = self.head

        while temp_head.next:
            temp_head = temp_head.next

        temp_head.next = Node(data, None, temp_head)

    def insert_at(self, data, index):
        if self.head is None:
            node = Node(data)
            self.head = node
            return

        if index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)

        else:
            count = 0
            temp_head = self.head

            while temp_head:
                if count == index - 1:
                    node = Node(data, temp_head.next, temp_head)
                    temp_head.next = node
                    break
                temp_head = temp_head.next
                count += 1

    def remove_at(self, index):
        if self.head is None:
            raise Exception("Linked List is Empty!!!!!!")
        temp_head = self.head

        if index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = temp_head.next

        count = 0
        while temp_head.next:
            if count == index - 1:
                temp_head.next = temp_head.next.next
                temp_head.next.previous = temp_head
                break
            count += 1
            temp_head = temp_head.next

    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next
        return count


if __name__ == '__main__':
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.insert_at_beginning(5)
    doubly_linked_list.insert_at_beginning(15)
    doubly_linked_list.insert_at_end(25)
    doubly_linked_list.insert_at_end(35)
    print("Linked List print in forward order: ", doubly_linked_list.print_forward())
    print("Linked List print in backward order: ", doubly_linked_list.print_backward())
    doubly_linked_list.insert_at(50, 4)
    print("inserting:", doubly_linked_list.print_forward())
    doubly_linked_list.remove_at(0)
    print("removing:", doubly_linked_list.print_forward())


