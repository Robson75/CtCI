import node


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def insert(self, x):
        if self.first is None:
            self.first = node.Node(x, None)
            self.last = self.first
        elif self.last == self.first:
            self.last = node.Node(x, None)
            self.first.next = self.last
        else:
            current = node.Node(x, None)
            self.last.next = current
            self.last = current

    def __str__(self):
        if self.first is not None:
            current = self.first
            out = 'LinkedList [' + str(current.value)
            while current.next is not None:
                current = current.next
                out += " " + str(current.value)
            return out + ']'
        return 'LinkedList []'

    def clear(self):
        self.__init__()
