/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
     if (strs.length === 0) return "";

    let store = strs[0];  // store the first word as a blueprint for other words to search

    for(let i = 0; i < store.length; i++){
        let check = store[i];

        for(let j = 1; j < strs.length; j++){
            if(i == strs[j].length || strs[j][i] != check){
                return store.slice(0,i);
            }
        }
    }
    return store;
};
