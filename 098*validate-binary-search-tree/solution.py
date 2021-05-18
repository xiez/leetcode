# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = None
        
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        if self.isValidBST(root.left) is False:
            return False
        
        if self.prev is None:
            self.prev = root.val
        else:
            if root.val <= self.prev:
                return False
            else:
                self.prev = root.val
            
        if self.isValidBST(root.right) is False:
            return False
        
        return True

