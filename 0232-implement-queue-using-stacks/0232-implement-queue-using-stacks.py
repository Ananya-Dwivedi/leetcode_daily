class MyQueue(object):

    def __init__(self):
        self.my_queue=[]

    def push(self, x):
        
            self.my_queue.append(x)
    

    def pop(self):
        if not self.my_queue:
            return null
        popped_element= self.my_queue[0]
        for i in range(1,len(self.my_queue)):
            self.my_queue[i-1]=self.my_queue[i]
        return popped_element

      
    def peek(self):
        return self.my_queue[0]
        
    def empty(self):
        if  self.my_queue:
            return False
                


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna