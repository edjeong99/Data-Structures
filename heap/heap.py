class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage)-1)

    def delete(self):
        # remove the first item in array and place the last item in the first place
        self.storage[0] = self.storage[len(self.storage)-1]
        self.storage.pop()

        index = 0
        # loop with _sift_down

        while index < len(self.storage) - 1:
            index = self._sift_down(index)

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

    def _sift_down(self, index):

        if len(self.storage) >= (2*index)+2:
            if self.storage[(2*index)+1] > self.storage[(2*index)+2]:
                if self.storage[(2*index)+1] > self.storage[index]:
                    self.storage[index], self.storage[(2*index) + 1 = self.storage[(2*index)+1], self.storage[index]
                    return 2*index + 1
            else:
                if self.storage[2*index+2] > self.storage[index]:
                    self.storage[index], self.storage[2*index +
                                                      2] = self.storage[2*index+2], self.storage[index]
                    return 2*index + 2

        return len(self.storage)
