class Solution(object):
    def minimumRecolors(self, blocks, k):
        recolor_count=0
        min_recolor=0
        window=blocks[:k]
        for ch in window:
            if ch =="W":
                recolor_count+=1
        min_recolor=recolor_count

        left=0
        for right in range(k,len(blocks)):
            if blocks[left]=='W':
                recolor_count-=1
            if blocks[right]=='W':
                recolor_count+=1
            min_recolor=min(min_recolor,recolor_count)
        
            left+=1
        return min_recolor
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna