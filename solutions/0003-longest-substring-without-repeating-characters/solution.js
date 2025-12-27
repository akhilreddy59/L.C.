/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    if (s.length == 1 || s.length == 0)
    return s.length;

    let res = 0, left = 0 , right = 0;
    let vis = new Array(26).fill(false);

    while(right < s.length ){
        while(vis[s[right].charCodeAt(0) - "a".charCodeAt(0)] === true ){
            vis[s[left].charCodeAt(0) - "a".charCodeAt(0)] = false;
            left++;
        }
        vis[s[right].charCodeAt(0) - "a".charCodeAt(0)] = true;

        res = Math.max(res , (right - left + 1));
        right++;
    }
    return res;
};
