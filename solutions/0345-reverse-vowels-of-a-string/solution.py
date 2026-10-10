class Solution(object):
    def reverseVowels(self, s):
        left = 0
        right = len(s) - 1
        list_s = list(s)
        vowels = set("aeiouAEIOU")

        while left < right:
            while left < right and s[left] not in vowels:
                left +=1
            while left < right and s[right] not in vowels:
                right -=1

            if left < right:
                list_s[left], list_s[right] = list_s[right], list_s[left]
                left +=1
                right -=1
        return "".join(list_s)

        """
        :type s: str
        :rtype: str
        """
        
        
        
