class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        r_lst, d_lst = [], []
        n = len(senate)        
        
        for idx, c in enumerate(senate):
            if c == 'R':
                r_lst.append([idx, c])
            else:
                d_lst.append([idx, c])
                
        while r_lst and d_lst:
            r, d = r_lst.pop(0), d_lst.pop(0)
            r_idx, r_val = r[0], r[1]
            d_idx, d_val = d[0], d[1]
            if r_idx < d_idx:
                r[0] += n
                r_lst.append(r)
            else:
                d[0] += n
                d_lst.append(d)
                
        return "Radiant" if len(r_lst) > 0 else "Dire"
        
