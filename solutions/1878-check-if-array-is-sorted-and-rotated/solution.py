class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sorted_nums = sorted(nums)
        n = len(nums)

        for rotations in range(n):
            rotated = sorted_nums[rotations:] + sorted_nums[:rotations]

            if rotated == nums:
                return True
        return False
        
