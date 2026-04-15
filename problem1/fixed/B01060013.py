def max_valid_window_sum(nums, k):
    n = len(nums)
    current_sum = 0
    neg_count = 0
    max_sum = float('-inf')
    found_valid = False

    # 1. Build the initial window of size k
    for i in range(k):
        current_sum += nums[i]
        if nums[i] < 0:
            neg_count += 1
    
    # Check if the first window is valid
    if neg_count <= 1:
        max_sum = current_sum
        found_valid = True

    # 2. Slide the window across the rest of the array
    for i in range(k, n):
        # Remove the element that is sliding out (at index i - k)
        out_element = nums[i - k]
        current_sum -= out_element
        if out_element < 0:
            neg_count -= 1
        
        # Add the element that is sliding in (at index i)
        in_element = nums[i]
        current_sum += in_element
        if in_element < 0:
            neg_count += 1
        
        # 3. If the current window is valid, update max_sum
        if neg_count <= 1:
            max_sum = max(max_sum, current_sum)
            found_valid = True

    return max_sum if found_valid else 0