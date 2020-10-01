# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        self.aux_postorder(root, ret)
        return ret

    def aux_postorder(self, root, ret):
        if not root:
            return

        self.aux_postorder(root.left, ret)
        self.aux_postorder(root.right, ret)
        ret.append(root.val)
        return ret

if __name__ == '__main__':
    s = Solution()
    N = TreeNode

    root = N(1)
    root.right = N(2)
    root.right.left = N(3)

    ret = s.postorderTraversal(root)
    print(ret)
    # assert s.postorderTraversal(root) == [3,2,1]
