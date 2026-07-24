# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        if n==1:
            return 1

        answer=n
        low=1
        high=n
        while low<=high:
            mid=(low+high)//2

            if isBadVersion(mid) == False:
                low=mid+1
            else:
                answer=mid
                high=mid-1
        
        return answer

        
                    
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna