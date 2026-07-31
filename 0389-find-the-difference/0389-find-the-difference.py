class Solution(object):
    def findTheDifference(self, s, t):
        
        freq_s={}
        
        for ch in s:
            freq_s[ch]=freq_s.get(ch,0)+1
        
        for ch in t:
            if ch in freq_s:
                if freq_s[ch] ==0:
                    return ch 
                else:
                    freq_s[ch]-=1
            if ch not in freq_s:
                return ch
                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna