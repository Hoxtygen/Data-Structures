import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1


    def dequeue(self):
        if not self.size:
            return None
        data = self.storage.remove_from_head()
        self.size -= 1
        return data
        

    def len(self):
        return self.size
