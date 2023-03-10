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
      # visit right subtree
      if self.right:
        fullname_letters += self.right.post_order_traversal()
      # visit base node
      fullname_letters.append(self.data)
      return fullname_letters

    def search(self, val):
      if self.data == val:
        return True
      # value might be in left subtree
      if val < self.data:
        # checks if left subtree has value
        if self.data:
          return self.left.search(val)
        else:
          return False
      
      # value might be in right subtree
      if val > self.data:
        # checks if right subtree has value
        if self.data:
          return self.right.search(val)
        else:
          return False

    # since left subtree has lower values
    def find_min(self):
      if self.left is None:
        return self.data
      return self.left.find_min()

    # since right subtree has higher values
    def find_max(self):
      if self.right is None:
        return self.data
      return self.right.find_max()

    def delete(self, val):
      # checks left subtree
      if val < self.data:
        if self.left:
          self.left = self.left.delete(val)
      # checks right subtree
      elif val > self.data:
        if self.right:
          self.right = self.right.delete(val)
      else:
        if self.left is None and self.right is None:
            return None
        elif self.left is None:
            return self.right
        elif self.right is None:
            return self.left

        min_val = self.right.find_min()
        self.data = min_val
        self.right = self.right.delete(min_val)

      return self


def build_letter_tree(fullname_letters):
  root = BinarySearchTreeNode(fullname_letters[0])
  for i in range(1, len(fullname_letters)):
    root.add_child(fullname_letters[i])
  return root

if __name__ == '__main__':
  letters = ["I", "R", "I", "S", "H", "M", "I", "C", "O", "L", "E", "C", "A", "N," "D", "O"]
  letters_tree = build_letter_tree(letters)
  print(f"Name: IRISH MICOLE CANDO")
  print(f"In Order Traversal: {letters_tree.in_order_traversal()}")
  print(f"Pre Order Traversal: {letters_tree.pre_order_traversal()}")
  print(f"Post Order Traversal: {letters_tree.post_order_traversal()}")
  print(f"Is letter R in my fullname? {letters_tree.search('R')}")
  print(f"Minimum Value: {letters_tree.find_min()}")
  print(f"Maximum Value: {letters_tree.find_max()}")
  letters_tree.delete("I")
  print(f"After deleting letter I, the new in order traversal is {letters_tree.in_order_traversal()}")