public class Solution {
public static int countPairs(int[] nums, int T) {
    int l = 0;
    int r = nums.length-1;
    int count = 0;

    while(l>r) {
        if(nums[l]+nums[r]<=T) {
            count += (r-l);
            l++;
        }
        else
            r--;
    }
    return 0;
}
}