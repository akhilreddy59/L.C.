class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean_s = "".join(char.lower() for char in s if char.isalnum())
        return clean_s == clean_s[::-1] 

        # left , right = 0, len(s) - 1

        # while left < right :


        #     while left < right and not s[left].isalnum():
        #         left += 1
        #     while left < right and not s[right].isalnum():
        #         right -= 1

        #     if s[left].lower() != s[right].lower():
        #         return False
            
        #     left +=1
        #     right -=1

        # return True        
