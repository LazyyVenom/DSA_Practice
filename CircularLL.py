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
        if self._head is None:
            self._head = newNode
            self._tail = newNode
            newNode.next = newNode
        else:
            self._tail.next = newNode
            newNode.next = self._head
            self._tail = newNode
        self._size += 1
    
    def display(self):
        curr = self._head
        for i in range(len(self)):
            print(f"{curr.data} -> ", end="")
            curr = curr.next

    def insert(self, e, idx):
        pass


if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.append(1)
    cll.append(2)
    cll.append(3)
    cll.append(4)
    cll.append(5)
    cll.display()
    print()