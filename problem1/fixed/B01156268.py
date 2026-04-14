def max_valid_window_sum(nums, k):
    negative_count = 0
    for i in nums[:k]:
        if i < 0:
            negative_count += 1

    final_sum = None
    temp_sum = sum(nums[:k])
    
    if negative_count <= 1:
        final_sum = temp_sum
            
    for i in range(k, len(nums)):
        temp_sum += nums[i]
        if nums[i] < 0:
            negative_count += 1

        temp_sum -= nums[i - k]
        if nums[i - k] < 0:
            negative_count -= 1

        if negative_count <= 1:
            if final_sum is None or temp_sum > final_sum:
                final_sum = temp_sum
                return final_sum

    if final_sum == None:
        print(f"There are no valid windows of size {k}.")