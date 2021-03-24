import copy
class Node:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def put(self, value):
        if self.head is None:
            node = Node(value, None, None)
            self.head = node
            self.tail = node
        else:
            self.tail.next = Node(value, self.tail, None)
            self.tail = self.tail.next

    def get(self):
        if self.head is None:
            return None
        elif self.head == self.tail:
            temp = self.head.value
            self.head = None
            self.tail = None
            return temp
        else:
            temp = self.head.value
            self.head = self.head.next
            if self.head is None:
                return temp
            self.head.prev = None
            return temp

    
    def peek(self):
        if self.head is None:
            return None
        return self.head.value

    def print(self):
        if self.head is None:
            print("[]")
        else:
            start = copy.copy(self.head)
            print("[", end="")
            while start.next is not None:
                print(start.value, end=", ")
                start = copy.copy(start.next)
            print(start.value,"]")
