public int guessNumber(int n){
    int min= 1;
    int max = n;

    while(min<=max){
        int pick = n/2;
        int guess = guess(pick);
        if(guess == -1){
            min = pick-1;
        }
        else if(guess == 1){
            max = pick;
        else{
            return pick;
        }
    }
    return 0;

}