/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
let str = String(x);
    let a = str.split('').reverse().join('');
    if(str === a){
        console.log("True");
        return true;
    }
    else{
        console.log("False");
        return false;
    }
};
