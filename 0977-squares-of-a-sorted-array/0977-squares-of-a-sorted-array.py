class Solution(object):
    def sortedSquares(self, nums):
        
        for i in range(len(nums)):
            nums[i]=nums[i]**2

        nums.sort()

        return nums
    

    # def mergesort(nums):

    #     mid=len(nums)//2

    #     left=mergesort(nums[:mid])
    #     right=mergesort(nums[mid:])

    #     merge(left,right)

    # def merge(left,right):
    #     ans=[]
    #     i=0
    #     j=0

    #     while i<len(left) and j<len(right):
    #         if left[i]<right[j]:
    #             ans.append(left[i])
    #             left+=1
    #         else:
    #             ans.append(right[j])
    #             j-=1
        
    #     while i<len(left):
    #         ans.append(left[i])
    #         i+=1

    #     while j<len(right):
    #         ans.append(right[i])
    #         j+=1

    #     return ans


        
        
            


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna