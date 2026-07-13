class Solution(object):
    def removeDuplicates(self, s):
        stack=[]
        for char in s:
            if (stack and char == stack[-1]):
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna