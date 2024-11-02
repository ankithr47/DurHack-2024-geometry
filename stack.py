class Stack:
    l = []
    def push(self, item):
        (self.l).append(item)
    def pop(self):
        x = self.l[len(self.l)-1]
        del self.l[len(self.l)-1]
        return x
