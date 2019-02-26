class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage)-1)

    def delete(self):
        # remove the first item in array and place the last item in the first place
        max = self.storage[0]
        self.storage[0] = self.storage[len(self.storage)-1]
        self.storage.pop()

        index = 0

        self._sift_down(index)
        return max

    def get_max(self):
        if self.storage[0]:
            return self.storage[0]
        else:
            return None

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):

        while self.storage[index] > self.storage[(index-1)//2]:
            self.storage[index], self.storage[(
                index-1)//2] = self.storage[(index-1)//2], self.storage[index]
            index = (index-1)//2
            if index == 0:
                break

    def _sift_down(self, index):
        # loop until there is no more child Node
        while index*2+1 <= len(self.storage) - 1:

            # see which children to compare
            if len(self.storage) < (2*index)+1:  # there is no child
                return
            # both child node exit and right one is bigger
            elif len(self.storage) > (2*index)+2 and self.storage[(2*index)+2] >= self.storage[(2*index)+1]:
                child = (2*index)+2
            else:  # left child is bigger
                child = (2*index)+1

             # compare with children and swap if needed
            if self.storage[child] > self.storage[index]:
                self.storage[index], self.storage[child] = self.storage[child], self.storage[index]

            index = child


'''
h = Heap()
h.insert(5)
print(h.storage)
h.insert(1)
print(h.storage)
h.insert(10)
print(h.storage)
h.insert(7)
print(h.storage)
h.delete()
print(h.storage)
h.delete()
print(h.storage)
'''
