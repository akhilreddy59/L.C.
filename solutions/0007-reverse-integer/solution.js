/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    const isNegative = x < 0
    const reversed = parseInt(Math.abs(x).toString().split('').reverse().join(''));
    const max_limit = Math.pow(2, 31);
    if (reversed > max_limit - 1) {
        return 0;
    }
    return isNegative ? -reversed : reversed;
};
