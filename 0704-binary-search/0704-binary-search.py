class Solution(object):
    def search(self, nums, target):
        low=0
        high=len(nums)-1

        while low<=high:
            mid=high-low//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low=mid+1

            else:
                high=mid-1
        return -1



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna