import array

class ArrayList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.array = array.array('i', [0]*capacity)

    def is_empty(self):
        return self.length==0

    def prepend(self, value):
        new_array = []
        if self.capacity<=self.length:
            self.capacity *= 2
            new_array = array.array('i', [0]*self.capacity)
            for i in range(self.length):
                new_array[i+1] = self.array[i]
            self.array = new_array
        else:
            for i in range(self.length-1, -1, -1):  #중요
                self.array[i+1] = self.array[i]
        
        self.array[0] = value
        self.length +=1


    def append(self, value):
        if self.capacity<=self.length:
            self.capacity *= 2
            new_array = array.array('i', [0]*self.capacity)
            for i in range(self.length):
                new_array[i] = self.array[i]

            self.array = new_array

        self.array[self.length] = value
        self.length += 1
            

    def set_head(self, index):
        self.array = self.array[index:]
        self.capacity = self.capacity - index
        self.length = self.length - index

    def access(self, index):
        return self.array[index]

    def insert(self, index, value):
        if self.capacity<= self.length:
            self.capacity *= 2
            new_array = array.array('i', [0]*self.capacity)
            for i in range(self.length):
                new_array[i] = self.array[i]
            self.array = new_array

        for i in range(self.length-1, index-1, -1):
            self.array[i+1] = self.array[i]
        
        self.array[index] = value
        self.length += 1



    def remove(self, index):
        for i in range(index, self.length):
            self.array[i] = self.array[i+1]

        self.array[self.length] = 0
        self.length -=1

    def print(self):
        print('[', end= "")
        for i in range(self.length):
            if(i==self.length-1):
                print(self.array[i],']')
            else:
                print(self.array[i],end=', ')

    