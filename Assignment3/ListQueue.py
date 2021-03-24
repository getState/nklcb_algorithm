import array

class LinearQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.array = array.array('l', [0]*capacity)

    def put(self, value):
        if self.rear == self.capacity:
            print("overflow")
            return False
        self.array[self.rear] = value
        self.rear += 1
        return True

    def get(self):
        if self.front == self.rear:
            return None
        self.front +=1
        return self.array[self.front-1]

    def peek(self):
        if self.front == self.rear:
            return None
        return self.array[self.front]

    def print(self):
        if self.front == self.rear:
            print("[]")
        else:
            start = self.front
            end = self.rear
            print("[",self.array[start], end="",sep="")
            start +=1
            while start!=end:
                print(", ",self.array[start], end="")
                start +=1
            print("]")