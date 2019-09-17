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
    self.size += 1
    self.storage.add_to_tail(value)
  
  # Should remove and return an item from the front of the queue
  def dequeue(self):
    # value = self.storage.remove_from_head()
    # if self.size > 0: 
    #   self.size -= 1
    #   return self.storage.remove_from_head()
    # or below
    if len() > 0:
      self.size -= 1
      return self.storage.remove_from_head()
  #return the number of items in the queue
  def len(self):
    return self.size
