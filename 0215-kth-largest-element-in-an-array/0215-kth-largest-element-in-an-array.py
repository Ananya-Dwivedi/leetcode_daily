class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort(reverse=True)   # Sort in descending order
        return nums[k-1] 
  

#quick sort 
        # # Convert kth largest to index in sorted order
        # k = len(nums) - k

        # def quickselect(left, right):
        #     pivot = nums[right]
        #     p = left
        #     for i in range(left, right):
        #         if nums[i] <= pivot:
        #             nums[i], nums[p] = nums[p], nums[i]
        #             p += 1
        #     nums[p], nums[right] = nums[right], nums[p]

        #     if p == k:
        #         return nums[p]
        #     elif p < k:
        #         return quickselect(p+1, right)
        #     else:
        #         return quickselect(left, p-1)

        # return quickselect(0, len(nums)-1)


#this is what i did experiment on :
        # pos=0
        # n=len(nums)
        # ans=[0]*n
        # low=0
        # for high in range(n-1,-1,-1):
        #     if nums[low]<nums[high]:
        #         ans[pos]=nums[low]
        #         pos+=1
        #         low+=1

        #     else:
        #         ans[pos]=nums[high]
        #         pos+=1

        # return ans
                
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna