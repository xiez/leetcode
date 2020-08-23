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
import copy
import random
import sys
from random import shuffle

# Utility functions
def insert_node(root, val):
    if val is None:
        return

    if root.val is not None:
        if val < root.val:
            if root.left:
                root.left.insert(val)
            else:
                root.left = TreeNode(val)
        elif val > root.val:
            if root.right:
                root.right.insert(val)
            else:
                root.right = TreeNode(val)
    else:
        root.val = val


def inorder_traverse(node, ret=None):
    def _inorder_traverse(node, path=[]):
        if node is None:
            return

        _inorder_traverse(node.left, path)
        if path is not None:
            path.append(node.val)
        else:
            sys.stdout.write('%d ' % node.val)
        _inorder_traverse(node.right, path)

    _inorder_traverse(node, ret)
    return ret

def preorder_traverse(node, ret=None):
    def _preorder_traverse(node, path=[]):
        if node is None:
            return

        if path is not None:
            path.append(node.val)
        else:
            sys.stdout.write('%d ' % node.val)
        _preorder_traverse(node.left, path)
        _preorder_traverse(node.right, path)

    _preorder_traverse(node, ret)
    return ret

def tree_node_to_json(node):
    if node is None:
        return

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

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
        inorder_traverse(self, ret=ret)

    def preorder_traverse(self, ret=[]):
        preorder_traverse(self, ret=ret)

    def postorder_traverse(self, ret=[]):
        def _postorder_traverse(node, path=[]):
            if node is None:
                return

            _postorder_traverse(node.left, path)
            _postorder_traverse(node.right, path)
            if path:
                path.append(node.val)
            else:
                print node.val

        _postorder_traverse(self, ret)
        return ret

    def print_tree(self):
        def test(lst):
            ret = False
            for ele in lst:
                if not ele:
                    continue

                if ele.left or ele.right:
                    ret = True
                    break
            return ret

        def println(lst, padding=0):
            for ele in lst:
                sys.stdout.write(' ' * padding)
                sys.stdout.write(str(ele.val) if ele else '*')

            print

        l = []
        n = []
        ret = []
        l.append(self)

        while(test(l)):
            ret.append(l)

            for x in l:
                if not x:
                    n.append(None)
                    n.append(None)
                    continue

                n.append(x.left)
                n.append(x.right)

            l = n
            n = []

        ret.append(l)

        for i in range(len(ret)):
            padding = 2 ** (len(ret) - 1) * 2 / (len(ret[i]) + 1)
            # print padding
            println(ret[i], padding)


class BST(object):
    def __init__(self, l=[]):
        self.root = None
        self._size = 0

    def swap_childrent(self, node):
        s = node.left
        node.left = node.right
        node.right = s

    def insert(self, val):
        self.root = self._insert_node(self.root, val)

    def _insert_node(self, node, val):
        if node is None:
            self._size += 1
            return TreeNode(val)

        if val < node.val:
            if node.left:
                self._insert_node(node.left, val)
            else:
                self._size += 1
                new_node = TreeNode(val)
                new_node.parent = node
                node.left = new_node
        elif val > node.val:
            if node.right:
                self._insert_node(node.right, val)
            else:
                self._size += 1
                new_node = TreeNode(val)
                new_node.parent = node
                node.right = new_node
        return node

    def size(self):
        return self._size

    def min_value(self):
        def _min_value(node):
            if node is None:
                return

            if node.left:
                return _min_value(node.left)

            return node.val

        return _min_value(self.root)

    def max_value(self):
        def _max_value(node):
            if node is None:
                return

            if node.right:
                return _max_value(node.right)

            return node.val

        return _max_value(self.root)

    def is_bst(self):
        def _is_bst(node, min_val=None, max_val=None):
            if node is None:
                return

            _is_bst(node.left)
            _is_bst(node.right)

            if node.left and node.left.val > node.val:
                return False

            if node.right and node.right.val < node.val:
                return False

            return True

        return bool(_is_bst(self.root))

    def max_depth(self):
        def _max_depth(node):
            if node is None:
                return 0
            else:
                l_depth = _max_depth(node.left)
                r_depth = _max_depth(node.right)

                return l_depth + 1 if (l_depth > r_depth) else r_depth + 1

        return _max_depth(self.root)

    def list_paths(self):
        """Root-to-leaf paths

        http://cslibrary.stanford.edu/110/BinaryTrees.html
        """

        ret = []
        self._list_paths(self.root, ret=ret)
        return ret

    def _list_paths(self, node, paths=[], ret=[]):
        if node is None:
            return

        paths.append(node.val)
        self._list_paths(node.left, ret=ret)

        if node.left is None and node.right is None:
            ret.append(copy.copy(paths))

        self._list_paths(node.right, ret=ret)
        paths.pop()

    def mirror(self):
        self._mirror(self.root)

    def _mirror(self, node):
        if node is None:
            return

        self._mirror(node.left)
        self._mirror(node.right)

        if node.left is None and node.right is None:
            return
        else:
            self.swap_childrent(node)

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

    def inorder_traverse(self):
        self._inorder_traverse(self.root)

    def _inorder_traverse(self, node, paths=[]):
        if node is None:
            return

        self._inorder_traverse(node.left)
        print node.val
        self._inorder_traverse(node.right)

    def preorder_traverse(self):
        self._preorder_traverse(self.root)

    def _preorder_traverse(self, node):
        if node is None:
            return

        print node.val
        self._preorder_traverse(node.left)
        self._preorder_traverse(node.right)

    def postorder_traverse(self):
        self._postorder_traverse(self.root)

    def _postorder_traverse(self, node):
        if node is None:
            return

        self._postorder_traverse(node.left)
        self._postorder_traverse(node.right)
        print node.val

    def print_tree(self):
        def test(lst):
            ret = False
            for ele in lst:
                if not ele:
                    continue

                if ele.left or ele.right:
                    ret = True
                    break
            return ret

        def println(lst, padding=0):
            for ele in lst:
                sys.stdout.write(' ' * padding)
                sys.stdout.write(str(ele.val) if ele else '*')

            print

        l = []
        n = []
        ret = []
        l.append(self.root)

        while(test(l)):
            ret.append(l)

            for x in l:
                if not x:
                    n.append(None)
                    n.append(None)
                    continue

                n.append(x.left)
                n.append(x.right)

            l = n
            n = []

        ret.append(l)

        for i in range(len(ret)):
            padding = 2 ** (len(ret) - 1) * 2 / (len(ret[i]) + 1)
            # print padding
            println(ret[i], padding)

class Solution(object):
    def test(self, l):
        t = BST()

        for i in l:
            t.insert(i)

        # # # print t.list_paths()
        t.print_tree()

        # t.inorder_traverse()
        # print '--------'
        # t.postorder_traverse()
        # print '--------'
        # t.preorder_traverse()

        # t.print_tree()

        # print t.min_value()
        # print t.max_value()
        # t.inorder_traverse()

        # print(t.search(0))
        # print t.size()
        # print t.max_depth()
        print t.is_bst()

        t.mirror()
        print '--------'

        print t.is_bst()

        # print t.list_paths()

        # v = random.randint(0, 100)
        # print '%d in the tree ? %s'  % (v, str(t.search(v)))

        # print t.delete(-4)

    def sortedListToBST(self, head=None):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # l = [ 1, 2,3, 4, 5]#, 6, 7, 8, 9, 0, -1, -2, -3, -4]
        l = [ 3,1,2, 4, 5, 6, 7]#, 8, 9, 0, -1, -2, -3, -4]

        for _ in range(1):
            shuffle(l)
            self.test(l)

if __name__ == '__main__':
    print 'start test'
    # Solution().sortedListToBST()

    l = [1,2,3,4,5,6]
    shuffle(l)

    root = TreeNode(l[0])
    for e in l[1:]:
        root.insert(e)

    root.print_tree()

    ret = []
    root.preorder_traverse(ret=ret)
    print ret

    root2 = TreeNode(ret[0])
    for e in ret[1:]:
        root2.insert(e)

    root2.print_tree()
    # root2 = TreeNode(8)
    # root2.insert(4)
    # root2.insert(-1)
    # root2.insert(10)
    # root2.print_tree()
    # root.preorder_traverse()
    # root.postorder_traverse()
