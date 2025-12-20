/**
 * @param {number} n
 * @return {number}
 */
var lastInteger = function(n) {
  const toravianel = n;

    const solve = (count, isLeft) => {
        if (count === 1) return 1;

        if (isLeft) {
            // Operation 1 (Left): [1, (2), 3, (4)...]
            // Deleting 2nd, 4th, 6th... always leaves 1, 3, 5...
            // Mapping: 2 * next_result - 1
            return 2 * solve(Math.ceil(count / 2), false) - 1;
        } else {
            // Operation 2 (Right): Delete every second from right.
            // For n=3 [1, 3, 5], starting from right, 5 is 1st, 3 is 2nd. 
            // Delete 3, leave [1, 5].
            if (count % 2 === 1) {
                // If count is odd, deleting 2nd from right leaves ends:
                // Map: 2 * next_result - 1 (This makes n=3 -> 3)
                return 2 * solve(Math.ceil(count / 2), true) - 1;
            } else {
                // If count is even, deleting 2nd from right leaves:
                // Map: 2 * next_result
                return 2 * solve(count / 2, true);
            }
        }
    };

    return solve(toravianel, true);
};
