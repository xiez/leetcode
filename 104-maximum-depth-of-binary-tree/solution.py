# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == '__main__':
    s = Solution()
    N = TreeNode

    root = N(3)
    root.left = N(9)
    root.right = N(20)
    root.right.left = N(15)
    root.right.right = N(7)
    print(s.maxDepth(root))
    assert s.maxDepth(root) == 3

    print('Done')
