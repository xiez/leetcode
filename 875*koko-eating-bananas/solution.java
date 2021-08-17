class Solution {
    public int max(int[] piles) {
        int ret = -1;
        for (int i = 0; i < piles.length; i++) {
            if (piles[i] > ret) {
                ret = piles[i];
            }
        }
        return ret;
    }
    public boolean canEat(int n_bana, int[] piles, int h) {
        int hours = 0;
        for (int i = 0; i < piles.length; i++) {
            int hr = (int)Math.ceil(piles[i] / (n_bana * 1.0));
            //System.out.printf("-->< %d\n", hr);
            hours += hr;
            if (hours > h) {
                return false;
            }
        }
        return true;
    }
    public int minEatingSpeed(int[] piles, int h) {
        int l, r, res=0;
        l = 1;
        r = max(piles);
        
        while (l <= r) {
            int mid = (int)(l + r) / 2;
            //System.out.printf("%d, %d, %d\n", l, r, mid);
            if (canEat(mid, piles, h)) {
                res = mid;
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        
        return res;        
    }
}
