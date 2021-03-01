import time

class Solution(object):
    def __init__(self):
        self.max_point = (0, 0)
        self.max = 0

    def update_max_point(self, row, col):
        if col - row > self.max:
            self.max_point = (row, col)
            # self.max = col - row

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        len_s = len(s)

        c1 = time.time()
        dp_table = [[0] * len_s for _ in xrange(len_s)]
        c2 = time.time()
        print('c2-c1:', c2-c1)

        row = 0
        delta = 0
        row_max = len_s

        cc = 0
        for i in xrange(5000):
            cc += 1

        # while row < row_max:
        #     col = row + delta
        #     while True:
        #         if row >= len_s or col >= len_s:
        #             row = 0
        #             break

        #         cc += 1
        #         # if s[row] == s[col]:
        #         #     if row + 1 <= col - 1:
        #         #         if dp_table[row+1][col-1] == 1:
        #         #             dp_table[row][col] = 1
        #         #             self.update_max_point(row, col)
        #         #     else:
        #         #         dp_table[row][col] = 1
        #         #         self.update_max_point(row, col)

        #         row += 1
        #         col += 1

        #     row_max -= 1
        #     delta += 1

        c3 = time.time()
        print('c3-c1:', c3-c1)

        print(len_s)
        print(cc)
        # print(dp_table)
        # print(self.max_point)
        a, b = self.max_point
        return s[a: b + 1]

if __name__ == '__main__':
    s = Solution()

    # print(s.longestPalindrome('ababaaa'))

    # print(s.longestPalindrome("babad"))

    # assert s.longestPalindrome("rfvtmdqjppztlvotnstyqeildrnevqkcoiqndxxncftlhdychrutvzkcxjnduhssfiatzisxioyuqmxqpdiouixfhyjlnfsjupwjztuyklrweuqmkuygndrqfhhcxrxcwdwcwgsknxxmxiwqxjbbljnckdgofehoarikioabmisfuzraxcaryjzsjetrvvpavbhbajrsnvrfjorjzpcjmkoekaipinfzhuaegaxzzvlwclbzhqzbtvxtgfhojqhcnokzqbedusoywsfsgbwxbvrqgmzojdmhlmzwtcvvmhnytqqlkpwyesbztabhyfukhpbchhvtzoegykvbzrywjcntrmsyokklsnzwkpjdcdcayfauuxcydiubnonpumcogiwqsqzagxhwbvkcxojfvewzqjdbbwbudxndyvubbumrktckrgxtbanatsfsxtckueqqtldfnxeznozegxnzntynlfavlmdfgpwgebylkromwrwxflgylbrtbyjblvgrxlkuhwnjmzqkngdghjvrsgtppkgsmpxrsahxlakadliwxmnbztfadwoglocbvwvhgcmgnkdtlbnqbfepbupfticejjxjoogutfvckdvztgjuklczwiimstpstbreffkvcmvofanuxndahhftbvsbfgoagwptvszptjatyoemevxnpqxboiycubeoqfenopwcbzbfnqtixtqrpzatq") == 'cwdwc'

    s.longestPalindrome('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')



    print('Done.')
