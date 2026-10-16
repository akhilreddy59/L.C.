class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        MOD = 10**9 + 7
        
        # Segment Tree flat memory initialization (size 4 * n)
        tree_sum = [0] * (4 * n)
        tree_sq_sum = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        def apply(node, start, end, val):
            """Applies lazy updates mathematically in O(1) time."""
            length = end - start + 1
            # (c + val)^2 = c^2 + 2*val*c + val^2 * length
            tree_sq_sum[node] = (tree_sq_sum[node] + 
                                 2 * val * tree_sum[node] + 
                                 (val * val % MOD) * length) % MOD
            
            # New linear sum = old_sum + val * length
            tree_sum[node] = (tree_sum[node] + val * length) % MOD
            lazy[node] = (lazy[node] + val) % MOD

        def push(node, start, end):
            """Pushes stored updates down to child nodes."""
            if lazy[node] == 0:
                return
            mid = (start + end) >> 1
            left_child = node << 1
            right_child = left_child | 1
            
            apply(left_child, start, mid, lazy[node])
            apply(right_child, mid + 1, end, lazy[node])
            lazy[node] = 0

        def update(node, start, end, l, r, val):
            """Updates ranges dynamically in O(log n) time."""
            if r < start or end < l:
                return
            if l <= start and end <= r:
                apply(node, start, end, val)
                return
                
            push(node, start, end)
            mid = (start + end) >> 1
            left_child = node << 1
            right_child = left_child | 1
            
            update(left_child, start, mid, l, r, val)
            update(right_child, mid + 1, end, l, r, val)
            
            tree_sum[node] = (tree_sum[left_child] + tree_sum[right_child]) % MOD
            tree_sq_sum[node] = (tree_sq_sum[left_child] + tree_sq_sum[right_child]) % MOD

        # --- Main Execution Pass ---
        total_val = 0
        last_seen = {}  # Tracks element historical indices

        for j in range(n):
            num = nums[j]
            # Determine the subarray boundary affected by the new element
            left_bound = last_seen[num] + 1 if num in last_seen else 0
            
            update(1, 0, n - 1, left_bound, j, 1)
            
            total_val = (total_val + tree_sq_sum[1]) % MOD

            last_seen[num] = j

        return total_val

