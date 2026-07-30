from collections import deque 
class MyStack(object):

    def __init__(self):
        self.input_deque=deque()
        # self.outut_deque=deque()
        # self.stack=[]
        

    def push(self, x):
        self.input_deque.append(x)

        for i in range(len(self.input_deque)-1):
            self.input_deque.append(self.input_deque.popleft())
        # self.stack.append(x)
        

    def pop(self):
        
        return self.input_deque.popleft()
        

        
        
        # if self.stack:
        #     return self.stack.pop()
        # else:
        #     return None
        
        

    def top(self):
        
        
        return self.input_deque[0]
        # if self.stack:
        #     return self.stack[-1]
        # else:
        #     return None
        

    def empty(self):
        if self.input_deque:
            return False
        else:
            return True

        # if self.stack:
        #     return False
        # else:
        #     return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna