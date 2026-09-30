class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        required_index = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[required_index] = nums[i]
                required_index +=1
        return required_index
