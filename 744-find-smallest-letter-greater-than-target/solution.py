class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if letters[-1] <= target:
            return letters[0]

        return self.aux_next_greated_letter(letters, 0, len(letters) - 1, target)

    def aux_next_greated_letter(self, lst, low, high, target):
        if low > high:
            return lst[0]

        if low == high:
            return lst[low]

        mid = (low + high) // 2
        # print(f'mid: {mid}')
        if lst[mid] > target:
            # find in left part
            # print(f'find in left: {low}, {mid}')
            return self.aux_next_greated_letter(lst, low, mid, target)
        else:
            # print(f'find in right: {mid+1}, {high}')
            return self.aux_next_greated_letter(lst, mid + 1, high, target)


if __name__ == '__main__':
    s = Solution()

    l = ["c", "f", "j"]
    # assert s.nextGreatestLetter(l, 'd') == 'f'
    assert s.nextGreatestLetter(l, 'k') == 'c'
