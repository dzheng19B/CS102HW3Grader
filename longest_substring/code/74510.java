//

public int lengthOfLongestSubstring(String s) {
    HashSet<Character> seen = new HashSet<Character>();
    int maxLength = 0;
    int l = 0;

    for(int r = 0; r<s.length(); r++) {
        while(seen.contains(s.charAt(r))) {
            seen.remove(s.charAt(l));
            l++;
        }
        seen.add(s.charAt(r));

        if(r-l+1>maxLength) {
            maxLength = r-l+1;
        }
    }
    return maxLength;
}