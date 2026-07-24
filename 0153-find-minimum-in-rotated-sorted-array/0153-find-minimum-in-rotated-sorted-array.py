class Solution(object):
    def findMin(self, nums):
        low=0
        high=len(nums)-1
        
        while low <high:
            mid=(low+high)//2
            if nums[mid]> nums[high]:
                low=mid+1
            else:
                high=mid
        return nums[high]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna