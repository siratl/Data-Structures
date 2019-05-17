"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    if value != None:
      if self.length > 0:
        self.head.insert_before(value)
        self.head = self.head.prev
      else:
        self.head = ListNode(value)
        self.tail = self.head
      self.length += 1

  def remove_from_head(self):
    if self.head != None:
      value = self.head.value
      if self.length > 1:
        new_head = self.head.next
        self.head.delete()
        self.head = new_head
      else:
        self.head = None
        self.tail = None
      self.length -= 1
      return value
    else:
      return None

  def add_to_tail(self, value):
    if value != None:
      if self.length > 0:
        self.tail.insert_after(value)
        self.tail = self.tail.next
      else:
        self.tail = ListNode(value)
        self.head = self.tail
      self.length += 1

  def remove_from_tail(self):
    if self.tail != None:
      value = self.tail.value
      if self.length > 1:
        new_tail = self.tail.prev
        self.tail.delete()
        self.tail = new_tail
      else:
        self.head = None
        self.tail = None
      self.length -= 1
      return value
    else:
      return None

  def move_to_front(self, node):
    current_prev = node.prev
    current_next = node.next
    current_prev_next = None
    current_next_prev = None

    if current_prev != None:
      if current_next != None:
        current_next.prev = current_prev
        current_prev.next = current_next
      else:
        current_prev.next = None
        self.tail = current_prev

    prev_head = self.head
    self.head = node
    node.prev = None
    node.next = prev_head
    prev_head.prev = node

  def move_to_end(self, node):
    current_prev = node.prev
    current_next = node.next
    current_prev_next = None
    current_next_prev = None

    if current_next != None:
      if current_prev != None:
        current_next.prev = current_prev
        current_prev.next = current_next
      else:
        current_next.prev = None
        self.head = current_next

    prev_tail = self.tail
    self.tail = node
    node.prev = prev_tail
    node.next = None
    prev_tail.next = node

  def delete(self, node):
    if node!=None:
      if self.length == 1:
        self.head = None
        self.tail = None
      else:
        if node.prev == None:
          self.head = node.next
        elif node.next == None:
          self.tail = node.prev
      node.delete()
      self.length -= 1
    
  def get_max(self):
    if self.length == 0:
      return None
    else:
      current_node = self.head
      max = self.head.value
      while(current_node != None):
        if current_node.value > max:
          max = current_node.value
        current_node = current_node.next
      return max
