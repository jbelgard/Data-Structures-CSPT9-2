"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

import sys
sys.path.append('singly_linked_list')
from singly_linked_list import LinkedList # pylint: disable = import-error

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def isEmpty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_head()


#3. In terms of the implementation, both Stacks are nearly identical with only the method names differing.  In terms of performance, the push and pop methods for both implementations are 0(1).  The LL's remove_tail method has a performance of o(n).  So, in order for it to acheive a performance of o(1), the stack must be implemented so that the 'head' of the LL represents the 'top' of the stack.  Compared to the array implementation where last index in the array represents the 'top' of the stack.
