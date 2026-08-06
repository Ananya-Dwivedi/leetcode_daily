class Solution(object):
    def smallestNumber(self, n, t):
        prod=1
        num=n
        while num>0:
            last_digit=num%10
            prod*=last_digit
            num//=10
        if prod % t==0:
            return n
        else:
           return self.smallestNumber(n+1,t)            
        # return prod % t

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna