class Solution(object):
    def closedIsland(self, grid):
        row , col = len(grid), len(grid[0])

        def dfs(i,j):
            if i < 0 or i == row or j < 0 or j == col:
                return 0
            if grid[i][j] == 1:
                return 1

            grid[i][j] = 1

            return (dfs(i+1,j) & dfs(i-1,j) & dfs(i,j+1) & dfs(i,j-1))

        ans = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    ans += dfs(i,j)

        return ans

