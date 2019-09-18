import sys
sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    

  def insert(self, value):
    print(self.value, value, self.left, self.right)
    if value < self.value and self.left == None:
      self.left = value
    elif value > self.value and self.right == None:
      self.right = value
    elif value < self.value:
      self.value = self.left
      self.insert(value)
    elif value > self.value:
      self.value = self.right
      self.insert(value)
    elif value == self.value and self.left == None:
      self.left = self.value
    elif value == self.value:
      self.value = self.left
      self.insert(value)
    
  def contains(self, target):
    if target > self.value:
      self.value = self.right:
      self.contains(target)
    elif target < self.value:
      self.value = self.left
      self.contains(target)
    elif target == self.value:
      return True
    else:
      return False

  def get_max(self):
    while self.right != None:
      if self.right == None:
        return self.value
      else:
        self.value = self.right

  def for_each(self, cb):
    pass



# Should have the methods `insert`, `contains`, `get_max`.
#   * `insert` adds the input value to the binary search tree, adhering to the rules of the ordering of elements in a binary search tree.
#   * `contains` searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not.
#   * `get_max` returns the maximum value in the binary search tree. //needs to keep going right
#   * `for_each` performs a traversal of _every_ node in the tree, executing the passed-in callback function on each tree node value. There is a myriad of ways to perform tree traversal; in this case any of them should work. 

# ![Image of Binary Search Tree](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Binary_search_tree.svg/300px-Binary_search_tree.svg.png)