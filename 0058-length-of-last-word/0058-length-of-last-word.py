class Solution(object):
    def lengthOfLastWord(self, s):
        count=0
        words=s.split()
     
        word=words[-1]
        return len(word)


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna