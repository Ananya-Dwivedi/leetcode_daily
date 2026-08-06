class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        left=0
        curr_len=0
        max_len=curr_len
        for right in range(len(nums)):
            if nums[right]==1:
                curr_len+=1
            else:
                max_len=max(curr_len,max_len)
                curr_len=0
                continue
            max_len=max(curr_len,max_len)
        return max_len
            
                
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna