# import sys
# sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    self.storage = 

  # Should add item to the back of the queue
  def enqueue(self, value):
    self.size += 1
    pass
  
  # Should remove and return an item from the front of the queue
  def dequeue(self):
    self.size -= 1
    pass

  #return the number of items in the queue
  def len(self):
    return self.size
