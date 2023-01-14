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
      # right subtree
      else:
        if self.right:
          self.right.add_child(data)
        else:
          self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
      fullname_letters =[]
      # visit left subtree
      if self.left:
        fullname_letters += self.left.in_order_traversal()
      # visit base node
      fullname_letters.append(self.data)
      # visit right subtree
      if self.right:
        fullname_letters += self.right.in_order_traversal()
      return fullname_letters

    def pre_order_traversal(self):
      fullname_letters =[self.data]
      # visit left subtree
      if self.left:
        fullname_letters += self.left.pre_order_traversal()
      # visit left subtree
      if self.right:
        fullname_letters += self.right.pre_order_traversal()
      return fullname_letters

    def post_order_traversal(self):
      fullname_letters = []
      # visit left subtree
      if self.left:
        fullname_letters += self.left.post_order_traversal()
      return fullname_letters

def build_letter_tree(fullname_letters):
  root = BinarySearchTreeNode(fullname_letters[0])
  for i in range(1, len(fullname_letters)):
    root.add_child(fullname_letters[i])
  return root

if __name__ == '__main__':
  letters = ["I", "R", "I", "S", "H", "M", "I", "C", "O", "L", "E", "C", "A", "N," "D", "O"]
  letters_tree = build_letter_tree(letters)
  print(letters_tree.in_order_traversal())
  print(letters_tree.pre_order_traversal())