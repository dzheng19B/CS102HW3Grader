def guessNumber (n: int) -> int:
        l, r = 0, n

        int guess (5)

        while l <= r:
                    mid = (1 + r) // 2
                    if nums [mid] == target:
                        return mid
                    elif nums [mid] < target:
                                l = mid + 1
                    else:
                            r = mid - 1

        return -1