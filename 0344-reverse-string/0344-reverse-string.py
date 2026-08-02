class Solution(object):
    def reverseString(self, s):
        #recursive form 

        def reverse(left,right):
            if left >right:
                return 

            s[left],s[right]=s[right],s[left]
            reverse(left+1,right-1)
        
        reverse(0,len(s)-1)
        # left=0
        # right=len(s)-1
        # while left<right:
        #     s[left],s[right]=s[right],s[left]
        #     left+=1
        #     right-=1
        # return s
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna