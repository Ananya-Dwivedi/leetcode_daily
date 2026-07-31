from collections import deque
class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        q=deque()
        for i in range(len(tickets)):
            q.append((tickets[i],i))

        time=0

        while q:
            ticket,index=q.popleft()

            ticket-=1
            time+=1

            if ticket == 0 and index==k:
                break

            if ticket> 0:
                q.append((ticket,index))

        return time       


        
        
        # time=0
        # rotation=0
        # while need != 0:
             
        #     time+=1
        #     front=tickets.popleft()
        #     if front==1:
        #         pass
        #     else:
        #         tickets.append(front-1)
        #     rotation+=1
        #     if len(tickets)==l and  rotation == k+1:
        #         need-=1
        #         rotation=0
        
        # return time







        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna