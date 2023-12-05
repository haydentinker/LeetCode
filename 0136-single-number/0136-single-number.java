class Solution {
    public int singleNumber(int[] nums) {
        int result=nums[0];
        int index=0;
        while (index<nums.length-1){
            result=result^nums[index+1];
            index++;
        }


        return result;
    }
}