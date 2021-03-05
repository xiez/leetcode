class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        ret = 0
        i = 0
        j = i + 1
        while i < len(s):
            d = {}
            while j < len(s):
                d[s[i]] = 1
            
                if s[j] in d:
                    ret = max(ret, j - i)
                    j = len(s)
                else:
                    d[s[j]] = 1
                    j += 1
                    ret = max(ret, j - i)                    

            i += 1
            j = i + 1
            #print(d)
        return ret            
