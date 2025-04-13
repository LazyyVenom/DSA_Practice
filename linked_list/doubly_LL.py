class Node:
    __slots__ = '_data', '_prev', '_next'

    def __init__(self, data):
        self._data = data
        self._next = None
        self._prev = None

class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def prepend(self, val):
        newest = Node(val)
        if self.isEmpty():
            self._tail = newest
        
        else:
            self._head._prev = newest
            newest._next = self._head
        
        self._head = newest
        self._size += 1
    
    def append(self, val):
        newest = Node(val)
        if self.isEmpty():
            self._head = newest
        
        else:
            self._tail._next = newest
            newest._prev = self._tail
        
        self._tail = newest
        self._size += 1
    
    def insert(self, val, idx):
        if idx < 0 or idx >= self._size:
            raise IndexError("Index out of bounds")
        
        if idx == 0:
            self.prepend(val)
            return
        elif idx == len(self) - 1:
            self.append(val)
            return
        newest = Node(val)
        if idx <= self._size // 2:
            curr = self._head
            for i in range(idx):
                curr = curr._next
            temp = curr._next
            curr._next = newest
            newest._prev = curr
            newest._next = temp
            temp._prev = newest
        else:
            curr = self._prev
            for i in range(self._size - idx):
                curr = curr._prev
            temp = curr._prev
            curr._prev = newest
            newest._next = curr
            newest._prev = temp
            temp._next = newest
        
        self._size += 1
    
    def delete(self, idx):
        if idx == 0:
            self.deleteHead()
            return
        elif idx == len(self) - 1:
            self.deleteTail()
            return
        if idx <= self._size // 2:
            curr = self._head
            for i in range(idx):
                curr = curr._next
            temp = curr._prev
            temp._next = curr._next
            curr._next._prev = temp
        else:
            curr = self._tail
            for i in range(self._size - idx - 1):
                curr = curr._prev
            temp = curr._next
            temp._prev = curr._prev
            curr._prev._next = temp
        self._size -= 1
    
    def deleteHead(self):
        if self.isEmpty():
            raise IndexError("List is empty")
        if self._size == 1:
            self._head = None
            self._tail = None
        else:
            self._head = self._head._next
            self._head._prev = None
        self._size -= 1
    
    def deleteTail(self):
        if self.isEmpty():
            raise IndexError("List is empty")
        if self._size == 1:
            self._head = None
            self._tail = None
        else:
            self._tail = self._tail._prev
            self._tail._next = None
        self._size -= 1
    
    def display(self):
        curr = self._head
        while curr:
            print(curr._data, end=" <-> ")
            curr = curr._next
        print("None")