class Solution(object):
    def countOdds(self, low, high):
        # count=0
        # while low<=high:
        #     if low%2!=0:
        #         count+=1
        #     low+=1
        # return count
        
        if high%2==0 and low%2==0:
            return (high-low)//2
        else:
            return (high-low)//2 +1

            
         
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna