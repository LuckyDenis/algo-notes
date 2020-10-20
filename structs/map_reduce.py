# coding: utf8
"""
MapReduce

https://docs.mongodb.com/manual/core/map-reduce/
"""


class Queue:
    def __init__(self):
        self.storage = []

    def make(self, data):
        for item in data:
            self.storage.append([str(item), 1])


class Map:
    def __init__(self):
        self.storage = dict()

    def emit(self, queue_storage):
        for item in queue_storage:
            key = item[0]
            count = item[1]
            if key not in self.storage:
                self.storage[key] = []
            self.storage[key].append(count)


class Reduce:
    def __init__(self):
        self.storage = dict()

    def merge(self, map_storage):
        for key in map_storage:
            self.storage[key] = sum(map_storage[key])
