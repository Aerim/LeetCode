from collections import deque

class MyStack(object):

    def __init__(self):
        self.q = deque([])
        
    def push(self, x):
        self.q.append((x))
        
    def pop(self):
        return self.q.pop()
    
    def top(self):
        return self.q[-1]
       
    def empty(self):
        if len(self.q) == 0:
            return True
        else:
            return False
        
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
