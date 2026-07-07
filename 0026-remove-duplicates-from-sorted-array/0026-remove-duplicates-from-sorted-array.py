class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1  


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
result = Solution()
output = result.removeDuplicates(nums)
print("The unique numbers are" ,output, " and the array is ",nums[:output])

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna