class Solution(object):
    def singleNumber(self, nums):
        # freq={}
        # for n in nums:
        #     freq[n]=freq.get(n,0)+1
        # for key in freq:
        #     if freq[key]==1:
        #         return key

        unique_nums=set()
        for num in nums:
            unique_nums.add(num)
        single=(3*sum(unique_nums) -sum(nums))//2
        return single




            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna