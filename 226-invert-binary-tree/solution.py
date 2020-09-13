# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return

        if root.left is None and root.right is None:
            return root

        right = root.right
        left = root.left
        root.left = self.invertTree(right)
        root.right = self.invertTree(left)

        return root

if __name__ == '__main__':
    s = Solution()

    left2 = TreeNode(1)
    right2 = TreeNode(3)
    left = TreeNode(2, left=left2, right=right2)

    left22 = TreeNode(6)
    right22 = TreeNode(9)
    right = TreeNode(7, left=left22, right=right22)

    root = TreeNode(4, left=left, right=right)

    assert root.val == 4
    assert root.left.val == 2
    assert root.left.left.val == 1
    assert root.left.right.val == 3
    assert root.right.val == 7
    assert root.right.left.val == 6
    assert root.right.right.val == 9

    new_root = s.invertTree(root)

    assert new_root.val == 4
    assert new_root.left.val == 7
    assert new_root.left.left.val == 9
    assert new_root.left.right.val == 6
    assert new_root.right.val == 2
    assert new_root.right.left.val == 3
    assert new_root.right.right.val == 1

    print('Done!')
