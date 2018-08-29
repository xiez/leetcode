'''
Given a singly linked list where elements are sorted in ascending order, 
convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in 
which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following 
height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

'''
import random
import sys
from random import shuffle

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, l=[]):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self._insert_node(self.root, val)

    def _insert_node(self, node, val):
        if node is None:
            return TreeNode(val)

        if val < node.val:
            if node.left:
                self._insert_node(node.left, val)
            else:
                node.left = TreeNode(val)
        elif val > node.val:
            if node.right:
                self._insert_node(node.right, val)
            else:
                node.right = TreeNode(val)

    def search(self, val):
        return self._search(self.root, val)

    def _search(self, node, val):
        if node is None:
            return False

        if node.val == val:
            return True
        elif node.val < val:
            return self._search(node.right, val)
        else:
            return self._search(node.left, val)

    def delete(self, val):
        return self._delete(self.root, val)

    def _delete(self, node, val):
        if node is None:
            return

        if node.val == val:
            # no children
            if node.left is None and node.right is None:
                node = None
                return val

            # one child
            elif node.left is None or node.right is None:
                node = node.left if node.left else node.right
                return val

            # two children
            else:
                assert False, 'not implement'

        elif node.val < val:
            return self._delete(node.right, val)
        else:
            return self._delete(node.left, val)

    def traverse_binary_tree(self, node, func):
        if node is None:
            return
        self.traverse_binary_tree(node.left, func)
        func('%d ' % node.val )
        self.traverse_binary_tree(node.right, func)

    def println(self):
        cb = sys.stdout.write
        self.traverse_binary_tree(self.root, cb)
        print

class Solution(object):
    def test(self, l):
        t = BST()

        for i in l:
            t.insert(i)

        t.println()

        # v = random.randint(0, 100)
        # print '%d in the tree ? %s'  % (v, str(t.search(v)))

        print t.delete(-4)
        t.println()

    def sortedListToBST(self, head=None):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        l = [ 1, 2,3, 4, 5, 6, 7, 8, 9, 0, -1, -2, -3, -4]

        for _ in range(1):
            shuffle(l)
            self.test(l)

if __name__ == '__main__':
    print 'start test'
    Solution().sortedListToBST()
        



