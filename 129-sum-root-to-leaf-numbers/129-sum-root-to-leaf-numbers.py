# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        
        def helper(node,number):
            
            nonlocal ans
            
            if not node:
                return
            
            number = (number*10) + node.val
            
            if not (node.left or node.right):
                ans+=number
                
            
            helper(node.left,number)
            helper(node.right,number)
            
        
        helper(root,0)
        
        return ans
        