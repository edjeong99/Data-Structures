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
        # if list is empty (head is None ), assign new Node to head and tail
        if self.head:
            current = self.head

            if current.next:
                self.head = current.next
                current.next.prv = None
            else:
                self.head = None
            value = current.value
            current.delete()
            return value

    def add_to_tail(self, value):
        # if tail is None, set head/tail to new Node
        if not self.tail:
            self.head = ListNode(value)
            self.tail = self.head

        # there is node in the list
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next

    def remove_from_tail(self):
        # if tail has a Node, assign new tail
        if self.tail:
            self.tail = self.tail.prev
            # delete old tail
            value = self.tail.next.value
            self.tail.next.delete()
            return value

    def move_to_front(self, node):
        # take care of current node's next/prev
        # if node is tail, assign new tail
        if not node.next:
            self.tail = node.prev

           # assign node's next/prev to right nodes
        else:
            node.prev.next = node.next

            if node.prev:
                node.next.prev = node.prev

        # now take care of head
            # assign head to node and edit node's next/prev
        self.head.prev = node
        node.next = self.head
        self.head = self.head.prev
        node.prev = None

    def move_to_end(self, node):
        # take care of current node's next/prev
        # if node is tail, assign new tail
        if not node.prev:
            self.head = node.next

           # assign node's next/prev to right nodes
        else:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        # now take care of tail
            # assign tail's next to node and edit node's next/prev
        self.tail.next = node
        node.prev = self.tail
        self.tail = self.tail.next
        node.next = None

    def delete(self, node):
        if node:
            node.next.prev = node.prev
            node.prev.next = node.next

            node.delete()

    def get_max(self):
        current = self.head
        maxVal = float("-inf")

        while current:
            maxVal = max(maxVal, current.value)
            current = current.next
        return maxVal


'''
ll = DoublyLinkedList()

ll.add_to_head(3)
print(ll.head.value)
print(ll.tail.value)
print('---')
ll.add_to_head(1)
print(ll.head.value)
print(ll.tail.value)
print('---')
ll.add_to_head(0)
print(ll.head.value)
print(ll.tail.value)
print('---')

ll.remove_from_head()
print(ll.head.value)
print(ll.tail.value)
print('---')

ll.remove_from_head()
print(ll.head.value)
print(ll.tail.value)
print('---')

ll.remove_from_head()

print('---')
'''

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
