class Solution(object):
    def __init__(self):
        self.best_guess = -1
                
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def canShip(cap):
            days_need = 1
            i = 0
            len_wei = len(weights)
            day_cap = cap
            
            while i < len_wei:
                if day_cap > 0 and day_cap - weights[i] >= 0:
                    day_cap -= weights[i]
                    i += 1
                else:
                    day_cap = cap
                    days_need += 1
                
            return True if days_need <= days else False
        
        low = max(weights)  # 10
        high = sum(weights) # 55
        while low < high + 1:
            mid = (high + low) / 2  # 32
            #print("mid", mid)
            if canShip(mid):
                self.best_guess = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return self.best_guess
