from unittest.main import TestProgram


class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class __BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need. Recall that attributes in an inner class 
    # must be public to be reachable from the the methods.

    def __init__(self, value):
      self.value = value
      self.left_child = None
      self.right_child = None
      self.height = 0

  def __init__(self):
    self.__root = None

    # TODO complete initialization

  def __balance_factor_check(self, node):
    if node is None:
      return 0
    else:
      return self.__height_check(node.right_child) - self.__height_check(node.left_child)
  
  def __rotate_left(self, node):
    new_root = node.right_child
    old_left_child = node.left_child
    new_root.left_child = node
    node.right_child = old_left_child
    node.height = self.__height_check(node)
    new_root.height = self.__height_check(new_root)
    return new_root

  def __rotate_right(self, node):
    new_root = node.left_child
    floater = new_root.right_child
    new_root.right_child = node
    node.left_child = floater
    node.height = self.__height_check(node)
    new_root.height = self.__height_check(new_root)
    return new_root
  
  def __balance(self, node):
    diff = self.__balance_factor_check(node)
    if abs(diff) < 2:
      return node
    if diff >= 2:
      r = self.__balance_factor_check(node.right_child)
      if r > 0:
        return self.__rotate_left(node)
      if r < 0:
        node.right_child = self.__rotate_right(node.right_child)
        return self.__rotate_left(node)
    # if balance factor is 2, tree is right-heavy by 2, so check if right child has balance factor of 1 or -1
    # if -1, do double rotation and if 1 do single rotation           
    if diff <= -2:
      l = self.__balance_factor_check(node.left_child)
      if l < 0:
        return self.__rotate_right(node)
      if l > 0:
        node.left_child = self.__rotate_left(node.left_child)
        return self.__rotate_right(node)
    else:
      return node
    #if balance factor is -2, tree is left-heavy by 2
    #if left child has balance factor of 1, do double rotation and if -1 do single rotation

    #update heights


  def __recursive_insert(self, value, current_node):
    if current_node is None:
      node = Binary_Search_Tree.__BST_Node(value)
      current_node = node
      current_node.height = current_node.height + 1
      return node
    else:
      if current_node.value > value:
        current_node.left_child = self.__recursive_insert(value, current_node.left_child)
      if current_node.value < value:
        current_node.right_child = self.__recursive_insert(value, current_node.right_child)   
      if current_node.value == value:
        raise ValueError
    current_node.height = self.__height_check(current_node)
    return self.__balance(current_node)

  def insert_element(self, value):
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    self.__root = self.__recursive_insert(value, self.__root)
    
  
  def __height_check(self, node):
    if node is None:
      return 0
    if node.right_child is None:
      temp_right_height = 0
    else:
      temp_right_height = node.right_child.height
    if node.left_child is None:
      temp_left_height = 0
    else:
      temp_left_height = node.left_child.height
    if temp_right_height > temp_left_height:
      return temp_right_height + 1
    else:
      return temp_left_height + 1
    
  def __remove_recursive(self, value, current_node):
    if current_node is None:
        raise ValueError
    if current_node.value == value:
      if current_node.left_child is None and current_node.right_child is None:
        return None
      if current_node.left_child is None and current_node.right_child is not None:
        return current_node.right_child
      if current_node.left_child is not None and current_node.right_child is None:
        return current_node.left_child
      if current_node.left_child is not None and current_node.right_child is not None:
        temp = current_node.right_child
        while temp.left_child is not None:
          temp = temp.left_child
        current_node.value = temp.value
        current_node.right_child = self.__remove_recursive(temp.value, current_node.right_child)
    else:
      if value > current_node.value:
        current_node.right_child = self.__remove_recursive(value, current_node.right_child)
      if value < current_node.value:
        current_node.left_child = self.__remove_recursive(value, current_node.left_child)
    current_node.height = self.__height_check(current_node)
    return self.__balance(current_node)

  def remove_element(self, value):
    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    # to replace the value in a node instead. It is not necessary to
    # return the value (though it would reasonable to do so in some 
    # implementations). Your solution must be recursive. 
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    self.__root = self.__remove_recursive(value, self.__root)

 
  def __in_order_recursive(self, current_node):
    # base case is when node is None, create string of left child + value + right child for each node you visit
    # and add it to string you return
    if current_node.left_child is None and current_node.right_child is None:
      return str(current_node.value)
    if current_node.left_child is None and current_node.right_child is not None:
      return str(current_node.value) + ', ' + self.__in_order_recursive(current_node.right_child)
    if current_node.left_child is not None and current_node.right_child is None:
      return self.__in_order_recursive(current_node.left_child) + ', ' + str(current_node.value)
    else:
      return self.__in_order_recursive(current_node.left_child) + ', ' + str(current_node.value) + ', ' + self.__in_order_recursive(current_node.right_child)

  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.__root is None:
      return '[ ]'
    else:
      return '[ ' + self.__in_order_recursive(self.__root) + ' ]'


  def __pre_order_recursive(self, current_node):
    if current_node.left_child is None and current_node.right_child is None:
      return str(current_node.value)
    if current_node.left_child is None and current_node.right_child is not None:
      return str(current_node.value) + ', ' + self.__pre_order_recursive(current_node.right_child)
    if current_node.left_child is not None and current_node.right_child is None:
      return str(current_node.value) + ', ' + self.__pre_order_recursive(current_node.left_child)
    else:
      return str(current_node.value) + ', ' + self.__pre_order_recursive(current_node.left_child) + ', ' + self.__pre_order_recursive(current_node.right_child)

  def pre_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.__root is None:
      return '[ ]'
    else:
      return '[ ' + self.__pre_order_recursive(self.__root) + ' ]'

 
  def __post_order_recursive(self, current_node):
    if current_node.left_child is None and current_node.right_child is None:
      return str(current_node.value)
    if current_node.left_child is None and current_node.right_child is not None:
      return self.__post_order_recursive(current_node.right_child) + ', ' + str(current_node.value)
    if current_node.left_child is not None and current_node.right_child is None:
      return self.__post_order_recursive(current_node.left_child) + ', ' + str(current_node.value)
    else:
      return self.__post_order_recursive(current_node.left_child) + ', ' + self.__post_order_recursive(current_node.right_child) + ', ' + str(current_node.value)

  def post_order(self):
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.__root is None:
      return '[ ]'
    else:
      return '[ ' + self.__post_order_recursive(self.__root) + ' ]'

  def __to_list_recursive(self, current_node):
      if current_node is None:
        return []
      left = self.__to_list_recursive(current_node.left_child)
      right = self.__to_list_recursive(current_node.right_child)
      return left + [current_node.value] + right

  
  def to_list(self):
    return self.__to_list_recursive(self.__root)

  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
    if self.__root is None:
      return 0
    else:
      return self.__root.height

  def __str__(self):
    return self.in_order()

if __name__ == '__main__':
  tree = Binary_Search_Tree()
  tree.insert_element(10)
  # print(tree.in_order)
  tree.insert_element(5)
  # print(tree.in_order)
  tree.insert_element(3)
  #print(tree.in_order())
  print(tree.to_list())
