class Solution(object):
    def maxScore(self, cardPoints, k):
        total=sum(cardPoints)
        window_size=len(cardPoints)-k
        if window_size==0:
            return total
        window=cardPoints[:window_size]
        current_sum=0
        for num in window:
            current_sum+=num
        min_sum=current_sum
        left=0
        for right in range(window_size,len(cardPoints)):
            current_sum=current_sum-cardPoints[left]+cardPoints[right]
            min_sum=min(current_sum,min_sum)
            left+=1
        return total-min_sum
        
            

        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna