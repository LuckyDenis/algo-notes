# coding: utf8

"""
Линейный связанный список.
"""


class Node:
    def __init__(self, payload, node=None):
        self.payload = payload
        self.next_node = node

    def __str__(self):
        return 'Node: (payload: {p}, next_node: {n})'.format(
            p=self.payload, n=self.next_node
        )


class LinkedList:
    def __init__(self):
        self.len = 0
        self.root = None

    def push(self, payload):
        if not self.root:
            self.root = Node(payload)
        else:
            node = Node(payload, self.root)
            self.root = node
        self.len += 1

    def pop(self):
        if not self.root:
            raise IndexError("pop from empty linked list")

        payload = self.root.payload
        self.root = self.root.next_node
        self.len -= 1

        return payload

    def __getitem__(self, index):
        if self.len < index:
            raise IndexError('linked list index out of range')
        count = 0
        for payload in self.__iter__():
            if count == index:
                return payload
            count += 1

    def __len__(self):
        return self.len

    def __str__(self):
        return 'LinkedList: (root: {r})'.format(r=self.root)

    def __iter__(self):
        return self.__next__()

    def __next__(self):
        curr = self.root
        while curr is not None:
            yield curr.payload
            curr = curr.next_node
