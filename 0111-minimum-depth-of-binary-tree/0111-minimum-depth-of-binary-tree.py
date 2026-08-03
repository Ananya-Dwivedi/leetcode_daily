# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        
        if not root:
            return 0
        

        left=self.minDepth(root.left)
        right=self.minDepth(root.right)

        if left==0:
            return 1+right
        
        if right==0:
            return 1+left
        

        return 1 + min(left,right)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna