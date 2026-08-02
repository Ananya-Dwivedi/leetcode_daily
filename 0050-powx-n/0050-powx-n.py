class Solution(object):
    def myPow(self, x, n):

        def power(x,n):
            if n<0:
                return 1/power(x,-n)
            if n==0:
                return 1

            half=power(x,n//2)

            if n%2==0:
                return half * half

            else:
                return x*half * half

        return power(x,n)
            
        
        # def power(x,n):


        #     if n==0:
        #         return 1 

        #     return x * power(x,n-1)
        
        # if n<0:
        #     return 1 / power(x,-n)
        # ans=power(x,n)
        # return ans
        
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna