class Solution(object):
    def frequencySort(self, s):
 

        freq = {}

        # Count frequency
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Sort characters by frequency
        chars = sorted(freq, key=freq.get, reverse=True)

        # Build result
        result = ""

        for ch in chars:
            result += ch * freq[ch]

        return result
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna