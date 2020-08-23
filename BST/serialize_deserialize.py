# -*- coding: utf-8 -*-
'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
'''
import json
import sys

def insert_node(root, val):
    if val is None:
        return

    if root.val is not None:
        if val < root.val:
            if root.left:
                insert_node(root.left, val)
            else:
                root.left = TreeNode(val)
        elif val > root.val:
            if root.right:
                insert_node(root.right, val)
            else:
                root.right = TreeNode(val)
    else:
        root.val = val

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


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ret = []
        preorder_traverse(root, ret=ret)
        return json.dumps(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        lst = json.loads(data)

        if len(lst) == 0:
            return None

        root = TreeNode(lst[0])
        for e in lst[1:]:
            insert_node(root, e)

        return root

if __name__ == '__main__':
    null = None
    l = [45,30,46,10,36,null,49,8,24,34,42,48,null,4,9,14,25,31,35,41,43,47,null,0,6,null,null,11,20,null,28,null,33,null,null,37,null,null,44,null,null,null,1,5,7,null,12,19,21,26,29,32,null,null,38,null,null,null,3,null,null,null,null,null,13,18,null,null,22,null,27,null,null,null,null,null,39,2,null,null,null,15,null,null,23,null,null,null,40,null,null,null,16,null,null,null,null,null,17]
    k = 1

    root = TreeNode(l[0])
    for e in l[1:]:
        print 'insert %s' % str(e)
        insert_node(root, e)

    preorder_traverse(root)

    # codec = Codec()

    # s = codec.serialize(root)
    # print repr(s)

    # assert False
    # ret = []
    # preorder_traverse(codec.deserialize(s), ret)
    # print repr(ret)

    # print s == ret
