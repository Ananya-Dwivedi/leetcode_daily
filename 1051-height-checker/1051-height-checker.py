class Solution(object):
    def heightChecker(self, heights):
        max_val=max(heights)

        count=[0]* (max_val+1)
    
        for height in heights:
            count[height]+=1

        result=[]

        for i in range(len(count)):
            for _ in range(count[i]):
                result.append(i)

        ans=0
        for i in range(len(result)):
            if result[i]!=heights[i]:
                ans+=1
        
        return ans
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna