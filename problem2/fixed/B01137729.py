left = 0
right = lenOf(nums) - 1
counter = 0
while left <right:
    if nums[left]+ nums[right] <= T:
        counter += right-left