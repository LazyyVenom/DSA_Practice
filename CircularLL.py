class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size

    def append(self, e):
        newNode = Node(e)
        if self._size == 0:
            self._head = newNode
        
        newNode.next = self._head
        self._tail = newNode
        self._size += 1
    
    def insert(self, e, idx):
        pass