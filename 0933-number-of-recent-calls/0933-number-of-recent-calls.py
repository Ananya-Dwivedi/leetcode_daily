from collections import deque 
class RecentCounter(object):

    def __init__(self):
        self.q=deque()

    
    def ping(self, t):
        
        self.q.append(t)

        while (self.q[0]< t-3000):
            self.q.popleft()
        
        return len(self.q)
                    
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna