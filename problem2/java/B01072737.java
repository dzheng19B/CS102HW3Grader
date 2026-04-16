public class Solution {
public static int countPairs(int[] nums, int T) {
	int left = 0;
	int right = nums.length - 1;
	int count = 0;

	while (left < right) {
		if (nums[left] + nums[right] <= T) {
			count += (right - left);
			left++;
		} else {
			right--;
		}
	}
	return count;
}
}