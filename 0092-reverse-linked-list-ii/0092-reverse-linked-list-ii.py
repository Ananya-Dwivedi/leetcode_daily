# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        if not head or left==right:
            return head
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        
        for i in range(left-1):
            prev=prev.next
        
        current=prev.next
        reverse_prev=None

        for i in range(right-left+1):
            next_node=current.next
            current.next=reverse_prev
            reverse_prev=current
            current=next_node

        tail=prev.next

        prev.next=reverse_prev
        tail.next=current
    
        return dummy.next

    

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna