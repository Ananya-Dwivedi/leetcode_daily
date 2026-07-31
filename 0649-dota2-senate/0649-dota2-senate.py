from collections import deque
class Solution(object):
    def predictPartyVictory(self, senate):
        n=len(senate)
        radiant=deque()
        dire=deque()
        for i in range(len(senate)):
            if senate[i]=='R':
                radiant.append(i)
            else:
                dire.append(i)

        
        while radiant and dire:
            R_front=radiant[0]
            D_front=dire[0]
            if  R_front < D_front:
                radiant.append(radiant.popleft()+n)
                dire.popleft()
            else:
                dire.append(dire.popleft()+n)
                radiant.popleft()

        if radiant:
            return "Radiant"

        else:
            return "Dire"

        




        

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna