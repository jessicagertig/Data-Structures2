from dll_queue import Queue
from dll_stack import Stack

def cb(value):
    result = value + 2
    return result

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if self is None:
        #     self = BinarySearchTree(value)
        # else:
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else: 
                self.right = BinarySearchTree(value)
        else:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        else:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self is None:
            return None
        elif self is not None:
            if self.right:
                return self.right.get_max()
            else:
                return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self:
            cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
        

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            self.in_order_print(node.left)
            
        print(node.value)
            
        if node.right:
            self.in_order_print(node.right)
            
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)

        while node is not None:
            node = q.dequeue()
            if node is None:
                break
            print(node.value)
            if node.right:
                q.enqueue(node.right)
            if node.left:
                q.enqueue(node.left)
            
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        s = Stack()
        s.push(node)

        while node is not None:
            node = s.pop()
            if node is None:
                break
            print(node.value)
            if node.right:
                s.push(node.right)
            if node.left:
                s.push(node.left)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

bst = BinarySearchTree(7)
bst.insert(5)
bst.insert(8)
bst.insert(10)
bst.insert(3)
bst.insert(9)
bst.insert(4)

bst.dft_print(bst)