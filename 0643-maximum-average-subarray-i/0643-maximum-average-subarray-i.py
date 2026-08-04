class Solution(object):
    def findMaxAverage(self, nums, k):
        window=nums[:k]
        current_sum=sum(window)
        max_sum=current_sum
        
        left=0
        for right in range(k,len(nums)):
            current_sum=current_sum-nums[left]+nums[right]
            max_sum=max(max_sum,current_sum)
            left+=1

        return float(max_sum)/k


        # max_avg=float("-inf")
        # for i in range(len(nums)):
        #     window=nums[i:k+i]
        #     if len(window)==k:

        #         total=sum(window)
        #         avg=float(total)/k
        #         max_avg=max(avg,max_avg)

        # return max_avg
            

                
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna