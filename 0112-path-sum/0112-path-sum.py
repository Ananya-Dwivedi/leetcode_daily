# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        remaining_sum=targetSum-root.val

        if not root.left and not root.right:
            if remaining_sum==0:
                return True

        left=self.hasPathSum(root.left,remaining_sum)
        right=self.hasPathSum(root.right,remaining_sum)
        return left or right
        

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna