class BinarySearchTreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

  
  def add_child(self, data):
    if data == self.data:
      return

    # left subtree
    if data < self.data:
      if self.left:
        self.left.add_child(data)
      else:
        self.left = BinarySearchTreeNode(data)
    else:
      if self.right:
        self.right.add_child(data)
      else:
        self.right = BinarySearchTreeNode(data)

  def in_order_traversal(self):
    elements =[]

    # visit left tree
    if self.left:
      elements += self.left.in_order_traversal()

    # visit base node
    elements.append(self.data)

    
    return elements