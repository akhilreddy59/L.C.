class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Helper function to compute the sum of digits
        def get_digit_sum(x):
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s
            
        n = len(nums)
        
        sorted_arr = sorted((get_digit_sum(x), x) for x in nums)
        
        target_indices = {val: idx for idx, (_, val) in enumerate(sorted_arr)}
        
        visited = [False] * n
        total_swaps = 0
        
        # Detect permutation cycles to calculate minimum swaps
        for i in range(n):
            if visited[i] or target_indices[nums[i]] == i:
                continue
                
            cycle_size = 0
            curr_idx = i
            
            # Traverse the cycle
            while not visited[curr_idx]:
                visited[curr_idx] = True
                curr_idx = target_indices[nums[curr_idx]]
                cycle_size += 1
                
            # A cycle of size K takes K - 1 swaps to sort
            if cycle_size > 1:
                total_swaps += (cycle_size - 1)
                
        return total_swaps

