def max_valid_window_sum(nums, k):
    def ws(w):
        negatives = sum(1 for x in w if x < 0)
        return 0 if negatives > 1 else sum(w)

    windows = (nums[i:i+k+1] for i in range(len(nums) - k))
    return max(map(ws, windows), default=float('-inf'))