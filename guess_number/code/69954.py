#-1 if its higher
#1 if its lower
#0 if equal 

#constraints x >= 1 
#guess() = some_number
#n is the upper limit 
#1, 2, 3, 4 ... n 
#n/2

def guessingGame(int n):
    lower = 1
    upper = n
    
    while(guess() != 0):
        middle = (upper + lower)/2
        if guess(middle) == 0:
            return middle
        
        if guess(middle) == -1:
            upper =  middle - 1
            
        if guess(middle) == 1:
            lower = middle + 1