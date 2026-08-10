class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = sorted(list(set(nums)))
        nums[:] = ans
        return len(ans)
        
