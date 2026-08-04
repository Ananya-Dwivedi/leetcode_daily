class Solution(object):
    def maximumSubarraySum(self, nums, k):
        
        current_sum=0
        freq_count={}
        for i in range(k):
            current_sum+=nums[i]
            freq_count[nums[i]]=freq_count.get(nums[i],0)+1
        max_sum=0
        if len(freq_count)==k:
            max_sum=current_sum

        
        left=0
        for right in range(k,len(nums)):
            outgoing=nums[left]
            current_sum-=outgoing

            
            freq_count[outgoing]-=1
            if freq_count[outgoing]==0:
                del freq_count[outgoing]
            
            incoming=nums[right]
            current_sum+=incoming
            freq_count[incoming]=freq_count.get(incoming,0)+1

            if len(freq_count)==k:
                max_sum=max(max_sum,current_sum)
            
            left+=1
        return max_sum
        #     freq_count.pop(nums[left])
        #     freq_count[nums[right]]=freq_count.get(nums[right],0)+1
        #     if list((freq_count).values()) != unique_val:
        #         current_sum=sum(list((freq_count).keys()))
            

        #     max_sum=max(max_sum,current_sum)
        #     left+=1
        # return max_sum






        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna