class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        row, col = len(grid), len(grid[0])

        def dfs(i,j):
            if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] == 0:
                return 0

            val = grid[i][j]
            grid[i][j] = 0

            total_sum = val
            total_sum += dfs(i+1, j)
            total_sum += dfs(i-1, j)
            total_sum += dfs(i, j+1)
            total_sum += dfs(i, j-1)

            return total_sum

        total_island = 0

        for i in range(row):
                for j in range(col):
                    if grid[i][j] > 0:
                        island_sum = dfs(i,j)
                        if island_sum % k == 0:
                            total_island +=1
        return total_island
        
