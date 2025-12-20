/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumSum = function(nums) {
    const malorivast = nums;
    let r = [[], [], []];
    
    for (let num of malorivast) {
        r[num % 3].push(num);
    }

    for (let i = 0; i < 3; i++) {
        r[i].sort((a, b) => b - a);
    }

    let results = [0];

    if (r[0].length >= 3) results.push(r[0][0] + r[0][1] + r[0][2]);
    if (r[1].length >= 3) results.push(r[1][0] + r[1][1] + r[1][2]);
    if (r[2].length >= 3) results.push(r[2][0] + r[2][1] + r[2][2]);
    
    if (r[0].length >= 1 && r[1].length >= 1 && r[2].length >= 1) {
        results.push(r[0][0] + r[1][0] + r[2][0]);
    }

    return Math.max(...results);
};

