/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var partitionArray = function(nums, k) {
    nums.sort((a, b) => a - b); 

    let count = 0;
    let i = 0;

    while (i < nums.length) {
        let start = nums[i];     
        count++;                 
        i++;

        while (i < nums.length && nums[i] - start <= k) {
            i++;
        }
    }

    return count;
};

