class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def traverse(self, ):
        if self.left:
            self.left.traverse()

        print(self.val)

        if self.right:
            self.right.traverse()


class Tree:
    def __init__(self, ):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)

        if self.root.val > val:
            if self.root.left is None:
                self.root.left = TreeNode(val)
            else:
                self.root.left.insert(val)
        elif self.root.val < val:
            if self.root.right is None:
                self.root.right = TreeNode(val)
            else:
                self.root.right.insert(val)

if __name__ == '__main__':
    t = Tree()

    t.insert(9)
    t.insert(8)
    t.insert(10)

    t.root.traverse()
