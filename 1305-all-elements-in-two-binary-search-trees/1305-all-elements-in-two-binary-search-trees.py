# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preod(self,rot):
        if not rot:
            return []
        stack = [rot,]
        result = list()
        
        
        while stack:
            node=stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        return result
        
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        output = self.preod(root1)
        
        output.extend(self.preod(root2))
        
        return sorted(output)
        