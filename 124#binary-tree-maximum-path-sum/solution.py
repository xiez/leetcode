# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.max_sum = None

    def aux_maxPathSum(self, root):
        print('-------')
        if not root:
            return 0

        left = self.aux_maxPathSum(root.left)
        print('left: %d' % left)
        right = self.aux_maxPathSum(root.right)
        print('right: %d' % right)

        # case1: current node in the path
        max_c1 = max(max(left, right) + root.val, root.val)
        print('c1: %d' % max_c1)

        # case2: current node as root node
        max_c2 = max(left + right + root.val, max_c1)
        print('c2: %d' % max_c2)

        # case3: current node is not included
        if self.max_sum is None:
            self.max_sum = max_c2
        else:
            self.max_sum = max(self.max_sum, max_c2)

        print('sum: %d' % self.max_sum)
        print('++++++++')
        return max_c1

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.aux_maxPathSum(root)
        return self.max_sum


if __name__ == '__main__':
    s = Solution()
    N = TreeNode

    # root = N(10)
    # root.left = N(-15)
    # root.right = N(-7)
    # print(s.maxPathSum(root))

    # root = N(1)
    # root.left = N(1)
    # root.left.left = N(1)
    # print(s.max_sum)

    # root = N(5)
    # root.left = N(4)
    # root.right = N(8)
    # root.left.left = N(11)
    # root.left.left.left = N(7)
    # root.left.left.right = N(2)
    # root.right.left = N(13)
    # root.right.right = N(4)
    # root.right.right = N(1)
    # print(s.maxPathSum(root))

