class Solution(object):
    def containsDuplicate(self, nums):
        seen=set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)

        return False


        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna