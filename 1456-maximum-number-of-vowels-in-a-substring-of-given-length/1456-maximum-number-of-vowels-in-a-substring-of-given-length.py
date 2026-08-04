class Solution(object):
    def maxVowels(self, s, k):
        current_vowel_count=0
        vowels={'a','e','i','o','u'}
        window=s[:k]
        for ch in window :
            if ch in vowels :
                current_vowel_count+=1
        max_count=current_vowel_count
        left=0
        for right in range(k,len(s)):
            if s[left] in vowels:
                current_vowel_count-=1
            
            if s[right] in vowels:
                current_vowel_count+=1
            

            max_count=max(max_count,current_vowel_count)
            left+=1
        return max_count
            



        

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna