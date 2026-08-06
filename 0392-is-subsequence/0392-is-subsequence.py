class Solution(object):
    def isSubsequence(self, s, t):
        if len(s)==0:
            return True
        left_s=0
        
        for left_t in range(len(t)):
            if t[left_t]==s[left_s]:
                left_s+=1

            if left_s==len(s):
                return True
            
        return False
            
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna