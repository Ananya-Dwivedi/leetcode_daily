class Solution(object):
    def reverseVowels(self, s):
        left=0
        right=len(s)-1
        vowels=set('aeiouAEIOU')
        s=list(s)
        
        while left<right:
            while left<right and s[left] not in vowels:
                left+=1
            while left<right and s[right] not in vowels:
                right-=1
            

            s[left],s[right]=s[right],s[left]

            left+=1
            right-=1
        
        return ('').join(s)

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna