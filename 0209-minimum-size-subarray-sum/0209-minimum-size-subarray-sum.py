class Solution(object):
    def minSubArrayLen(self, target, nums):
        left=0
        current_sum=0
        minimum_length=float('inf')
        
        for right in range(len(nums)):
            current_sum+=nums[right]

            while current_sum >= target:
                minimum_length=min(minimum_length,right-left+1)
                current_sum-=nums[left]
                left+=1
            
        if minimum_length == float('inf'):
            return 0
        return minimum_length
            
            

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna