class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularDeque:
    def __init__(self, k):
        self.head = None
        self.tail = None
        self.count = 0
        self.capacity = k
    
    def insertFirst(self,node):
        self.head = node
        self.tail = node
        
    def insertFront(self, value):
        node = Node(value)
        if self.capacity == self.count:
            return False
        else:
            if self.head is None:
                self.insertFirst(node)
            else:
                node.next = self.head
                self.head.prev = node
                self.head = node
            self.count += 1
            return True

    def insertLast(self, value):
        node = Node(value)
        if self.capacity == self.count:
            return False
        else:
            if self.head is None:
                self.insertFirst(node)
            else:
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
            self.count += 1
            return True
    def deleteFront(self):
        if self.count == 0:
            return False
        else:
            if self.head.next is None:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.count -= 1
            return True
    def deleteLast(self) :
        if self.count == 0:
            return False
        else:
            if self.head.next is None:
                self.head = None
                self.tail = None
            else:
                node = self.tail.prev
                node.next = None
                self.tail = node
            self.count -= 1
            return True
    def getFront(self) :
        return -1 if self.head is None else self.head.val    
    def getRear(self):
        return -1 if self.tail is None else self.tail.val
    def isEmpty(self):
        return self.count == 0
    def isFull(self):
        return self.count == self.capacity
