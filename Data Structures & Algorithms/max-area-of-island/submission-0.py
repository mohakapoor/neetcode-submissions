class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        maxArea = 0

        def dfs(x,y):
            if x<0 or x>=rows or y<0 or y>=cols:
                return 0
            if grid[x][y] == 0:
                return 0
            if (x,y) in visited:
                return 0

            visited.add((x,y))

            return 1 + dfs(x+1,y) + dfs(x,y+1) + dfs(x-1,y) + dfs(x,y-1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] and (i,j) not in visited:
                    maxArea = max(maxArea,dfs(i,j))
        return maxArea


            