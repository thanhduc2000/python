class Stack:
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        #return len(self.items) == 0
        return self.items == []

    def __str__(self):
        if self.items == []:
            return ""
        return ' '.join([str(i) for i in self.items])

    def clear(self):
        return []
