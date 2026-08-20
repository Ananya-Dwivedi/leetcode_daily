class Solution(object):
    def isPalindrome(self, x):
        sign=-1 if x<0 else 1
        x=abs(x)
        original=x
        reverse=0

        while x!=0:
            digit=x%10
            reverse=reverse*10+digit
            x//=10

        reverse*=sign
        if reverse == original:
            return True
        return False
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna