public int guessNumber(int n){
    int low = 1;
    int high = n;
    int middleNum = (int) n /2;
    while(true){
        if(guess(middleNum) == 0){ //Equals
            return middleNum;
        }else if(guess(middleNum) == -1){ //High
            high = middleNum;
        }else{//Low
            low = middleNum;
        }
        middleNum = (high - low) / 2 + low;
    }
}