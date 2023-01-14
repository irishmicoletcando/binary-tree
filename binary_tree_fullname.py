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
    
    def in_order_traversal(self):
      fullname_letters =[]
      # visit left tree
      if self.left:
        fullname_letters += self.left.in_order_traversal()
      # visit base node
      fullname_letters.append(self.data)
      return fullname_letters



if __name__ == '__main__':
  letters = ["I", "R", "I", "S", "H", "M", "I", "C", "O", "L", "E", "C", "A", "N," "D", "O"]