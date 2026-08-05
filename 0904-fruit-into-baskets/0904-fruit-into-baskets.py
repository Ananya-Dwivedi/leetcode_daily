class Solution(object):
    def totalFruit(self, fruits):
        freq={}
        left=0
        ans=0
        window_length=0
        for right in range(len(fruits)):
            freq[fruits[right]]=freq.get(fruits[right],0)+1
            window_length+=1

            while len(freq) >2:
                freq[fruits[left]]-=1
                if freq[fruits[left]]==0:
                    del freq[fruits[left]]
                window_length-=1
                
                left+=1
            ans=max(ans,window_length)
        return ans 
            
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna