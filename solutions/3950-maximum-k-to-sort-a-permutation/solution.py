class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = -1

        for i in range(len(nums)):
            if nums[i] != i:
                ans = ans & nums[i]
        
        return max(0, ans
        )
        
