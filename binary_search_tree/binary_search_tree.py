class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):

        current = self

        # loop through tree until None is reached
        while True:
            # if value is less than the Node value, go left
            if value < self.value:

                if not self.left:
                    self.left = BinarySearchTree(value)
                    break
                self = self.left

            # if value is same or bigger than the Node value, go right
            else:

                if not self.right:
                    self.right = BinarySearchTree(value)
                    break
                self = self.right

    def contains(self, target):
        current = self
        # while loop until there is no more Node
        while self:
            if self.value == target:
                return True
            if target < self.value:
                self = self.left
            else:
                self = self.right
        # if loop doesn't find target, return False
        return False

    def get_max(self):
        current = self

        # get right Node until there is no more right node
        while self.right:
            self = self.right

        return self.value
