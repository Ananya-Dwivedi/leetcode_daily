# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
    

        result = []
        path = []

        def dfs(node):

            if not node:
                return

            # Step 1: Choose
            path.append(str(node.val))

            # Step 2: If leaf, save the current path
            if not node.left and not node.right:
                result.append("->".join(path))
            else:
                # Step 3: Explore
                dfs(node.left)
                dfs(node.right)

            # Step 4: Undo (Backtrack)
            path.pop()

        dfs(root)
        return result

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna