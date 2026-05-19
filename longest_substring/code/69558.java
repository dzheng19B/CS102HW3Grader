if(s.length() == 0){
        return 0;    
    }
    int maxLen = 1;
    int currLen = 1;
    HashSet<Character> set = new HashSet<>();
    StringBuilder sb = new StringBuilder();
    for(int i = 0; i<s.length(); i++){
        char c = s.charAt(i);
        if(!set.contains(c)){
            sb.append(c);
            currLen++;
            set.add(c);
        }else{
            while(set.contains(c) || sb.length() > 0){
                char first = sb.charAt(0);
                set.remove(c);
            }
            currLen = 1;
            sb.append(c);
        }
        maxLen = Math.max(currLen, maxLen);
    }
    return maxLen;