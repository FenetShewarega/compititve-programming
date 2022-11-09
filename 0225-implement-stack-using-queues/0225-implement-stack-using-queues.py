class MyStack:

    def __init__(self):
        
        self.q1 =deque()
        self.q2 = deque()
    def push(self, x: int) -> None:
        for i in range(len(self.q1)):
            self.q2.append(self.q1.popleft())
        self.q1.append(x)    
        for x in range(len(self.q2)):
            self.q1.append(self.q2.popleft())
            
    def pop(self) -> int:
        return self.q1.popleft()
        

    def top(self) -> int:
        return self.q1[0]
  
    def empty(self) -> bool:
        return  len(self.q1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# [123]  q1 [3,2,1]
#        q2 []


# [3 2 1]
# [ ]