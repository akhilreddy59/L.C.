class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        position = bisect.bisect_left(nums, target)
        return position
        
