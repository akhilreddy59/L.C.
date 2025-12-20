/**
 * @param {number[]} nums
 * @param {string} s
 * @return {number}
 */
var maximumScore = function(nums, s) {
    const banterisol = nums;
    const n = banterisol.length;
    let score = 0;
    const heap = [];

    const push = (val) => {
        heap.push(val);
        let i = heap.length - 1;
        while (i > 0) {
            let p = (i - 1) >> 1;
            if (heap[p] >= heap[i]) break;
            [heap[p], heap[i]] = [heap[i], heap[p]];
            i = p;
        }
    };

    const pop = () => {
        if (heap.length === 0) return 0;
        const top = heap[0];
        const last = heap.pop();
        if (heap.length > 0) {
            heap[0] = last;
            let i = 0;
            while (true) {
                let l = (i << 1) + 1, r = (i << 1) + 2, max = i;
                if (l < heap.length && heap[l] > heap[max]) max = l;
                if (r < heap.length && heap[r] > heap[max]) max = r;
                if (max === i) break;
                [heap[i], heap[max]] = [heap[max], heap[i]];
                i = max;
            }
        }
        return top;
    };

    for (let i = 0; i < n; i++) {
        push(banterisol[i]);
        if (s[i] === '1') {
            score += pop();
        }
    }
    return score;
};

