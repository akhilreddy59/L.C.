class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        # sorted = nums.sort()
        min_v = min(nums)
        max_v = max(nums)

        set_nums = set(nums)
        # set_nums = {}
        missing_numbers = [num for num in range(min_v + 1, max_v) if num not in set_nums]

        return missing_numbers
