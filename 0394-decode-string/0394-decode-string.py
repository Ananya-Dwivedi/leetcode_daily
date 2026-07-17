class Solution(object):
    def decodeString(self, s):
        current=""
        stack=[]
        number=0
        for ch in s:
            if ch.isdigit():
                number=number*10+int(ch)
            elif ch == '[':
                stack.append((current,number))
                current=""
                number=0
            elif ch.isalpha():
                current+=ch
            else:
                previous_str,repeat=stack.pop() 
                current=previous_str+current * repeat
        return current       
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna