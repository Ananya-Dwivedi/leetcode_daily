# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
    
        if not p and  not q:
            return  True
        if  not q or not p :
            return False          

        if p.val !=q.val:
            return False
   
        left=self.isSameTree(p.left,q.left)
        right=self.isSameTree(p.right,q.right)
        
        return left and right
        



                

        

         
        


        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna