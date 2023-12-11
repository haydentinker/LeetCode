class Solution {
    public int findSpecialInteger(int[] arr) {
        Integer frequency=arr.length/4;
        Integer sameInt=0;
        Integer curr=arr[0];
        for(int i=1;i<arr.length;i++){
            if(arr[i]==curr){
                sameInt++;
                if (sameInt>frequency){
                    return curr;
                }
            }else{
                sameInt=1;
                curr=arr[i];
            }
        }
        return arr[0];
    }
}