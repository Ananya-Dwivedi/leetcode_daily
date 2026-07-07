class NumArray(object):

  
    def __init__(self, nums):
       self.prefix=[nums[0]]
      
       for i in range(1,len(nums)):
           self.prefix.append(self.prefix[i-1]+nums[i])

           
           


    def sumRange(self, left, right):
       if left==0:
           return self.prefix[right]
       else:
           return self.prefix[right]-self.prefix[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna