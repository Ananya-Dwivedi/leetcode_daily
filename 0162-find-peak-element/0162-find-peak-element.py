class Solution(object):
    def findPeakElement(self, nums):
        low=0
        high=len(nums)-1
        while low<high:
            mid=(low+high)//2
            if nums[mid]<nums[mid+1]:
                low=mid+1
            else:
                high=mid

        return high
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna