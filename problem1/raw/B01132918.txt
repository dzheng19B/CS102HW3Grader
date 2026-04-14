def max_valid_window_sum(nums, k):
  window = nums[:k]
  max_num = 0

  while True:
    num_negatives = 0
    sum = 0
    for num in window:
      if num < 0: num_negatives += 1
      if num_negatives > 1: break
      sum += num

    if num_negatives > 1: break
    max_num = max(sum, max_num)

    window.pop(0)
    if k <= len(nums) - 1: window.append(nums[k])
    k += 1
    if k > len(nums): break

  return max_num
  

""" typescript code i poorly translated to python:
function maxValidWIndowSum(nums: number[], k: number): number {
  const window = nums.slice(0, k);
  let max = 0;

  do {
    const isValid = window.filter((num) => num < 0).length === 1;
    if (isValid) {
        const sum = window.reduce((acc, curr) => acc + curr, 0);
        max = Math.max(max, sum);
    }

    window.splice(0, 1);
    window.push(nums[k]);
    k++;
  } while (k <= nums.length);

  return max;
} """