class Solution(object):
    def runningSum(self, nums):
        total=0
        for num in nums:
            total+=num
        
        for i in range(1,len(nums)):
            nums[i]=nums[i]+nums[i-1]

        return nums


            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna