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
#
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

    def add_to_head(self, value):

        # if list is empty (head is None ), assign new Node to head and tail
        if not self.head:
            self.head = ListNode(value)
            self.tail = self.head

        # there is node in the list
        else:
            self.head.insert_before(value)
            self.head = self.head.prev

    def remove_from_head(self):
        pass

    def add_to_tail(self, value):
        pass

    def remove_from_tail(self):
        pass

    def move_to_front(self, node):
        pass

    def move_to_end(self, node):
        pass

    def delete(self, node):
        pass

    def get_max(self):
        pass


ll = DoublyLinkedList()

ll.add_to_head(3)
print(ll.head.value)
print(ll.tail.value)

ll.add_to_head(1)
print(ll.head.value)
print(ll.tail.value)

ll.add_to_head(0)
print(ll.head.value)
print(ll.tail.value)

'''
ln = ListNode(1)

ln.insert_after(3)

current = ln
while current:
    print(current.value)
    current = current.next

ln.insert_after(2)

current = ln
while current:
    print(current.value)
    current = current.next
'''
