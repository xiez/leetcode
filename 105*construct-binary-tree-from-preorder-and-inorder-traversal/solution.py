# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        assert len(preorder) == len(inorder)

        if not preorder or not inorder:
            return None

        if len(preorder) == 1 and len(inorder) == 1:
            assert preorder[0] == inorder[0]
            n = TreeNode(preorder[0])
            return n

        root = TreeNode(preorder[0])

        idx = inorder.index(preorder[0])
        left_preorder = preorder[1: idx + 1]
        left_inorder = inorder[0: idx]
        right_preorder = preorder[idx + 1:]
        right_inorder = inorder[idx + 1:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root

    def aux_traverse(self, root, res):
        if not root:
            return

        if root.left:
            self.aux_traverse(root.left, res)
        res.append(root.val)
        if root.right:
            self.aux_traverse(root.right, res)

    def traverse(self, root):
        res = []
        self.aux_traverse(root, res)
        return res

if __name__ == '__main__':
    s = Solution()

    pre_od = [3,9,20,15,7]
    in_od = [9,3,15,20,7]

    root = s.buildTree(pre_od, in_od)
    print(s.traverse(root))

    assert root.val == 3
    assert root.left.val == 9
