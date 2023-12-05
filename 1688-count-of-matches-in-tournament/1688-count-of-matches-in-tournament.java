class Solution {
    public int numberOfMatches(int n) {      
        if (n==1){
            return 0;
        }
        int matchesPlayed=0;
        if (n%2==0){
            matchesPlayed=n/2;
        }else{
           matchesPlayed=(n-1)/2; 
        }
        return matchesPlayed+numberOfMatches(n-matchesPlayed);
    }
}