"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        if not head :
            return None
        old_to_new={None:None}

        current=head

        while current:
            copy=Node(current.val)
            old_to_new[current]=copy
            current=current.next

        current=head
        while current:
            copy=old_to_new[current]
            copy.next=old_to_new[current.next]
            copy.random=old_to_new[current.random]
            current=current.next
        return old_to_new[head]


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna