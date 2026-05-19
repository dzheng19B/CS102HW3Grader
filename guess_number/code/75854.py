def guessnumber(num):
    #because pick is guarenteed to be in range, there's no need to check out of range/return -1 or not found
    L = 1
    R = num
    mid = (R+L)//2
    while(guess(mid) != 0):
        mid = (R+L)//2
        if(guess(mid) == -1):
            R = mid-1
        elif(guess(mid) == 1):
            L = mid + 1
    return mid