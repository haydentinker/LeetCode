class Solution {
    public int totalMoney(int n) {
        int result=0;
        int week=0;
        while (n>=7){
            for(int i=1;i<8;i++){
                result+=i+week;
            }
            week++;
            n-=7;
        }
        if (n>0){
            for (int i=1;i<=n;i++){
                result+=i+week;
            }
        }
        return result;
    }
}