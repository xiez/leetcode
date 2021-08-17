class Solution(object):
    def __init__(self):
        self.best_guess = -1
        
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def canEat(n_bana):
            hours = 0
            for p in piles:
                hs = math.ceil(p / (n_bana * 1.0))
                hours += hs
                if hours > h:
                    return False
                    
            return True
        
        low = min(piles)
        high = max(piles)
        
        while low < high + 1:
            mid = (high + low) / 2
            print(high, low, mid)
            
            if canEat(mid):
                self.best_guess = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return self.best_guess
