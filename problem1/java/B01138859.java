public class Solution {
public static int maxValidWindowSum(int[] nums, int k)
    {
        boolean first = true;
        int sum = 0;
        int ans = 0;
        int numNeg = 0;
        int left = 0;
        int right = 0;
        while (right < nums.length)
        {
            if (right - left < k)
            {
                if (nums[right] < 0)
                {
                    numNeg++;
                }
                sum += nums[right];
                right++;
            }
            else
            {
                if (numNeg <= 1)
                {
                    if (first)
                    {
                        ans = sum;
                    }
                    else
                    {
                        ans = Math.max(ans,sum);
                    }
                    first = false;
                }
                if (nums[left] < 0)
                {
                    numNeg--;
                }
                if (nums[right] < 0)
                {
                    numNeg++;
                }
                sum -= nums[left];
                sum += nums[right];
                left++;
                right++;
            }
        }
        if (numNeg <= 1)
        {
            ans = Math.max(ans,sum);
        }
        return ans;
    }
}