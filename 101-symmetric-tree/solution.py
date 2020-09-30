# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        return self.is_mirror(root.left, root.right)

    def is_mirror(self, tree1, tree2):
        if tree1 is None and tree2 is None:
            return True

        if tree1 and tree2 is None:
            return False

        if tree2 and tree1 is None:
            return False

        if tree1.val != tree2.val:
            return False

        return self.is_mirror(tree1.left, tree2.right) and \
            self.is_mirror(tree1.right, tree2.left)

    def aux_traverse(self, root, res):
        if root.left is None and root.right is None:
            res.append(root.val)
            return

        if root.left:
            self.aux_traverse(root.left, res)
        else:
            res.append('-')
        res.append(root.val)
        if root.right:
            self.aux_traverse(root.right, res)
        else:
            res.append('-')

    def traverse(self, root):
        res = []
        self.aux_traverse(root, res)
        return res

if __name__ == '__main__':
    s = Solution()
    N = TreeNode

    root = N(1)
    root.left = N(2)
    root.right = N(2)
    root.left.left = N(2)
    root.left.right = N(4)
    root.right.left = N(4)
    root.right.right = N(2)

    print(s.traverse(root))
    assert s.isSymmetric(root) is True

    print('Done')
