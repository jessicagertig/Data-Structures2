
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
            self.size -= 1
            return self.storage.remove_from_tail()

    ##front is the tail as you dequeue from the end of a line
    def find_front(self):
        return self.storage.tail

    def len(self):
        return self.size

q = Queue()
q.enqueue(3)
q.enqueue(5)
q.enqueue(7)
q.dequeue()
q.enqueue(4)