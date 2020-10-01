# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []

        if not root:
            return ret

        ret.append([root])

        while True:
            last = ret[-1]

            next_level = []
            for e in last:
                if not e:
                    continue

                if e.left:
                    next_level.append(e.left)
                if e.right:
                    next_level.append(e.right)

            if not next_level:
                break

            ret.append(next_level)

        vals = []
        for e in ret:
            vals.append([x.val for x in e])

        return vals


if __name__ == '__main__':
    s = Solution()
    N = TreeNode

    root = N(3)
    root.left = N(9)
    root.right = N(20)
    root.right.left = N(15)
    root.right.right = N(7)

    print(s.levelOrder(root))
    assert s.levelOrder(root) == [[3], [9,20], [15,7]]
