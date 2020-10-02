# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def aux_inorder(self, root, ret):
        if not root:
            return

        self.aux_inorder(root.left, ret)
        ret.append(root.val)
        self.aux_inorder(root.right, ret)

    def inorder(self, root):
        ret = []
        self.aux_inorder(root, ret)
        return ret

    def inline_replace(self, root, d):
        if not root:
            return

        root.val = d[root.val]
        self.inline_replace(root.left, d)
        self.inline_replace(root.right, d)

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        keys = self.inorder(root)
        vals = sorted(keys)

        d = {}
        for k, v in zip(keys, vals):
            d[k] = v

        self.inline_replace(root, d)


if __name__ == '__main__':
    s = Solution()
    N = TreeNode

    root = N(3)
    root.left = N(1)
    root.right = N(4)
    root.right.left = N(2)

    # print(s.inorder(root))
    print(s.inorder(root))
    s.recoverTree(root)
    print(s.inorder(root))
