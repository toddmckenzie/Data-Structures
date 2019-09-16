# import sys
# sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    self.storage = DoublyLinkedList()

  # Should add item to the back of the queue
  def enqueue(self, value):
    self.storage.add_to_tail(value)
  
  # Should remove and return an item from the front of the queue
  def dequeue(self):
    # value = self.storage.remove_from_head()
    value = self.storage.remove_from_head()
    return value

  #return the number of items in the queue
  def len(self):
    return self.storage.__len__()
