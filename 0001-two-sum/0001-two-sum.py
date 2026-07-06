class Solution(object):
    def twoSum(self, nums, target):
     
        seen={}
        for i in range(len(nums)):
            complement =target-nums[i]

            if complement in seen:
                return ([seen[complement],i])
                

            seen[nums[i]]=i
                   
nums=[2,7,11,15]
target=9
Add_Sum=Solution()
print(Add_Sum.twoSum(nums,target))            
    
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna