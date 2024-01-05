function intersect(nums1: number[], nums2: number[]): number[] {
    let result: number[]=[];
    let nums1Dict={}
    for (let i=0;i<nums1.length;i++){
        if(nums1[i] in nums1Dict){
            nums1Dict[nums1[i]]+=1;
        }else{
            nums1Dict[nums1[i]]=1;
        }
    }
    for (let i=0;i<nums2.length;i++){
        if(nums1Dict[nums2[i]]){
            result.push(nums2[i])
            nums1Dict[nums2[i]]--;
        }
    }
    return result;
};