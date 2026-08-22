# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        
        length=0
        current=head
        while current:
            length+=1
            current=current.next

        k=k%length
        while k>0:
            last=head
            sec_last=None

            while last.next:
                sec_last=last
                last=last.next
            
            sec_last.next=None
            last.next=head
            
    
            head=last

            k-=1
        return head

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna