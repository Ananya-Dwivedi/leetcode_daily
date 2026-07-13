class Solution(object):
    def maxDepth(self, s):
        depth=0
        maximum=0
        for char in s:
            if not char.isdigit():
                if char == '(':
                    depth+=1
                    maximum=max(maximum,depth)
                elif char ==')':
                    depth-=1
                else:
                    continue
        return maximum
            


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna