class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack=[]
        answer=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                previous_index=stack.pop()
                answer[previous_index]=i-previous_index

                
            stack.append(i)
        return answer
            

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna