# -*- coding: utf-8 -*-

'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insert(self, val):
        if val is None:
            return

        if self.val:
            if val < self.val:
                if self.left:
                    self.left.insert(val)
                else:
                    self.left = TreeNode(val)
            elif val > self.val:
                if self.right:
                    self.right.insert(val)
                else:
                    self.right = TreeNode(val)
        else:
            self.val = val

    def inorder_traverse(self, ret=[]):
        def _inorder_traverse(node, path=None):
            if node is None:
                return

            _inorder_traverse(node.left, path)
            if path is not None:
                path.append(node.val)
            else:
                print node.val
            _inorder_traverse(node.right, path)

        _inorder_traverse(self, ret)
        return ret

def inorder_traverse(node, ret=[]):
    def _inorder_traverse(node, path=[]):
        if node is None:
            return

        _inorder_traverse(node.left, path)
        if path is not None:
            path.append(node.val)
        else:
            print node.val
        _inorder_traverse(node.right, path)

    _inorder_traverse(node, ret)
    return ret


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        ret = []
        inorder_traverse(root, ret=ret)

        print ret
        return ret[k - 1]


if __name__ == '__main__':
    # l = [5, 3, 6, 2, 4, None, None, 1]
    # k = 5
    null = None
    l = [41,37,44,24,39,42,48,1,35,38,40,null,43,46,49,0,2,30,36,null,null,null,null,null,null,45,47,null,null,null,null,null,4,29,32,null,null,null,null,null,null,3,9,26,null,31,34,null,null,7,11,25,27,null,null,33,null,6,8,10,16,null,null,null,28,null,null,5,null,null,null,null,null,15,19,null,null,null,null,12,null,18,20,null,13,17,null,null,22,null,14,null,null,21,23]
    k = 1

    root = TreeNode(l[0])
    for e in l[1:]:
        root.insert(e)

    print Solution().kthSmallest(root, k)
