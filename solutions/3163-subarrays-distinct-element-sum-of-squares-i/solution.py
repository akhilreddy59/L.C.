class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = 0
        n = len(nums)

        for i in range(n):
            distint_val = set()
            for j in range(i, n):
                distint_val.add(nums[j])

                total_sum += len(distint_val) ** 2

        return total_sum
        
