public class Solution {
public static int maxValidWindowSum(int[] nums, int k) {
   int l = 0;
   int windowsum = 0;
   int negative = 0;
   int max = 0;

   for(int r = 0; r<nums.length; r++) {
      windowsum+=nums[r];
      if(nums[r]<0)
         negative++;
   }

   if(r-l+1>k) {
      if(nums[l]<0)
         negative--;
      windowsum -= nums[l];
      l++;
}

if(r-l+1 == k && negative <=1)
   max = Math.max(max, windowsum);


   return max;
}
}