class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_s = list(s)
        vowel = set("aeiouAEIOU")
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and s[left] not in vowel:
                left +=1

            while left < right and s[right] not in vowel:
                right -=1

            if left < right:
                list_s[left], list_s[right] = list_s[right], list_s[left]
                left+=1
                right-=1
        return "".join(list_s) 
