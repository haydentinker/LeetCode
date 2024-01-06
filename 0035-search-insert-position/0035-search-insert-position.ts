function searchInsert(nums: number[], target: number): number {
    let l=0;
    let r=nums.length;
    let mid=0
    while (l<=r){
        mid=(r+l)>>1;
        if (nums[mid]==target){
            return mid;
        }
        else if (nums[mid]>target){
            r=mid-1;
        }else{
            l=mid+1;
        }
    }
    if(target>nums[mid]){
        return mid+1;
    }
    return mid;
};