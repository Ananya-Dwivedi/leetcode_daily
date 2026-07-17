class Solution(object):
    def scoreOfParentheses(self, s):
        stack=[]
        score=0
        for ch in s:
            if ch =='(':
                stack.append(score)
                score=0
            if ch==')':
                prev_score=stack.pop()
                if score==0:
                    score=prev_score+1
                else:
                    score=prev_score+ 2*score
        return score


        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna