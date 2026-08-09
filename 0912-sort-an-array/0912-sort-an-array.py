class Solution(object):
    def sortArray(self, nums):
        max_val=max(nums)
        min_val=min(nums)
        
        count=[0]* (max_val-min_val+1)

        for num in nums:
            count[num-min_val]+=1
        
        result=[]

        for num in range(len(count)):
            for i in range(count[num]):
                result.append(num+min_val)
        
        return result

        #simple counting sort 
        # max_val=max(nums)
        
        # count=[0]* (max_val+1)

        # for num in nums:
        #     count[num]+=1
        
        # result=[]

        # for num in range(len(count)):
        #     for i in range(count[num]):
        #         result.append(num)
        
        # return result

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna