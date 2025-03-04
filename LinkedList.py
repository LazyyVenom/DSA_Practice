class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.size += 1

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
    
    def __str__(self):
        if self.head is None:
            return "Empty"
        else:
            current = self.head
            out = []
            while current:
                out.append(str(current.data))
                current = current.next
            return " -> ".join(out)
    
    def __len__(self):
        return self.size
    
    def __getitem__(self, index):
        if index >= self.size:
            raise IndexError("Index out of range")
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            return current.data


if __name__ == "__main__":
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    print(l)
    print(len(l))
    l.prepend(0)
    print(l)
    print(len(l))