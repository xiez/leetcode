import java.util.HashMap;
class Solution {
    HashMap<Integer, Integer> cache;
    
    public Solution() {
        cache = new HashMap<>();
    }
    
    private int countN(int n) {
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }
        
        if (cache.get(n) != null) {
            return cache.get(n);
        }
        
        int ret;
        if (n % 2 == 0) {
            ret = countN(n / 2);
        } else {
            ret = countN((n-1) / 2) + 1;
        }
        cache.put(n, ret);
        return ret;
    }
    public int[] countBits(int n) {
        int[] ret = new int[n+1];
        for (int i = 0; i <= n; i++) {
            ret[i] = countN(i);
        }
        
        return ret;
    }
}
