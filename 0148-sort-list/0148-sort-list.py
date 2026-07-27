# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):

        if not head or not head.next:
            return head

        slow=head
        fast=head.next
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next

        mid=slow.next
        slow.next=None

        left = self.sortList(head)
        right =self.sortList(mid)

        return self.merge(left,right)


    def merge(self,left,right):
        dummy=ListNode()
        tail=dummy

        while left and right:
            
            if left.val<right.val:
                tail.next=left
                left=left.next
      
            else:
                tail.next=right
                right=right.next
            

            tail = tail.next

        
        if left:
            tail.next = left
        else:
            tail.next = right

        return dummy.next






# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna