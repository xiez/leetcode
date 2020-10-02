class Trie:

    class Node:
        def __init__(self, end_of_word=False):
            self.children = [None] * 26
            self.end_of_word = end_of_word

        def __repr__(self):
            return '/' if self.end_of_word else '*'

    def __init__(self):
        self.root = self.Node()

    def _char2index(self, char):
        """lower-case character to index, e.g. a -> 0"""
        return ord(char) - ord('a')

    def insert(self, word):
        cur_node = self.root
        for ch in word:
            idx = self._char2index(ch)
            if cur_node.children[idx] is None:
                cur_node.children[idx] = self.Node()

            cur_node = cur_node.children[idx]
        cur_node.end_of_word = True

    def search(self, word):
        cur_node = self.root
        for ch in word:
            idx = self._char2index(ch)
            if cur_node.children[idx] is None:
                return False
            cur_node = cur_node.children[idx]

        return cur_node.end_of_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur_node = self.root
        for ch in prefix:
            idx = self._char2index(ch)
            if cur_node.children[idx] is None:
                return False
            cur_node = cur_node.children[idx]

        return True

    def aux_traverse(self, root):
        if root is None:
            return

        print(root.children)

        for child in root.children:
            self.aux_traverse(child)

    def traverse(self):
        cur_node = self.root
        return self.aux_traverse(cur_node)


if __name__ == '__main__':
    t = Trie()

    t.insert('a')
    t.insert('ba')
    t.insert('baa')

    # t.traverse()

    print(t.search('a'))
    print(t.search('b'))
    print(t.search('ba'))
    print(t.startsWith('b'))
    print(t.startsWith('ba'))
    print(t.startsWith('baa'))
    print(t.startsWith('baaa'))
