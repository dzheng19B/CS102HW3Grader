# -1 if the real number is lower
# 0 if the number is equal
# 1 if the real number is higher
# placeholder for testing
def guess(n: int) -> int:
    if (n == 42): return 0
    elif (n > 42): return -1
    else: return 1

def guessNumber(n: int) -> int:
    l = 1
    r = n
    
    while l <= r:
        mid = (l + r) // 2
        result = guess(mid)
        
        if result == -1:
            r = mid - 1
        elif result == 1:
            l = mid + 1
        else:
            return mid

    # no fallback case - we assume correctness

# testing
print(guessNumber(90))