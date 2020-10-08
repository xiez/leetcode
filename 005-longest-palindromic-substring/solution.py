class Solution(object):
    def __init__(self):
        self.max_point = (0, 0)
        self.max = 0

    def update_max_point(self, row, col):
        if col - row > self.max:
            self.max_point = (row, col)

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        len_s = len(s)
        dp_table = [[0] * len_s for _ in range(len_s)]

        row = 0
        delta = 0
        row_max = len_s

        while row < row_max:
            col = row + delta
            while True:
                if row >= len_s or col >= len_s:
                    row = 0
                    break

                if s[row] == s[col]:
                    if row + 1 <= col - 1:
                        if dp_table[row+1][col-1] == 1:
                            dp_table[row][col] = 1
                            self.update_max_point(row, col)
                    else:
                        dp_table[row][col] = 1
                        self.update_max_point(row, col)

                row += 1
                col += 1

            row_max -= 1
            delta += 1

        # print(dp_table)
        # print(self.max_point)
        a, b = self.max_point
        return s[a: b + 1]

if __name__ == '__main__':
    s = Solution()

    # print(s.longestPalindrome('ababaaa'))

    # print(s.longestPalindrome("babad"))

    assert s.longestPalindrome("rfvtmdqjppztlvotnstyqeildrnevqkcoiqndxxncftlhdychrutvzkcxjnduhssfiatzisxioyuqmxqpdiouixfhyjlnfsjupwjztuyklrweuqmkuygndrqfhhcxrxcwdwcwgsknxxmxiwqxjbbljnckdgofehoarikioabmisfuzraxcaryjzsjetrvvpavbhbajrsnvrfjorjzpcjmkoekaipinfzhuaegaxzzvlwclbzhqzbtvxtgfhojqhcnokzqbedusoywsfsgbwxbvrqgmzojdmhlmzwtcvvmhnytqqlkpwyesbztabhyfukhpbchhvtzoegykvbzrywjcntrmsyokklsnzwkpjdcdcayfauuxcydiubnonpumcogiwqsqzagxhwbvkcxojfvewzqjdbbwbudxndyvubbumrktckrgxtbanatsfsxtckueqqtldfnxeznozegxnzntynlfavlmdfgpwgebylkromwrwxflgylbrtbyjblvgrxlkuhwnjmzqkngdghjvrsgtppkgsmpxrsahxlakadliwxmnbztfadwoglocbvwvhgcmgnkdtlbnqbfepbupfticejjxjoogutfvckdvztgjuklczwiimstpstbreffkvcmvofanuxndahhftbvsbfgoagwptvszptjatyoemevxnpqxboiycubeoqfenopwcbzbfnqtixtqrpzatq") == 'cwdwc'
