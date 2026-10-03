class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, value in enumerate(nums):
            compliment = target - value 

            if compliment in seen:
                return [seen[compliment], i]
            seen[value] = i
        return []
        
