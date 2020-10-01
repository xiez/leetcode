# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
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
        left_to_right = 1
        for e in ret:
            iter = e if left_to_right == 1 else reversed(e)
            vals.append([x.val for x in iter])
            left_to_right = left_to_right * -1

        return vals


if __name__ == '__main__':
    s = Solution()
    N = TreeNode

    root = N(3)
    root.left = N(9)
    root.right = N(20)
    root.right.left = N(15)
    root.right.right = N(7)

    print(s.zigzagLevelOrder(root))
    assert s.zigzagLevelOrder(root) == [[3], [20,9], [15,7]]
