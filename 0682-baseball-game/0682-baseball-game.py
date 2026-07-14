class Solution(object):
    def calPoints(self, operations):
        stack=[]
        for ch in operations:
            
          
            if ch == 'D':
                stack.append(int(stack[-1]+stack[-1]))
            elif ch == 'C':
                stack.pop()
            elif ch == '+' :
                stack.append(int(stack[-1]+stack[-2]))
            else:
                stack.append(int(ch))


        return sum(stack)


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna