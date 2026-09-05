class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a,2)
        y = int(b,2)

        ans = x + y
        return bin(ans)[2:]
        
