l = 0
negatives =  0
max  =  0

for each index r within nums length:
    if value at r is less than 0:
        increment negatives
        while num negatives is 2:
            if val at l is negative:
                decrement negatives
                increment l
                if r + l + 1 = k:
                    set max to the bigger value between max and the sum of all values from indices l to r
                    increment l

                    print max



















