import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList



class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def dequeue(self):
        if self.size > 0:
            value = self.storage.tail.value
            self.size -= 1
            self.storage.remove_from_tail()
            return value

    def len(self):
        return self.size

q = Queue()
q.enqueue(3)
q.enqueue(5)
q.enqueue(7)
q.dequeue()
q.enqueue(4)