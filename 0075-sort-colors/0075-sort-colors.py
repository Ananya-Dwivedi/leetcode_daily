class Solution(object):
    def sortColors(self, nums):
        left=0
        mid=0
        right=len(nums)-1
        while mid <=right:
            if nums[mid]==2:
                nums[mid],nums[right]=nums[right],nums[mid]
                right-=1
            
            elif nums[ mid]==1:
                mid+=1
            else:
                nums[mid],nums[left]=nums[left],nums[mid]
                left+=1
                mid+=1
        return nums
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna