# note: example 1's output should totally be 5 instead of 4?
# since (2,4) should be a valid pair too

def count_pairs(nums, T):
  num_pairs = 0
  left = 0
  right = len(nums) - 1

  while left < right:
    if nums[left] + nums[right] > T:
      right -= 1
      continue

    num_pairs += right - left
    left += 1

  return num_pairs

""" typescript :D
function countPairs(nums: number[], T: number): number {
  let numPairs = 0;

  let left = 0;
  let right = nums.length - 1;

  while (left < right) {:
    if (nums[left] + nums[right] > T) {:
        right--;
        continue;
    }

    numPairs += right - left;
    left++;
  }

  return numPairs;
} """