def count_pairs(nums, T):
    # Paste this into your answer if you want to use Python
        left = 0
        right = len(nums) - 1
        total_pairs = 0
        while left < right:
            if nums[left] + nums[right] <= T:
                total_pairs = right - left #  updates with pointers
                left += 1 #  shift left
            else:
                right+=1 #  shift right if not
        return total_pairs