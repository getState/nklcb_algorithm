class Node:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        return self.head is None

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value, None, None)
            self.tail = self.head
        else:
            node = Node(value, self.head, None)
            self.head.prev = node
            self.head = node

    def append(self, value):
        if self.head is None:
            self.head = Node(value, None, None)
            self.tail = self.head
        else:
            node = Node(value, None, self.tail)
            self.tail.next = node
            self.tail = node 

    def set_head(self, index):
        if self.head is None:
            return False

        cur = self.head
        for _ in range(index):
            if cur.next is None:
                return False
            cur = cur.next
        self.head = cur
        self.head.prev = None
        return True

    def access(self, index):
        if self.head is None:
            return False
        
        cur = self.head
        for _ in range(index):
            if cur.next is None:
                return None
            cur = cur.next
        if cur is None:
            return False
        else:
            return cur.value

    


    def insert(self, index, value):
        if self.head is None and index > 0:
            return False

        if index == 0:
            self.prepend(value)
            return True
        
        curr = self.head
        for _ in range(index):
            if curr.next is None:
                return False
            curr = curr.next
        
        if curr is None:
            node = Node(value, None, self.tail)
            self.tail.next = node
            self.tail = node
        else:
            node = Node(value, curr, curr.prev)
            curr.prev.next = node
        return True

    def remove(self, index):
        if self.head is None:
            return False

        if index == 0:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return True
        
        curr = self.head
        for _ in range(index):
            if curr.next is None:
                return False
            curr = curr.next
        
        if curr is None:
            return False
        else:
            curr.prev.next = curr.next
            if curr.next is not None:
                curr.next.prev = curr.prev
            else:
                self.tail = curr.prev
            return True

    def print(self):
        if self.head is None:
            print("[]")
        else:
            cur = self.head
            print("[", end="")
            while cur.next is not None:
                print(cur.value, end=', ')
                cur = cur.next
            print(cur.value, ']')

    def print_inverse(self):
        if self.head is None:
            print("[]")
        else:
            cur = self.tail
            print("[", end="")
            while cur.prev is not None:
                print(self.tail.value, end=", ")
                cur = cur.prev
            print(cur.value, "]")
    