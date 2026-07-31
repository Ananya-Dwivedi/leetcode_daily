class Solution(object):
    def topKFrequent(self, words, k):
        freq_words={}

        for word in words:
            freq_words[word]=freq_words.get(word,0)+1
        

        # return freq_words
        sorted_freq=(sorted(freq_words.items(),key=lambda item:(-item[1],item[0])))
        
        ans = []

        for i in range(k):
            ans.append(sorted_freq[i][0])

        return ans
        
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna