public class Solution {
{
public static int maxValidWindowSum(int[] nums, int k) {
    int sum = 0;
    int neg = 0;
    int max = 0;
    for(int i = 0; i<k; i++){
        sum += nums[i];
        if(nums[i]<0){
            neg++;
        }
    }
    if(neg<=1){
        max = sum;
    }
    for(int i = 1; i<nums.length-k; i++){
        sum = sum + nums[i+k-1] - nums[i-1];
        if(nums[i+k-1] < 0){
            neg++;
        }
        if(nums[i-1] < 0){
            neg--;
        }
        if(neg<=1 && sum>max)
            max = sum;
        }
    }
    return max;
}
}