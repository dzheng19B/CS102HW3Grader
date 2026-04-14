def max_valid_window_sum(nums, k):
    # Initialize variables for the first window
    window_sum = sum(nums[0:k])
    neg_count = 0
    for i in range(k):
        if nums[i] < 0:
            neg_count += 1
    # Track the maximum valid sum, start at 0 (return 0 if no valid window)
    max_sum = 0
    # Check if first window is valid
    if neg_count <= 1:
        max_sum = window_sum
    # Slide the window across the rest of the array
    for i in range(1, len(nums) - k + 1):
        # Add the new element entering the window (right side)
        window_sum += nums[i + k - 1]
        # Remove the element leaving the window (left side)
        window_sum -= nums[i - 1]
        # Update negative count based on what left and what entered
        if nums[i - 1] < 0:
            neg_count -= 1
        if nums[i + k - 1] < 0:
            neg_count += 1
        # If valid window, check against current max
        if neg_count <= 1:
            max_sum = max(max_sum, window_sum)
    
    return max_sum