class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # target = max(nums)
        # return sum(target - num for num in nums)
        return len(nums) * max(nums) - sum(nums)

        
