# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        dummy_small=ListNode()
        small=dummy_small
        dummy_large=ListNode()
        large=dummy_large
    
        current=head
        while current:
            if current.val <x:
                small.next=current
                small=small.next
            else:
                large.next=current
                large=large.next

            current=current.next

        small.next=dummy_large.next
        large.next=None
        return dummy_small.next
        
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna