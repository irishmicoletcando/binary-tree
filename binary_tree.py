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
      if self.data:
        pass
      else:
        self.left = BinarySearchTreeNode(data)