class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        current_window_sum = 0

        for i in range(0, k):
            current_window_sum = current_window_sum + nums[i]

        max_sum = current_window_sum

        for i in range(k, len(nums)):
            current_window_sum = current_window_sum + nums[i] - nums[i - k]

            if current_window_sum > max_sum:
                max_sum = current_window_sum

        return max_sum / float(k) 

