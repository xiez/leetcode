class WordDictionary(object):

    class Node:
        def __init__(self, end_of_word=False):
            self.children = [None] * 26
            self.end_of_word = end_of_word

        def __repr__(self):
            return '/' if self.end_of_word else '*'

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node()

    def _char2index(self, char):
        """lower-case character to index, e.g. a -> 0"""
        return ord(char) - ord('a')

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        cur_node = self.root
        for ch in word:
            idx = self._char2index(ch)
            if cur_node.children[idx] is None:
                cur_node.children[idx] = self.Node()
            cur_node = cur_node.children[idx]

        cur_node.end_of_word = True

    def searchWord(self, word):
        cur_node = self.root
        for ch in word:
            idx = self._char2index(ch)
            if cur_node.children[idx] is None:
                return False
            cur_node = cur_node.children[idx]

        return cur_node.end_of_word

    def searchDot(self, word):
        cur_nodes = [self.root]
        for ch in word:
            next_nodes = []
            if ch == '.':
                for cur_node in cur_nodes:
                    for e in cur_node.children:
                        if e is None:
                            continue
                        next_nodes.append(e)

                cur_nodes = next_nodes
            else:
                idx = self._char2index(ch)
                for cur_node in cur_nodes:
                    if cur_node.children[idx] is None:
                        continue
                    next_nodes.append(cur_node.children[idx])

                cur_nodes = next_nodes

        return any([e.end_of_word for e in cur_nodes]) is True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if '.' in word:
            return self.searchDot(word)
        else:
            return self.searchWord(word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
if __name__ == '__main__':
    t = WordDictionary()
    t.addWord('b')
    t.addWord('bad')
    t.addWord('badd')
    print(t.search('bad'))
    print(t.search('ba'))
    print(t.search('bad.'))
