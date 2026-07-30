# from collections import deque
class MyQueue(object):

    def __init__(self):
        self.input_stack=[]
        self.output_stack=[]
        # self.my_queue=deque()

    def push(self, x):
        
            self.input_stack.append(x)
     
            # self.my_queue.append(x)
    

    def pop(self):

        if not self.output_stack:
            
            while self.input_stack:
                popped_element=self.input_stack.pop()
                self.output_stack.append(popped_element)
            return  self.output_stack.pop()
        
        else:
            return  self.output_stack.pop()


        # if not self.my_queue:
        #     return None
        # return self.my_queue.popleft()
        # popped_element= self.my_queue[0]
        # for i in range(1,len(self.my_queue)):
        #     self.my_queue[i-1]=self.my_queue[i]
        # self.my_queue.pop()
        
        # return popped_element

      
    def peek(self):
        if not self.output_stack:
            
            while self.input_stack:

                self.output_stack.append(self.input_stack.pop())
            return  self.output_stack[-1]
        
        else:
            return  self.output_stack[-1]

        # return self.my_queue[0]
        
    def empty(self):
        if not self.input_stack and not self.output_stack:
            return True
        else:
            return False
        # if  self.my_queue:
        #     return False
        # return True
                


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna