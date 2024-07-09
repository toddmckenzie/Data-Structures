class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    print('here is the value ' + str(value))
    self._bubble_up(len(self.storage)-1)

  def delete(self):
    self.storage.pop(self.storage[0])
    

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    if self.storage[(index-1)//2] < self.storage[index]:
      # [self.storage[(index-1)//2], self.storage[index]] = [self.storage[index], self.storage[(index-1)//2]]
      temp = self.storage[(index-1)//2]
      self.storage[(index-1)//2] = self.storage[index]
      self.storage[index] = temp
      newIndex = (index-1)//2
      return self._bubble_up(newIndex)

  def _sift_down(self, index):
    pass

# * Should have the methods `insert`, `delete`, `get_max`, `_bubble_up`, and `_sift_down`.
#   * `insert` adds the input value into the heap; this method should ensure that the inserted value is in the correct spot in the heap
#   * `delete` removes and returns the 'topmost' value from the heap; this method needs to ensure that the heap property is maintained after the topmost element has been removed. 
#   * `get_max` returns the maximum value in the heap _in constant time_.
#   * `get_size` returns the number of elements stored in the heap.
#   * `_bubble_up` moves the element at the specified index "up" the heap by swapping it with its parent if the parent's value is less than the value at the specified index.
#   * `_sift_down` grabs the indices of this element's children and determines which child has a larger value. If the larger child's value is larger than the parent's value, the child element is swapped with the parent.

#  Thus the children of the node at position n would be at positions 2n and 2n + 1 in a one-based array, or 2n + 1 and 2n + 2 in a zero-based array. Computing the index of the parent node of n-th element is also straightforward. For one-based arrays is the parent on n/2 position, similarly for zero-based arrays is parent on (n-1)/2 position (floored).