# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def height(self, root):
        if root is None:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))

    def isSymArray(self, arr):
        if len(arr) == 0:
            return True

        if arr[0] != arr[-1]:
            return False

        return self.isSymArray(arr[1:-1])

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        if self.height(root.left) != self.height(root.right):
            return False

        arr = self.traverse(root)
        return True if self.isSymArray(arr) else False

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
    root.right.left = N(2)
    # root.right.right = N(3)

    print(s.traverse(root))
    assert s.isSymmetric(root) is False

    assert s.isSymArray([]) is True
    assert s.isSymArray(['-', 1, 3, 1, '-']) is True
    assert s.isSymArray(['-', 1, 3, '-']) is False

    print('Done')
