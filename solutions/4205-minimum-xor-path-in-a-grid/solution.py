class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        i,j = len(grid), len(grid[0])
        
        dp = [[set() for _ in range(j)] for _ in range(i)]

        dp[0][0].add(grid[0][0])

        for r in range(i):
            for c in range(j):

                if r > 0:
                    for current_xor in dp[r-1][c]:
                        dp[r][c].add(current_xor ^ grid[r][c])

                if c > 0:
                    for current_xor in dp[r][c-1]:
                        dp[r][c].add(current_xor ^ grid[r][c])

        return min(dp[i-1][j-1])



        # def dfs(r,c,current_xor):
        #     current_xor ^= grid[r][c]

        #     if r == i-1 and c == j-1:
        #         return current_xor
            
        #     min_xor = float('inf')

        #     if r + 1 < i:
        #         min_xor = min(min_xor, dfs(r+1,c, current_xor))
            
        #     if c + 1 < j:
        #         min_xor = min(min_xor, dfs(r, c+1, current_xor))

        #     return min_xor
        # return dfs(0,0,0)
            
        
