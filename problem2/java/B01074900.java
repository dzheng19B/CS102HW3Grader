public class Solution {
public static int countPairs(int[] nums, int T) {
    // Paste this into your answer if you want to use Java

   //Set up two pointers
   int left = 0;
   int right = nums.length-1;
   int sum = 0;

   //Check for pairs
   while(left <= right){

      if((nums[left] + nums[right]) <= T){
            sum = (right - left);
            left++;
      }
      else if((nums[left] + nums[right]) > T){
            right--;
      }

   }

   return sum;

}
}