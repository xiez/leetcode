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

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        if self.isBalanced(root.left) and self.isBalanced(root.right):
            l_h = self.height(root.left)
            r_h = self.height(root.right)
            if abs(l_h - r_h) <= 1:
                return True
            else:
                return False
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    N = TreeNode

    root = N(3)
    root.left = N(9)
    root.right = N(20)
    root.right.left = N(15)
    root.right.right = N(7)
    print(s.height(root))
    assert s.isBalanced(root) is True

    root = N(1)
    root.left = N(2)
    root.right = N(2)
    root.left.left = N(3)
    root.left.right = N(3)
    root.left.left.left = N(4)
    root.left.left.right = N(4)
    print(s.height(root))
    assert s.isBalanced(root) is False

    root = N(1)
    root.left = N(2)
    root.right = N(2)
    root.left.left = N(3)
    root.right.right = N(3)
    root.left.left.left = N(4)
    root.right.right.right = N(4)
    print(s.height(root))
    assert s.isBalanced(root) is False

    print('Done!')
