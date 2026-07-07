class Solution(object):
    def findMiddleIndex(self, nums):
        prefix_sum=[0]*(len(nums)+1)
        for i in range(len(nums)):
            prefix_sum[i+1]=prefix_sum[i]+nums[i]


        total=prefix_sum[len(nums)]
        
        for i in range(len(nums)):
            left_sum=prefix_sum[i]
            right_sum=total-prefix_sum[i+1]
            if left_sum==right_sum:
                return i 
        return -1
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna