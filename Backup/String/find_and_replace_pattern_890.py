class Solution(object):
    def is_permutation(self, word, pattern):
        letter_map = {}
        value_list = []

        for i in range(len(word)):
            if pattern[i] not in letter_map:
                if word[i] not in value_list:
                    letter_map[pattern[i]] = word[i]
                    value_list.append(word[i])
                else:
                    return False
            else:
                if letter_map.get(pattern[i]) != word[i]:
                    return False

        return True

    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        ret = []
        for word in words:
            if self.is_permutation(word, pattern):
                ret.append(word)

        return ret

if __name__ == '__main__':
    f = Solution().findAndReplacePattern

    words = ["abc","deq","mee","aqq","dkd","ccc"]
    pattern = 'abb'

    print(f(words, pattern))
    assert f(words, pattern) == ["mee", "aqq"]
