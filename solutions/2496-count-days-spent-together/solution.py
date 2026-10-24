class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def date_to_day_of_year(date_str):
            month = int(date_str[:2])
            day = int(date_str[3:])
            return sum(days_in_months[:month - 1]) + day

        # Determine overlap period
        start_date = max(arriveAlice, arriveBob)
        end_date = min(leaveAlice, leaveBob)

        start_day = date_to_day_of_year(start_date)
        end_day = date_to_day_of_year(end_date)

        return max(0, end_day - start_day + 1)
