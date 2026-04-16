public class Solution {
public static int maxValidWindowSum(int[] nums, int k) {
    int windowSum = 0;
    int negativeCount = 0;
    int maxSum = Integer.MIN_VALUE;


    for (int i = 0; i < k; i++) {
        windowSum += nums[i];
        if (nums[i] < 0) {
            negativeCount++;
        }
    }

    if (negativeCount <= 1) {
        maxSum = windowSum;
    }

    for (int i = k; i < nums.length; i++) {
        if (nums[i - k] < 0) {
            negativeCount--;
        }
        windowSum -= nums[i - k];
        windowSum += nums[i];
        if (nums[i] < 0) {
            negativeCount++;
        }
        if (negativeCount <= 1) {
            maxSum = Math.max(maxSum, windowSum);
        }
    }


    return maxSum == Integer.MIN_VALUE ? 0 : maxSum;
}
}