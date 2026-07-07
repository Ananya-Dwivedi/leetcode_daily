class Solution(object):
    def missingNumber(self, nums):
       for i in range(len(nums)+1):
            if i not in nums:
                return i
num2=[3,0,1]
result=Solution()
output=result.missingNumber(num2)
print(output)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna