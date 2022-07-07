"""
-- Created by Pravesh Budhathoki
-- Treeleaf Technologies Pvt. Ltd.
-- Created on 2022-07-07 
"""

"""This is a bit advance of Hash Table. Here collisions are handled using Linked List """


class HashTable:
    def __init__(self, size=15):
        self.size = size

        # instead of "None" empty list is created to store (key, value) pair and add multiple elements i.e. multiple
        # keys and values in the list to avoid collision if same hash is generated for different key.
        self.array = [[] for _ in range(self.size)]

    def get_hash(self, key):
        h = 0
        for k in key:
            h += ord(k)
        return h % self.size

    # This method helps to insert the item in hash table,
    # item can be inserted by, hash_table[key] = value, where hash_table is object of class HashTable
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        flag = False

        # This code replaces the value of key with new value in hash table
        for _index, elements in enumerate(self.array[h]):
            if len(elements) == 2 and elements[0] == key:
                self.array[h][_index] = (key, value)
                flag = True
                break
        # This code just append the items i.e. (key, value) in hash table
        if not flag:
            self.array[h].append((key, value))

        return self.array

    # This method helps to get the "value" from hash table by using "key",
    # value can be extracted by, hash_table[key] gives "value" that is related to that "key",
    # here hash_table is object of class HashTable
    def __getitem__(self, key):
        h = self.get_hash(key)
        for _index, element in enumerate(self.array[h]):
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for _index, element in enumerate(self.array[h]):
            if element[0] == key:
                del self.array[h][_index]
        return self.array


if __name__ == '__main__':
    hash_table = HashTable()

    # pravesh and bikash generates same hash value, so it is kept in same list in hash table which avoids collision
    # This is the process of avoiding collisions using Linked List
    hash_table["pravesh"] = 24
    hash_table["bikash"] = 25
    hash_table["simon"] = 31
    hash_table["march 22"] = 30
    print("Original value in hash table:", hash_table.array)

    # replace the value of pravesh to 22
    hash_table["pravesh"] = 22
    print("After replacing value of key pravesh hash table:", hash_table.array)

    del hash_table["march 22"]
    print("Deleting march 22 key from hash table:", hash_table.array)

