def count_pairs(nums, T):
    #kind of similar to two sum but this will run in O(n) b/c its one pass
    #initialize two pointers left on the left side going up the array and right on the right side going down the array, and count
    left = 0
    right = len(nums) - 1
    count = 0