class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # n = len(digits)
        # x = digits[n-1] + 1
        # digits.remove(digits[n-1])
        # digits.append(x)
        # return digits

        my_num = int("".join(map(str, digits)))
        x = my_num + 1
        reorder = [int(a) for a in str(x)]

        return reorder

        
