class Solution(object):
    def removeOuterParentheses(self, s):
        depth=0
        answer=""
        for char in s:
            if char == '(':
                if depth==0:
                    depth+=1
                else:
                    answer+=char
                    depth+=1
            else:
                    
                if depth==1:
                    depth-=1
                else:
                    depth-=1
                    answer+=char
        return answer


    #     class Solution:
    # def removeOuterParentheses(self, s: str) -> str:

    #     depth = 0
    #     answer = []

    #     for ch in s:

    #         if ch == '(':

    #             if depth > 0:
    #                 answer.append(ch)

    #             depth += 1

    #         else:

    #             depth -= 1

    #             if depth > 0:
    #                 answer.append(ch)

    #     return "".join(answer)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna