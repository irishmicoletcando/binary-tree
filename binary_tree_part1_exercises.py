# 1. find_min(): finds minimum element in entire binary tree
# 2. find_max(): finds maximum element in entire binary tree
# 3. calculate_sum(): calculates sum of all elements
# 4. post_order_traversal(): performs post order traversal of a binary tree
# 5. pre_order_traversal(): perofrms pre order traversal of a binary tree

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
    elements =[]

    # visit left tree
    if self.left:
      elements += self.left.in_order_traversal()

    # visit base node
    elements.append(self.data)

    # visit right tree
    if self.right:
      elements += self.right.in_order_traversal()

    return elements

  def search(self, val):
    if self.data == val:
      return True

    # value might be in left subtree
    if val < self.data:
      # checks if left subtree has value
      if self.data:
        self.left.search(val)
      else:
        return False

    # value might be in right subtree
    if val > self.data:
      # checks if right subtree has value
      if self.data:
        self.right.search(val)
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

  def calculate_sum(self):
    left_sum = self.left.calculate_sum() if self.left else 0
    right_sum = self.right.calculate_sum() if self.right else 0
    # base node + left subtree + right subtree
    return self.data + left_sum + right_sum

  def pre_order_traversal(self):
    elements = [self.data]
    if self.left:
      elements += self.left.pre_order_traversal()
    return elements
    
def build_tree(elements):
  root = BinarySearchTreeNode(elements[0])

  for i in range(1, len(elements)):
    root.add_child(elements[i])

  return root

if __name__ == '__main__':
  numbers = [17, 4, 1, 20, 9, 23, 18, 34]
  numbers_tree = build_tree(numbers)
  print(numbers_tree.in_order_traversal())
  print(numbers_tree.search(20))
  print(numbers_tree.find_min())
  print(numbers_tree.find_max())