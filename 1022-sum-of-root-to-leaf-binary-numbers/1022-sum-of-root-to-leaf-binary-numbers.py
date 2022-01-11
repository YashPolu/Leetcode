# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        root_leaf = 0
        stack = [(root,0)]
        
        while stack:
            root, current = stack.pop()
            if root is not None:
                current = (current << 1) | root.val
                
                if root.left is None and root.right is None:
                    root_leaf += current
                
                else:
                    stack.append((root.left,current))
                    stack.append((root.right,current))
        
        return root_leaf