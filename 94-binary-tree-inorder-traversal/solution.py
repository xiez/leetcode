# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        self.aux_inorder(root, ret)
        return ret

    def aux_inorder(self, root, ret):
        if not root:
            return

        self.aux_inorder(root.left, ret)
        ret.append(root.val)
        self.aux_inorder(root.right, ret)

        return ret

if __name__ == '__main__':
    s = Solution()
    N = TreeNode

    root = N(1)
    root.right = N(2)
    root.right.left = N(3)

    ret = s.inorderTraversal(root)
    print(ret)
    assert s.inorderTraversal(root) == [1,3,2]
