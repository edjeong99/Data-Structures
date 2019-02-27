

from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


# LRUCache uses Doubly Linked List
# new item is stored at Top
# oldest is stored at Tail


class LRUCache:
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.dll = DoublyLinkedList()

    """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the top of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache.
  """

    def get(self, key):

        current = self.dll.head

# loop the link to see if there is a matched key
        while current:
            if key in current.value:  # matched key found
                self.dll.move_to_front(current)
                return current.value[key]

            current = current.next

    """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply
  want to overwrite the old value associated with the key with
  the newly-specified value.
  """

    def set(self, key, value):

        # if key exists in list, replace value and move it to Head
        current = self.dll.head

        while current:
            if key in current.value:  # match found
                current.value[key] = value
                self.dll.move_to_front(current)  # move to head
                return
            current = current.next

        # if key doesn't exist in list, add the new Node to Head
        # use dictionary format to save input
        input = {key: value}
        self.dll.add_to_head(input)
        self.size += 1

        # size is more than limit, delete Tail
        if self.size > self.limit:
            self.dll.remove_from_tail()
            self.size -= 1


def print_all(lcache):
    current = lcache.dll.head
    while current:
        print(f'print all current.value = {current.value}')
        current = current.next
    print('end of print all')


l = LRUCache(3)
l.set('item1', 'a')
l.set('item2', 'b')
l.set('item3', 'c')


l.set('item2', 'z')
print_all(l)
print(l.get('item1'))
'''
l.get('item1')
print_all(l)
l.set('item3', 'c')
print_all(l)
l.get('item2')
print_all(l)
'''
