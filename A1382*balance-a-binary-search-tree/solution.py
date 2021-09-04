# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self, node, lst):
        if node is None:
            return
        
        self.inorder(node.left, lst)
        lst.append(node.val)
        self.inorder(node.right, lst)

    def _list_to_tree(self, lst, low, high):
        if low > high:
            return

        mid = (high + low) / 2
        root = TreeNode(lst[mid])
        root.left = self._list_to_tree(lst, low, mid - 1)
        root.right = self._list_to_tree(lst, mid + 1, high)
        return root
    
    def ordered_list_to_balanced_tree(self, lst):
        l, h = 0, len(lst) - 1
        mid = (h + l) / 2
        root = TreeNode(lst[mid])
        root.left = self._list_to_tree(lst, l, mid - 1)
        root.right = self._list_to_tree(lst, mid + 1, h)
        return root
    
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        lst = []
        self.inorder(root, lst)
        #print(lst)        
        
        ret = self.ordered_list_to_balanced_tree(lst)
        return ret
