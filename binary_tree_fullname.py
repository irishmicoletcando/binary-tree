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
          self.left.add_child(data)
        else:
          self.left = BinarySearchTreeNode(data)
      else:
        if self.right:
          self.right.add_child(data)
        else:
          self.right = BinarySearchTreeNode(data)