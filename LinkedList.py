class Node:

  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:

  def __init__(self):
    self.head = None

  def print_list(self):
    cur_node = self.head
    while cur_node:
      print(cur_node.data)
      cur_node = cur_node.next

  def append(self, data):
    new_node = Node(data)

    if self.head is None:
      self.head = new_node
      return

    last_node = self.head
    while last_node.next:
      last_node = last_node.next
    last_node.next = new_node

  def prepend(self, data):
    new_node = Node(data)

    new_node.next = self.head
    self.head = new_node

  def insert_after_node(self, prev_node, data):

    if not prev_node:
      print("Previous node does not exist.")
      return

    new_node = Node(data)

    new_node.next = prev_node.next
    prev_node.next = new_node

  def delete_node(self, key):

    cur_node = self.head

    if cur_node and cur_node.data == key:
      self.head = cur_node.next
      cur_node = None
      return

    prev = None
    while cur_node and cur_node.data != key:
      prev = cur_node
      cur_node = cur_node.next

    if cur_node is None:
      return

    prev.next = cur_node.next
    cur_node = None

  def delete_node_at_pos(self, pos):
    if self.head:
      curr_node = self.head
      if pos == 0:
        self.head = curr_node.next
        curr_node = None
        return

      prev = None
      count = 0

      while curr_node and count != pos:
        prev = curr_node
        curr_node = curr_node.next

        count += 1

      if curr_node is None:
        return

      prev.next = curr_node.next
      curr_node = None

  def len_iterative(self):
    count = 0
    curr_node = self.head
    while curr_node:
      count += 1
      curr_node = curr_node.next

    return count

  def len_recursive(self, node):
    if node is None:
      return 0
    return 1 + self.len_recursive(node.next)

  def swap_nodes(self, key_1, key_2):
    if key_1 == key_2:
      return

    prev_1 = None
    curr_node_1 = self.head
    while curr_node_1 and curr_node_1.data != key_1:
      prev_1 = curr_node_1
      curr_node_1 = curr_node_1.next

    prev_2 = None
    curr_node_2 = self.head
    while curr_node_2 and curr_node_2.data != key_2:
      prev_2 = curr_node_2
      curr_node_2 = curr_node_2.next

    if not curr_node_2 or not curr_node_1:
      return

    if prev_1:
      prev_1.next = curr_node_2
    else:
      self.head = curr_node_2

    if prev_2:
      prev_2.next = curr_node_1
    else:
      self.head = curr_node_1

    curr_node_1.next, curr_node_2.next = curr_node_2.next, curr_node_1.next

  def reverse_iterative(self):
    prev = None
    curr = self.head

    while curr:
      nxt = curr.next
      curr.next = prev
      prev = curr
      curr = nxt
    self.head = prev

  def reverse_recursive(self):

    def _reverse_recursive(curr, prev):
      if not curr:
        return prev

      nxt = curr.next
      curr.next = prev
      prev = curr
      curr = nxt

      return _reverse_recursive(curr, prev)

    self.head = _reverse_recursive(curr = self.head, prev = None)


  def merge_sorted(self, linkedList):
    curr_node_1 = self.head
    curr_node_2 = linkedList.head
    small_node = None
    index = 0
    
    while curr_node_1 or curr_node_2:
      if curr_node_1 and curr_node_2:  
        if curr_node_1.data < curr_node_2.data:
          if small_node is not None:
            small_node.next = curr_node_1
          small_node = curr_node_1
          curr_node_1 = curr_node_1.next
        else:
          if small_node is not None:
            small_node.next = curr_node_2
          small_node.next = curr_node_2
          small_node = curr_node_2
          curr_node_2 = curr_node_2.next
  
      else:
        if curr_node_1: 
          if small_node is not None:
            small_node.next = curr_node_1
          small_node.next = curr_node_1
          small_node = curr_node_1
          curr_node_1 = curr_node_1.next

        if curr_node_2:
          if small_node is not None:
            small_node.next = curr_node_2
          small_node.next = curr_node_2
          small_node = curr_node_2
          curr_node_2 = curr_node_2.next

      if index == 0:
        self.head = small_node

      index += 1


  def remove_duplicates(self):
    prev = None
    curr = self.head
    duplicate = dict()

    while curr:
      if curr.data in duplicate:
        prev.next = curr.next
        curr = None
      else:
        duplicate[curr.data] =  1
        prev = curr
        
      curr = prev.next



llist = LinkedList()
llist.append(1)
llist.append(6)
llist.append(1)
llist.append(4)
llist.append(2)
llist.append(2)
llist.append(4)

print("Original Linked List")
llist.print_list()
print("Linked List After Removing Duplicates")
llist.remove_duplicates()
llist.print_list()

# llist_1 = LinkedList()
# llist_2 = LinkedList()

# llist_1.append(1)
# llist_1.append(5)
# llist_1.append(7)
# llist_1.append(9)
# llist_1.append(10)

# llist_2.append(2)
# llist_2.append(3)
# llist_2.append(4)
# llist_2.append(6)
# llist_2.append(8)

# llist_1.merge_sorted(llist_2)
# print("===============================")
# llist_1.print_list()
# print("===============================")



    
# llist = LinkedList()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.append("D")

# # llist.delete_node("B")
# # llist.delete_node("E")
# print("===============================")
# llist.print_list()

# # llist.delete_node_at_pos(0)
# print("===============================")
# llist.print_list()

# print(f"Iterative function len {llist.len_iterative()}")
# print("===============================")
# print(f"Recursive function len {llist.len_recursive(llist.head)}")
# print("===============================")
# llist.swap_nodes("B", "D")
# print("Swapping nodes B and D that are not head nodes")
# llist.print_list()
# print("===============================")
# llist.swap_nodes("A", "B")
# print("Swapping nodes A and B where key_1 is head node")
# llist.print_list()
# print("===============================")
# print(llist.reverse_iterative())
# print(llist.print_list())
# print("===============================")
# print(llist.reverse_recursive())
# print(llist.print_list())
# print("===============================")
