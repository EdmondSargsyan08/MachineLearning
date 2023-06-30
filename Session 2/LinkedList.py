class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__ (self):
        self.head = None

    def add_from_end(self, data):
        new_node = node(data)
        if not self.head:

