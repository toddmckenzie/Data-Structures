  def add_to_head(self, value):
    new_node = ListNode(value, None, None)
    if not self.head and not self.tail:  
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node
    
    self.length += 1
  