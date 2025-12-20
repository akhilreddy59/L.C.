/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
    let seen = new Set();
    for(let i = nums.length-1; i >= 0; i--){
        if(seen.has(nums[i])){
            return Math.floor(i/3)+1;
        }
        seen.add(nums[i]);
    }
    return 0;
};
