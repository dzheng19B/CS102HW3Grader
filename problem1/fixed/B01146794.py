left=0
right=k-1 # fixed window of length k
sum=0
negCount=0
validWindow=False
maxSum=0
for i in range(0,right+1): #initializes sum to be the sum of all values in the starting window
    sum+=nums[i]
    if (nums[i]< 0):
        negCount +=1
        if negCount <= 1:#check if initial window's valid
        maxSum = sum
        validWindow = True

        while right < len(nums)-1:#until we reach the end of the list
        if nums[left] <0: #changes count of negatives if the removed element is negative
            negCount-=1
            sum-=nums[left]
            left+=1
            right+=1 #increments right side of window
            sum+=nums[right]
            if (nums[right]< 0):
                negCount +=1
                if sum >maxSum and negCount <=1: #checks if the sum of the current window is greater than our maximum if so set max to sum and if it's valid
                    validWindow = True
                    maxSum=sum
                    if not validWindow:
                        return "Window of length k could not be found"
                    return maxSum