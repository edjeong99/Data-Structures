# queue is done


class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = []

    def enqueue(self, item):
        self.storage.append(item)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            item = self.storage[0]
            del self.storage[0]
            self.size -= 1
        else:
            item = None

        return item

    def len(self):
        return self.size
