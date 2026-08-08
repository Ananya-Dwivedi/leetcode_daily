class Solution(object):
    def maxProduct(self, nums):
        current_max=nums[0]
        current_min=nums[0]
        max_prod=nums[0]

        for i in range(1,len(nums)):
            if nums[i]<0:
        
                current_max,current_min=current_min,current_max
                
            current_max=max(current_max * nums[i],nums[i])        
            current_min=min(current_min * nums[i],nums[i])        
            max_prod=max(max_prod,current_max) 

        return max_prod       

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna