
class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> ret = new ArrayList<Integer>();
        
        for (int i=0; i < nums.length; i++) {
            int idx = Math.abs(nums[i]) -1;          
            if (nums[idx] < 0) {
                ret.add(idx+1);
            }
            nums[idx] *= -1;
        }
        
        return ret;
    }
}
