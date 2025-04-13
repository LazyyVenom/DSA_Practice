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
        if len(self) <= idx:
            raise IndexError("Out Of Index Error")

        if idx == 0:
            self.addAtBegin(e)
        elif idx == len(self) - 1:
            self.append(e)
        else:
            newNode = Node(e)
            curNode = self._head
            for i in range(idx-1):
                curNode = curNode.next
            temp = curNode.next
            curNode.next = newNode
            newNode.next = temp
            self._size += 1

    def deleteAtBegin(self):
        if len(self) == 0:
            raise Exception("Already Empty!")

        elif len(self) == 1:
            self._head = None
            self._tail = None
            self._size = 0

        else:
            self._head = self._head.next
            self._tail.next = self._head
            self._size -= 1
    
    def deleteTail(self):
        if len(self) == 0:
            raise Exception("Already Empty!")

        elif len(self) == 1:
            self._head = None
            self._tail = None
            self._size = 0

        else:
            curNode = self._head
            for i in range(len(self) - 1):
                curNode = curNode.next
            
            curNode.next = self._head
            self._tail = curNode
            self._size -= 1
    
    def delete(self, idx):
        if len(self) <= idx:
            raise IndexError("Out Of Index Error")

        elif len(self) == 1:
            self._head = None
            self._tail = None
            self._size = 0

        elif idx == 0:
            self.deleteAtBegin()

        elif idx == len(self) - 1:
            self.deleteTail()
        
        else:
            curNode = self._head
            for i in range(idx - 1):
                curNode = curNode.next
            curNode.next = curNode.next.next
            self._size -= 1

    def addAtBegin(self, e):
        newNode = Node(e)
        if len(self) == 0:
            self._head = newNode
            self._tail = newNode
        else:
            newNode.next = self._head
            self._head = newNode
        
        self._tail.next = newNode
        self._size += 1


if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.append(1)
    cll.append(2)
    cll.append(3)
    cll.append(4)
    cll.append(5)
    cll.display()
    print()