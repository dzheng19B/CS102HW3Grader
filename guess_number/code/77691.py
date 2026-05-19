def guessNumber(n: int) -> int:
    min = 1
    max = n
    while True:
        currGuess = min + ((max - min) // 2)
        guessRet = guess(currGuess)
        if (guessRet == 1):
            min = currGuess + 1
        if (guessRet == -1):
            max = currGuess - 1
        if (guessRet == 0):
            return currGuess
"""