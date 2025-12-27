/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
let mergedArray = [...nums1 , ...nums2];

mergedArray.sort((a,b) => a - b);
let n = mergedArray.length;
let mid = Math.floor(n/2);

if(n % 2 === 0){      
     // if length of arr is even then [mid] and [mid-1] are added and divided by 2 for median
    return (mergedArray[mid - 1] + mergedArray[mid]) / 2;
}
else{
return mergedArray[mid];
}
};
