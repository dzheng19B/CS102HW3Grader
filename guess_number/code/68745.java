public int guessNumber(int n){
  int L = 0;
  int R = n;
  while(guess((R-L)/2) != 0){
    if(guess((R-L)/2) == 1){
       L = ((R-L)/2) + L;
    } else{
       R = ((R-L)/2);
    }
  }
  return (R-L)/2;
}
