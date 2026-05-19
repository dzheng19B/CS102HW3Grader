def guessNumber(n: int):
    
    start, end = 1, n


    while start <= end:
        
        pick = start + (end-start) // 2 
        
        if guess(pick) == 1:
            start = pick + 1

        elif guess(pick) == -1:
            end = pick - 1 

        else
            return pick; 
 
]