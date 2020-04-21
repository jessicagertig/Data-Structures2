from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=3):
        self.limit = limit
        self.dll_cache = DoublyLinkedList()
        self.storage_dict = dict()
        self.size = 0
    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key not in self.storage_dict:
            return None
        else:
            value = self.storage_dict[key]
            curr_node = self.dll_cache.head
            while(curr_node is not None):
                if curr_node.value[0] == key:
                    node = curr_node
                    self.dll_cache.move_to_front(node)
                    curr_node = curr_node.next
                else:
                    curr_node = curr_node.next
            return value


    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.storage_dict:
            curr_node = self.dll_cache.head
            while(curr_node is not None):
                if curr_node.value[0] == key:
                    self.dll_cache.delete(curr_node)
                    curr_node = curr_node.next
                else:
                    curr_node = curr_node.next
            self.dll_cache.add_to_head((key, value))
            self.storage_dict[key] = value
        elif self.size < self.limit:
            self.size += 1
            ##add to head (key, value)
            self.dll_cache.add_to_head((key, value))
            ##add to dictionary
            self.storage_dict[key] = value
        elif self.size == self.limit: 
            oldest_key = self.dll_cache.tail.value[0]
            self.storage_dict.pop(oldest_key)
            self.dll_cache.remove_from_tail()
            self.dll_cache.add_to_head((key, value))
            self.storage_dict[key] = value


    
attempt = LRUCache()
attempt.set('item1', 'a')
print(attempt.size)
print("Head", attempt.dll_cache.head.value)
attempt.set('item2', 'b')
print(attempt.size)
print(attempt.dll_cache.length)

print(attempt.storage_dict)
print("Head", attempt.dll_cache.head.value)
print("Tail", attempt.dll_cache.tail.value)

attempt.set('item2', 'c')
print(attempt.size)
print(attempt.storage_dict)
print("Head", attempt.dll_cache.head.value)
print("Tail", attempt.dll_cache.tail.value)

attempt.set('item3', 'b')
attempt.set('item4', 'z')
print(attempt.size)
print(attempt.storage_dict)
print("Head", attempt.dll_cache.head.value)
print("Tail", attempt.dll_cache.tail.value)
attempt.get('item2')
print(attempt.size)
print(attempt.storage_dict)
print("Head", attempt.dll_cache.head.value)
print("Tail", attempt.dll_cache.tail.value)