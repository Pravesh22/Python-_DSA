"""
--Created by Pravesh Budhathoki
--Created on 2022-07-07 
"""

"""This code gives basic overview of how dictionary works in python. 
Dictionary in python acts as Hash_Table"""


class HashTable:
    def __init__(self, size=15):
        self.size = size
        self.array = [None for _ in range(self.size)]

    def get_hash(self, key):
        h = 0
        for k in key:
            h += ord(k)
        return h % self.size

    def add(self, key, value):
        h = self.get_hash(key)
        self.array[h] = value
        return self.array

    def get(self, key):
        h = self.get_hash(key)
        return self.array[h]

    # This method helps to insert the item in hash table,
    # item can be inserted by, hash_table[key] = value, where hash_table is object of class HashTable
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.array[h] = value
        return self.array

    # This method helps to get the "value" from hash table by using "key",
    # value can be extracted by, hash_table[key] gives "value" that is related to that "key",
    # here hash_table is object of class HashTable
    def __getitem__(self, item):
        h = self.get_hash(item)
        return self.array[h]


if __name__ == '__main__':
    hash_table = HashTable()
    hash_table["ram"] = 24
    print(hash_table.array)
    # print(hash_table.array)
    # hash_table.add("ram", 24)
    # hash_table.add("shyam", 25)
    # hash_table.add("hari", 26)

