# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return TreeNode(val)
        
        current_node = root
        
        while True:
            if current_node.val <= val:
                if current_node.right != None:
                    current_node = current_node.right
                else:
                    current_node.right = TreeNode(val)
                    break;
            else:
                if current_node.left != None:
                    current_node = current_node.left
                else:
                    current_node.left = TreeNode(val)
                    break;
        
        return root
                
        