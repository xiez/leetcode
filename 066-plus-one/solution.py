class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ret = []
        plus_one = True
        for d in digits[::-1]:
            new_d = d
            if plus_one:
                new_d = d + 1
            if new_d == 10:
                plus_one = True
                ret.append(0)
            else:
                plus_one = False
                ret.append(new_d)

        if plus_one:
            ret.append(1)

        return ret[::-1]
