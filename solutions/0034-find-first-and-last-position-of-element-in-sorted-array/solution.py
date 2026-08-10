class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = bisect.bisect_left(nums, target)
        end = bisect.bisect_right(nums, target) - 1

        if start < len(nums) and nums[start] == target:
            return [start, end]
        
        return [-1, -1]    
