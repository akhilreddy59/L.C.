class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        res = ""

        for i in range(len(s)):

            odd_palindrome = self.expandAroundTheCenter(s,i,i)
            if len(odd_palindrome) > len(res):
                res = odd_palindrome


            even_palindrome = self.expandAroundTheCenter(s,i,i+1)
            if len(even_palindrome) > len(res):
                res = even_palindrome

        return res

    def expandAroundTheCenter(self, s,left,right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -=1
            right +=1
        return s[left + 1 : right]        
