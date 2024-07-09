import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack



class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    

  def insert(self, value):
    if value < self.value: 
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    elif value > self.value:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)
    
    
  def contains(self, target):
    if target == self.value:
      return True
    elif target > self.value:
      if not self.right:
        return False
      else:
        return self.right.contains(target)
    elif target < self.value:
      if not self.left:
        return False
      else:
        return self.left.contains(target)

  def get_max(self):
    if not self.right:
      return self.value
    else:
      return self.right.get_max()

  def for_each(self, cb):
    cb(self.value)
    if self.left:
      self.left.for_each(cb)  
    if self.right:
      self.right.for_each(cb)

 # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    # was in_order_print
  def in_order_print(self, node):
    if node:
      self.in_order_print(node.left)
      print(node.value) 
      self.in_order_print(node.right)
   
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal bv
  def bft_print(self, node):
    queue = Queue()
    queue.enqueue(node)
    while queue.len() > 0:
      awesome_node = queue.dequeue()
      print(awesome_node.value)
      if awesome_node.left:
        queue.enqueue(awesome_node.left)
      if awesome_node.right:
        queue.enqueue(awesome_node.right)  
      
   

    


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
  def dft_print(self, node):
    stack = Stack()
    stack.push(node)
    while stack.len() > 0:
      popped  = stack.pop()
      print(popped.value)
      if popped.left:
        stack.push(popped.left)
      if popped.right:
        stack.push(popped.right)
        # create stack. 
    # put root in stack, 
    # while stack is not empty.
    # pop first item in stack
    # check root.left and put in stack
    # check root.right and put in stack
    # go to top of stack and continue.





    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
  def pre_order_dft(self, node):
    pass

    # Print Post-order recursive DFT
  def post_order_dft(self, node):
    pass

  def in_order_dft(self,node):
    pass
    # Should have the methods `insert`, `contains`, `get_max`.
    #   * `insert` adds the input value to the binary search tree, adhering to the rules of the ordering of elements in a binary search tree.
    #   * `contains` searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not.
    #   * `get_max` returns the maximum value in the binary search tree. //needs to keep going right
    #   * `for_each` performs a traversal of _every_ node in the tree, executing the passed-in callback function on each tree node value. There is a myriad of ways to perform tree traversal; in this case any of them should work. 

    # ![Image of Binary Search Tree](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Binary_search_tree.svg/300px-Binary_search_tree.svg.png)