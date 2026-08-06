class Solution(object):
    def longestSubarray(self, nums):
        left=0
        zero_count=0
        ans=0
        count=0
        for right in range(len(nums)):
            if nums[right]==0:
                zero_count+=1
            while zero_count>1:
                if nums[left]==0:
                    zero_count-=1

                
                left+=1
            ans=max(ans,right-left)
        return ans



            

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna